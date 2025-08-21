import streamlit as st
from components import sidebar
import time
import re

def show_loading_screen():
    with st.spinner("Loading your itinerary..."):
        time.sleep(1.5)

def itinerary_page():
    show_loading_screen()
    sidebar.sidebar_nav()
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
    </style>
    """, unsafe_allow_html=True)
    data = st.session_state.get("itinerary_data", None)
    if not data:
        st.warning("⚠️ No itinerary found. Please go back and generate one.")
        st.stop()
    hotel_info_raw = data.get("Hotel", "No hotel info found")
    lines = hotel_info_raw.split("\n")
    hotel_line = lines[0].strip()
    maps_line = lines[1].replace("Maps:", "").strip() if len(lines) > 1 else None
    match = re.match(r"^(.*)\s\((.*)\)$", hotel_line)
    if match:
        hotel_name, details = match.groups()
    else:
        hotel_name, details = hotel_line, ""
    st.markdown(f"""
    <div class="stItinerary">
        <h3 style="margin:0; color:#ffcb05;">🏨 {hotel_name}</h3>
        <p style="margin:0.5rem 0; color:#eee;">💰 {details}</p>
        {"<p>📍 <a href='"+maps_line+"' target='_blank' style='color:#9cf;'>View on Google Maps</a></p>" if maps_line else ""}
    </div>
    """, unsafe_allow_html=True)
    itinerary = data.get("Itinerary", {})
    if not itinerary:
        st.json(itinerary)
        st.stop()
    if "current_day" not in st.session_state:
        st.session_state.current_day = 0
    days = itinerary.get("days", [])
    if not days:
        st.info("No detailed day-wise itinerary available.")
        st.stop()
    current_day = days[st.session_state.current_day]
    st.title("📅 Travel Itinerary")
    st.subheader(f"📍 Day {current_day.get('day_number')} – {current_day.get('area_focus', '')}")
    st.markdown("### 🍴 Meals")
    meal_cols = st.columns(len(current_day["meals"]))
    for col, (meal_name, meal_info) in zip(meal_cols, current_day["meals"].items()):
        with col:
            html = f"""
            <div class="stItinerary">
                <h4 style="margin:0; color:#ffcb05;">🍽️ {meal_name}</h4>
                <p style="margin:0.3rem 0; color:#eee;">
                    ⏱ {meal_info.get('allocated_minutes', 'N/A')} mins
                </p>
            """
            if meal_info.get("suggested_restaurants"):
                html += "<ul style='margin:0.3rem 0; padding-left:1.2rem;'>"
                for r in meal_info["suggested_restaurants"]:
                    distance = f" ({r['distance_km_from_hotel']} km)" if r.get("distance_km_from_hotel") else ""
                    html += f"<li style='margin:0.2rem 0;'>🍴 {r['name']}{distance}</li>"
                html += "</ul>"
            html += "</div>"
            st.markdown(html, unsafe_allow_html=True)
    if current_day.get("items"):
        st.markdown("### 🎯 Activities & Spots")
        for item in current_day["items"]:
            duration = item.get('duration_minutes')
            distance = item.get('distance_km_from_hotel')
            details = []
            if duration is not None:
                details.append(f"⏱ {duration} mins")
            if distance is not None:
                details.append(f"📏 {distance} km")
            details_line = " | ".join(details) if details else ""
            html = f"""
            <div class="stItinerary">
                <h4 style="margin:0; color:#ffcb05;">{item['name']} ({item['type']})</h4>
                {"<p style='margin:0.3rem 0;'>" + details_line + "</p>" if details_line else ""}
            """
            if item.get("description"):
                html += f"<p style='margin:0.3rem 0; color:#eee;'>{item['description']}</p>"
            if item.get("top_activities"):
                html += f"<p style='margin:0.3rem 0; color:#ffcb05;'>✨ Activities: {item['top_activities']}</p>"
            if item.get("images"):
                html += "<div style='display:flex; gap:0.5rem; margin-top:0.5rem;'>"
                for img in item["images"][:5]: 
                    html += f"<img src='{img}' style='width:100%; border-radius:12px;' />"
                html += "</div>"
            html += "</div>"
            st.markdown(html, unsafe_allow_html=True)
    if current_day.get("maps_route_url"):
        st.markdown(f"[🗺️ View Route on Google Maps]({current_day['maps_route_url']})")
    if current_day.get("transportation_tips"):
        st.info(current_day["transportation_tips"])
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("⬅️ Previous") and st.session_state.current_day > 0:
            st.session_state.current_day -= 1
            st.rerun()
    with col3:
        if st.button("Next ➡️") and st.session_state.current_day < len(days) - 1:
            st.session_state.current_day += 1
            st.rerun()
