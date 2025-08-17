import streamlit as st

def load_styles():
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(to top, rgba(0,0,0,0.5)50%,rgba(0,0,0,0.5)50%), 
        url("https://images.unsplash.com/photo-1488565546156-63ec9134f11e?q=80&w=1170&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    /* Navbar */
    .navbar {
        display: flex;
        align-items: center;
        padding: 1rem 2rem;
        background-color: rgba(255, 255, 255, 0.1);
    }
    .navbar img {
        height: 40px;
        align-items:center;
    }

    /* Hero */
    .hero {
        text-align: center;
        padding: 20px 0;
        color: white;
    }
    .hero h1 span {
        color: #4285F4;
    }

    /* Buttons */
    .button {
        background-color: white;
        color: black;
        padding: 0.8rem 1.5rem;
        font-size: 1rem;
        border-radius: 8px;
        cursor: pointer;
        font-weight: bold;
        border: none;
    }
    .button:hover {
        background-color: grey;
    }
    /* Image gallery */
    .gallery {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 1rem;
        padding: 2rem;
        background-color: rgba(255,255,255,0.1);
    }
    .gallery img {
        width: 300px;
        height: 200px;
        object-fit: cover;
        border-radius: 12px;
    }
    /* Login/Register Box */
    .login-box {
        max-width: 400px;
        margin: 2rem auto;
        padding: 2rem;
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)
