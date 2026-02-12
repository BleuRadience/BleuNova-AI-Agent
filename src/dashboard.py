# Created by @BleuRadience - Unauthorized use prohibited.

import os
import streamlit as st

def run_dashboard():
    # This should be called to start the streamlit server
    port = os.getenv('DASHBOARD_PORT', '8501')
    os.system(f"streamlit run src/dashboard_app.py --server.port {port} --server.headless true")

# This is the actual streamlit app
def main():
    st.set_page_config(page_title="BleuNova Dashboard")
    st.title("BleuNova AI Agent Dashboard")
    
    task = st.text_input("Enter Task:")
    if st.button("Process"):
        from agent_core import BleuNovaAgent
        agent = BleuNovaAgent()
        result = agent.process_task(task)
        st.write(result)
    
    # Workflow Builder placeholder
    st.sidebar.title("Workflow Builder")
    st.sidebar.text("Drag components here (WIP)")

if __name__ == "__main__":
    main()
