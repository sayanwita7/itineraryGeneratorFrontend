import streamlit as st
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def sidebar_nav():
    LOGOUT_URL = os.getenv("LOGOUT_URL")
    PROFILE_URL=os.getenv("PROFILE_URL")
    username = st.session_state.get("username", "Guest")
    st.sidebar.image(
        "https://images.squarespace-cdn.com/content/v1/6782a59d9f2e5a4d12afac77/bb8839f8-a268-42c0-8a9f-37b6e30dc7b7/Logo+final.PNG",
        use_container_width=True
    )
    st.sidebar.markdown(f"👋 Welcome, {username}")
    if st.session_state.get("page", "profile") != "profile":
        if st.sidebar.button("👤 Profile", key="profile_btn"):
            try:
                res=requests.post(PROFILE_URL, json={"username": username})
                data = res.json()
                if data:
                    st.session_state["itineraries"] = data["itineraries"]
                    st.session_state["user_info"] = data["user_info"]
                    st.session_state.page = "profile"
                    st.rerun()
                else:  
                    st.error("Profile fetch failed. Try again.")  
            except Exception as e:
                st.sidebar.error(f"Profile fetching error: {e}")
            
    if st.session_state.get("page", "landing") != "landing":
        if st.sidebar.button("🏠 Back to Landing Page", key="landing_btn"):
            st.session_state.page = "landing"
            st.rerun()
    if st.sidebar.button("🚪 Logout", key="logout_btn"):
        try:
            res = requests.get(LOGOUT_URL, timeout=5)
            if res.status_code == 200:
                st.sidebar.success("Logged out successfully!")
            else:
                st.sidebar.warning("Logout request failed.")
        except Exception as e:
            st.sidebar.error(f"Logout error: {e}")
        st.session_state.clear()
        st.session_state.page = "home"
        st.rerun()
