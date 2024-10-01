import streamlit as st
from utils.firebase_operations import initialize_firebase, upload_to_firebase  # Import your Firebase functions
from utils.file_operations import load_users
from utils.welcome import welcome_page
from utils.login import login_page
from utils.intake_form import display_intake_form
from utils.history_with_ai import run_virtual_patient
from utils.simple_success1 import display_simple_success1


st.set_page_config(layout="wide")

def main():
    # Initialize Firebase
    db = initialize_firebase()  # Call Firebase initialization
    
    # Initialize session state
    if "page" not in st.session_state:
        st.session_state.page = "welcome"  # Default page

    print(f"Current page: {st.session_state.page}")  # Debugging statement

    # Page routing
    if st.session_state.page == "welcome":
        welcome_page()
    elif st.session_state.page == "login":
        users = load_users()
        login_page(users, db)
    elif st.session_state.page == "intake_form":
        display_intake_form(db)
    elif st.session_state.page == "virtual_patient":
        run_virtual_patient()
    elif st.session_state.page == "ending":
        display_simple_success1()
        
if __name__ == "__main__":
    main()
