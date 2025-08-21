Tripzy - AI-Powered Itinerary Generator
Tripzy is a personalized trip planning tool built using Streamlit (Frontend) and Flask (Backend).  
It generates customized travel itineraries for touring around Kolkata based on preferences like trip duration, budget, travel group and arrival location.

Project Structure for frontend:
frontend/                       # Streamlit frontend
   ├── app.py                   # Main Streamlit UI file
   ├── style.py                 # File containing all common styling
   ├── page/                    # Pages
   ├── components/              # Common component across all pages
   ├── requirements.txt         # Frontend dependencies
   ├── venv/                    # Virtual environment (not pushed to GitHub)
   └── .env                     # Frontend environment variables

Project Setup Guide:
1. Clone the Repository and navigate to the directory:
git clone https://github.com/sayanwita7/itineraryGeneratorFrontend.git
cd itinerary-generator
2. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Mac/Linux
3. Install dependencies:
pip install -r requirements.txt
4. Run the streamlit app:
streamlit run app.py

Environment variables:
1. REGISTER_URL
2. LOGIN_URL
3. LOGOUT_URL
4. PROFILE_URL
5. FETCH_IT_URL
6. FETCH_URL



 
