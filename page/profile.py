import streamlit as st
import pandas as pd
import requests
from components import sidebar
import os
from dotenv import load_dotenv
load_dotenv()

def profile_page():
    sidebar.sidebar_nav()
    history_response = {
        "itineraries": st.session_state.get("itineraries", []),
        "user_info": st.session_state.get("user_info", {})
    }
    st.markdown("""
    <style>
        /* Background with darker overlay */
        [data-testid="stAppViewContainer"] {
            background-image:
                linear-gradient(to top, rgba(0,0,0,0.75)50%, rgba(0,0,0,0.75)50%),
                url("https://skysafar.in/wp-content/uploads/2024/05/Kolkata.png");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        /* Glassmorphism Itinerary Card */
        .stItinerary {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
            border: 1px solid rgba(255,255,255,0.2);
            font-size: 1rem;
            line-height: 1.5;
            color: #fff;
        }
        /* Subheader Styling */
        .stSubheader {
            font-size: 1.3rem;
            font-weight: 700;
            color: #ffcb05; /* bright accent */
            margin-bottom: 0.75rem;
        }    
        .stItinerary ul {
            margin: 0.3rem 0;
            padding-left: 1.2rem;
        }
        .stItinerary li {
            margin: 0.2rem 0;
        }
                /* Full-width table */
        .itinerary-table {
            width: 100%;
            border-collapse: collapse;
            color: #fff;
        }

        .itinerary-table th, .itinerary-table td {
            border: 1px solid rgba(255,255,255,0.2);
            padding: 10px;
            text-align: center;
        }

        .itinerary-table th {
            background: rgba(255, 203, 5, 0.2);
            color: #ffcb05;
            font-weight: bold;
        }
                
        /* Table Container */
        .itinerary-table {
            width: 100%;
            margin-top: 20px;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.2);
        }

        /* Table row styling */
        .itinerary-row {
            display: flex;
            border-bottom: 1px solid rgba(255,255,255,0.2);
            background: rgba(255,255,255,0.05);
            transition: 0.3s;
        }
        .itinerary-row:hover {
            background: rgba(255, 203, 5, 0.1);
        }

        /* Table cell styling */
        .itinerary-cell {
            flex: 1;
            padding: 12px;
            text-align: center;
            font-size: 0.95rem;
            color: #fff;
        }

        /* Header row */
        .itinerary-header {
            display: flex;
            background: rgba(255, 203, 5, 0.2);
            font-weight: bold;
            color: #ffcb05;
        }

        /* Styled button */
        div.stButton > button {
            background: #ffcb05;
            color: black;
            font-weight: 600;
            border-radius: 8px;
            border: none;
            padding: 6px 12px;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background: #ffdb4d;
            transform: scale(1.05);
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(f"""
        <div class="stItinerary">
            <h2 class="stSubheader">👤 {history_response['user_info'].get('name', '')} ({history_response['user_info'].get('username', '')})</h2>
            <p>📧 Email: {history_response['user_info'].get('email', '')}</p>
            <p>📞 Phone: {history_response['user_info'].get('phone', '')}</p>
        </div>
        """, unsafe_allow_html=True)
    itinerary_list = history_response["itineraries"]
    if itinerary_list:
        df = pd.DataFrame(itinerary_list)
        df_display = df.drop(columns=["itinerary_id"]).copy()
        header_cols = st.columns(len(df_display.columns) + 1)
        for i, col_name in enumerate(df_display.columns):
            header_cols[i].markdown(f"<div class='itinerary-cell'><b>{col_name}</b></div>", unsafe_allow_html=True)
        header_cols[-1].markdown(f"<div class='itinerary-cell'><b>Action</b></div>", unsafe_allow_html=True)
        for idx, row in df.iterrows():
            cols = st.columns(len(df_display.columns) + 1)
            for i, col_name in enumerate(df_display.columns):
                cols[i].markdown(f"<div class='itinerary-cell'>{row[col_name]}</div>", unsafe_allow_html=True)
            if cols[-1].button("View", key=f"view_{row['itinerary_id']}"):
                FETCH_IT_URL=os.getenv("FETCH_IT_URL")
                url = f"{FETCH_IT_URL}/{row['itinerary_id']}"
                response = requests.get(url)
                if response.status_code == 200:
                    st.session_state["itinerary_data"] = response.json()
                    st.session_state.page = "itinerary"
                    st.rerun()
                else:
                    st.error("Failed to fetch itinerary details")