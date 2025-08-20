import streamlit as st
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def registration_page():
    st.markdown("<h2>Register</h2>", unsafe_allow_html=True)
    name = st.text_input("Full Name")
    uname = st.text_input("Username")
    email = st.text_input("Email")
    phno = st.text_input("Phone Number")
    password = st.text_input("Create Password", type="password")
    confirm_pass = st.text_input("Confirm Password", type="password")

    if st.button("Register", use_container_width=True):
        if password != confirm_pass:
            st.error("Passwords do not match")
        elif not all([name, uname, email, phno, password]):
            st.error("Please fill in all fields")
        else:
            try:
                uri=os.getenv("REGISTER_URL")
                response = requests.post(
                    uri, 
                    json={
                        "name": name,
                        "email": email,
                        "username": uname,
                        "phone": phno,
                        "password": password
                    }
                )

                data = response.json()
                if "message" in data:
                    st.success(data["message"])
                    st.session_state.page = "login"
                    st.rerun()
                elif "error" in data: 
                    st.error(data["error"])
                else:  
                    st.error("Registration failed. Please try again.")

            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {e}")

    if st.button("Back to Login", use_container_width=True):
        st.session_state.page = "login"
        st.rerun()

    if st.button("Back to Home", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
