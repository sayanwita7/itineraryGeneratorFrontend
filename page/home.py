import streamlit as st

def home_page():
    st.markdown("""
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

    col1, col2 = st.columns([1, 1], gap="small")
    with col1:
        if st.button("Sign In →", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()
    with col2:
        if st.button("Sign Up →", use_container_width=True):
            st.session_state.page = "register"
            st.rerun()
