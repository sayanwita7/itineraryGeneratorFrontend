import streamlit as st
import requests
import os
from dotenv import load_dotenv
from page import home, landing, login, preferences, register, profile, itinerary
from styles import load_styles

load_dotenv()
load_styles()
st.set_page_config(page_title="Tripzy", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "home"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.page == "home":
    home.home_page()
elif st.session_state.page == "login":
    login.login_page()
elif st.session_state.page == "register":
    register.registration_page()
elif st.session_state.page == "landing":
    landing.landing_page()
elif st.session_state.page == "preferences":
    preferences.preferences_page()
elif st.session_state.page == "itinerary":
    itinerary.itinerary_page()
elif st.session_state.page == "profile":
    profile.profile_page()
