import streamlit as st
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def login_page():
    st.markdown("<h2>Login</h2>", unsafe_allow_html=True)
    uname = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", use_container_width=True):
        if not uname or not password:
            st.error("Please enter both username and password")
        else:
            try:
                uri=os.getenv("LOGIN_URL")
                response = requests.post(
                    uri,
                    json={"username": uname, "password": password}
                )
                data = response.json()
                if response.status_code == 200 and "userId" in data:
                    st.session_state.logged_in = True
                    st.session_state.username = uname
                    st.session_state.page = "landing"
                    st.rerun()

                elif "error" in data:
                    st.error(data["error"])
                else:
                    st.error("Login failed. Please try again.")

            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {e}")

    if st.button("Back to Home", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()
