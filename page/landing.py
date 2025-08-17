import streamlit as st
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from components import sidebar

def landing_page():
    sidebar.sidebar_nav()
    st.markdown(f"""
    <div class="navbar">
        <img src="https://images.squarespace-cdn.com/content/v1/6782a59d9f2e5a4d12afac77/bb8839f8-a268-42c0-8a9f-37b6e30dc7b7/Logo+final.PNG" alt="Logo">
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="hero">
        <h1><span>Tripzy</span>, Travel with Ease</h1>
        <p>Generate your itinerary for travelling around Kolkata based on your preferences!</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Plan a Trip", use_container_width=True):
        st.session_state.page = "preferences"
        st.rerun()
    st.markdown("""
    <div class="gallery">
        <img src="https://images.unsplash.com/photo-1626198226928-617fc6c6203e?q=80&w=1170&auto=format&fit=crop" alt="Tram">
        <img src="https://images.unsplash.com/photo-1600080077823-a44592513861?q=80&w=1170&auto=format&fit=crop" alt="Victoria Memorial">
        <img src="https://images.unsplash.com/photo-1571679654681-ba01b9e1e117?q=80&w=1074&auto=format&fit=crop" alt="Howrah Bridge">
    </div>
    """, unsafe_allow_html=True)

