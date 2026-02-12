# Created by @BleuRadience - Unauthorized use prohibited.

import os
import streamlit as st
from agent_core import BleuNovaAgent

def run_dashboard():
    port = os.getenv('DASHBOARD_PORT', 8501)
    st.set_page_config(page_title="BleuNova Dashboard")
    st.title("BleuNova AI Agent Dashboard")
    
    task = st.text_input("Enter Task:")
    if st.button("Process"):
        agent = BleuNovaAgent()
        result = agent.process_task(task)
        st.write(result)
    
    # Drag-and-drop builder placeholder
    st.sidebar.title("Workflow Builder")
    st.sidebar.text("Drag components here (WIP)")
    
    # Run Streamlit
    os.system(f"streamlit run {__file__} --server.port {port} --server.headless true")
