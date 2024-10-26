import streamlit as st
import requests

# Define your base URL for API requests
BASE_URL = "http://localhost:8000/"

# Function for user login
def login():
    st.subheader("Login")
    contact_email = st.text_input("Email")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        response = requests.post(f"{BASE_URL}login/", json={'contact_email': contact_email, 'password': password})
        
        if response.status_code == 200:
            st.session_state.logged_in = True
            st.session_state.user_id = response.json().get('user_id')
            st.session_state.sessionid = response.json().get('sessionid')
            st.success(f"Login successful! {st.session_state.sessionid}")
            st.rerun()  # Refresh to reflect login
        else:
            st.error("Invalid credentials")

def flat_page():
    st.subheader("Flats")
    response = requests.get(f"http://localhost:8000/flats/")
    if response.status_code == 200:
        flats = response.json()
        for flat in flats:
            st.write(f"Flat ID: {flat['id']}, Rent: {flat['rent_per_room']}, Availability: {flat['availability']}")
    else:
        st.error("Failed to fetch flats")

# Function to display the dashboard
def dashboard():
    st.subheader("Dashboard")
    st.write("Welcome to your dashboard!")
    st.write("User ID:", st.session_state.user_id)
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.session_state.sessionid = None
        st.success("Logged out successfully")
        st.rerun()
# Function to manage session
def fetch_session():
    if 'session_data' not in st.session_state:
        response = requests.get('http://127.0.0.1:8000/session_data', cookies={"sessionid": st.session_state.get('sessionid')})
        if response.status_code == 200:
            st.session_state['session_data'] = response.json()
        else:
            st.warning("Session expired. Please log in again.")
            st.session_state.logged_in = False  # Set logged_in to False if session expired
            st.experimental_rerun()  # Refresh to go to login

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if st.session_state.logged_in:
        page = st.sidebar.selectbox("Select Page", ["User Dashboard", "Flats", "Add Flat", "Interests", "Leases", "Apartments"])
        # fetch_session()
        if page == "Flats":
            flat_page()
        if page == "Add Flat":
            add_flat()
    else:
        login()

if __name__ == "__main__":
    main()
