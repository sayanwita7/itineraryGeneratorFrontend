import streamlit as st
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def preferences_page():
    st.markdown("<h2 style='text-align: center;'>✈️ Travel Preferences</h2>", unsafe_allow_html=True)
    st.caption("Just a few details and **Tripzy** will plan your trip!")

    col1, col2 = st.columns(2)
    with col1:
        trip_length = st.number_input("Trip Length ⏰", min_value=1, step=1)
    with col2:
        budget = st.selectbox("Budget 💳", ["Low", "Mid", "High"])
    col3, col4 = st.columns(2)
    with col3:
        options = { 
            "🧍 Solo - Discovering on Your Own": "solo", 
            "💑 Partner - Exploring with a Loved One": "partner", 
            "👨‍👩‍👧 Family - Traveling with Family": "family", 
            "👯 Friends - Exploring with Friends": "friends" }
        choice = st.radio("Traveling With 🚗", list(options.keys())) 
        travel_with = options[choice]
    with col4:
        arrival_at = st.radio( "Arrival Point 📍", ["Howrah Railway Station", "Sealdah Railway Station/ Esplanade Bus Stand", "Dumdum Airport"] )

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🚀 Plan", use_container_width=True):
            try:
                uri=os.getenv("FETCH_URL")
                response = requests.post(
                    uri, 
                    json={
                        "duration": trip_length,
                        "budget": budget,
                        "grouptype": travel_with,
                        "arrival": arrival_at
                    }
                )
                data = response.json()
                if "suggestions" in data:
                    st.success(data["suggestions"])
                    st.rerun()
                elif "Error" in data: 
                    st.error(data["Hotel"])
                else:  
                    st.error("Prediction failed. Try again.")
            except requests.exceptions.RequestException as e:
                st.error(f"Server error: {e}")

    with c2:
        if st.button("⬅ Back", use_container_width=True):
            st.session_state.page = "landing"
            st.rerun()
