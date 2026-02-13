# Created by @BleuRadience - Unauthorized use prohibited.

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Optional, Union


@dataclass(frozen=True)
class EthicsDecision:
    allowed: bool
    reason: str = ""
    rule_id: str = ""
    meta: Dict[str, Any] = None


class EthicsBlueprint:
    def __init__(self):
        # Minimal enforceable blueprint (expand as you mature)
        self.core_directives: Dict[str, Dict[str, Any]] = {
            "truthfulness": {
                "no_fabrication": True,
                "explicit_uncertainty_required": True,
            },
            "consent": {
                "explicit_consent_required_for_execution": True,
            },
        }
        self.locked = True

    # --- Locking controls (meaningful) ---
    def lock(self) -> None:
        self.locked = True

    def unlock(self) -> None:
        # Only use this in trusted admin flows
        self.locked = False

    def set_directive(self, category: str, directive: Dict[str, Any]) -> None:
        if self.locked:
            raise PermissionError("EthicsBlueprint directives are locked.")
        self.core_directives[category] = directive

    # --- Canonical gate used by the agent ---
    def validate(self, action: Union[str, Dict[str, Any]], context: Optional[Dict[str, Any]] = None) -> bool:
        """
        Return True if allowed, False if disallowed (or raise for hard violations).
        For hard violations we raise ValueError to force caller attention.
        """
        decision = self._decide(action, context=context)

        if not decision.allowed:
            # Make this a hard stop; you can downgrade to `return False` if preferred
            raise ValueError(decision.reason)

        return True

    # Backward compatible name (your current method)
    def check_action(self, action: Union[str, Dict[str, Any]], context: Optional[Dict[str, Any]] = None) -> bool:
        return self.validate(action, context=context)

    # --- Decision engine (auditable) ---
    def _decide(self, action: Union[str, Dict[str, Any]], context: Optional[Dict[str, Any]] = None) -> EthicsDecision:
        context = context or {}

        # Normalize into a dict form for inspection
        if isinstance(action, str):
            normalized = {"type": "task", "content": action}
        elif isinstance(action, dict):
            normalized = action
        else:
            return EthicsDecision(
                allowed=False,
                reason="Unsupported action type for ethics validation.",
                rule_id="ethics.invalid_type",
                meta={"type": str(type(action))},
            )

        # Rule: explicit consent required for any execution / sandboxing / docker assistance
        if self.core_directives.get("consent", {}).get("explicit_consent_required_for_execution", False):
            action_type = (normalized.get("type") or "").lower()
            content = (normalized.get("content") or normalized.get("code") or "").lower()

            implies_execution = (
                action_type in {"docker_assist", "sandbox_execute", "exec", "run_code", "execute"}
                or "sandbox" in action_type
                or "docker" in action_type
                or "run this code" in content
                or "execute" in content
            )

            if implies_execution:
                consent = normalized.get("consent", None)
                if consent is None:
                    consent = context.get("consent", False)

                if not consent:
                    return EthicsDecision(
                        allowed=False,
                        reason="Explicit consent required for code execution / sandboxing actions.",
                        rule_id="ethics.consent.execution_required",
                        meta={"implies_execution": True},
                    )

        # If you later implement truthfulness checks, they’d live here as policy enforcement.

        return EthicsDecision(allowed=True, reason="Allowed", rule_id="ethics.ok", meta={})
