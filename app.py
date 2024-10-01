import streamlit as st
from utils.firebase_operations import initialize_firebase, upload_to_firebase  # Import your Firebase functions
from utils.history_with_ai import run_virtual_patient

st.set_page_config(layout="wide")

def main():
    # Initialize Firebase
    db = initialize_firebase()  # Call Firebase initialization
    
    # Initialize session state
    if "page" not in st.session_state:
        st.session_state.page = "welcome"  # Default page

    print(f"Current page: {st.session_state.page}")  # Debugging statement

    # Collect and upload session data whenever the page changes
    #previous_page = st.session_state.get("previous_page")
    #if previous_page != st.session_state.page:
    #    save_session_data(db)  # Pass db to the save function
    #    st.session_state.previous_page = st.session_state.page  

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

def save_session_data(db):
    session_data = collect_session_data()
    try:
        upload_message = upload_to_firebase(db, session_data)  # Pass db as an argument
        st.success(upload_message)  # Provide feedback to the user
    except Exception as e:
        st.error(f"Error saving progress: {e}")


def collect_session_data():
    session_data = {
        "unique_code": st.session_state.get("unique_code", ""),
        # ... add other session state variables here
    }
    return session_data

if __name__ == "__main__":
    main()
