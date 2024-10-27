import streamlit as st
import requests
import pandas as pd

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

# def flat_page():
#     st.subheader("Flats")
#     response = requests.get(f"http://localhost:8000/flats/")
#     if response.status_code == 200:
#         flats = response.json()
#         for flat in flats:
#             st.write(f"Flat ID: {flat['flat_identifier']}, Owner : {flat['ownername']}, Rent : {flat['rent_per_room']}, Apartment Name : {flat['associated_apt_name']} ,Availability : {flat['availability']}")
#     else:
#         st.error("Failed to fetch flats")

def flat_page():
    st.title("Flats Overview")
    
    response = requests.get("http://localhost:8000/flats/")
    if response.status_code == 200:
        flats = response.json()
        
        # Convert the data to a pandas DataFrame
        df = pd.DataFrame(flats)
        
        # Reorder and rename columns for better presentation
        df = df[['flat_identifier', 'ownername', 'rent_per_room', 'associated_apt_name', 'availability']]
        df.columns = ['Flat ID', 'Owner', 'Rent', 'Apartment', 'Available']
        
        # Apply styling
        def highlight_availability(val):
            color = 'green' if val else 'red'
            return f'background-color: {color}; color: white;'
        
        styled_df = df.style.applymap(highlight_availability, subset=['Available'])
        
        # Display summary statistics
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Flats", len(df))
        col2.metric("Available Flats", df['Available'].sum())
        col3.metric("Average Rent", f"${df['Rent'].mean():.2f}")
        
        # Display the styled dataframe
        st.dataframe(styled_df, use_container_width=True)
        
        # Add a filter for availability
        st.subheader("Filter Flats")
        show_available = st.checkbox("Show only available flats")
        if show_available:
            filtered_df = df[df['Available'] == True]
            st.dataframe(filtered_df, use_container_width=True)
        
        # Display individual flat cards
        st.subheader("Flat Details")
        for _, flat in df.iterrows():
            with st.expander(f"Flat {flat['Flat ID']}"):
                col1, col2 = st.columns(2)
                col1.write(f"**Owner:** {flat['Owner']}")
                col1.write(f"**Apartment:** {flat['Apartment']}")
                col2.write(f"**Rent:** ${flat['Rent']}")
                col2.write(f"**Available:** {'Yes' if flat['Available'] else 'No'}")
    else:
        st.error("Failed to fetch flats data")

def owner_page():
    st.subheader("Flats")
    response = requests.get(f"http://localhost:8000/owners/")
    if response.status_code == 200:
        owners = response.json()
        for owner in owners:
            st.write(f"")
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
        
def fetch_session():
    if 'session_data' not in st.session_state:
        response = requests.get('http://127.0.0.1:8000/session_data', cookies={"sessionid": st.session_state.get('sessionid')})
        if response.status_code == 200:
            st.session_state['session_data'] = response.json()
        else:
            st.warning("Session expired. Please log in again.")
            st.session_state.logged_in = False
            st.rerun()

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if st.session_state.logged_in:
        page = st.sidebar.selectbox("Select Page", ["User Dashboard", "Flats", "Add Flat", "Interests", "Leases", "Apartments"])
        # fetch_session()
        if page == "Flats":
            flat_page()
        if page == "Owners":
            owner_page()
    else:
        login()

if __name__ == "__main__":
    main()
