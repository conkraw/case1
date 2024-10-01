import streamlit as st
import json
import openai
from docx import Document
import time

# Set up OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_chatgpt_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": "Role play a parent who is going to receive bad news from a doctor."}
        ]
    )
    return response['choices'][0]['message']['content']

def run_virtual_patient():
    st.title("Virtual Patient: Case #1")

    st.info(
        "You will have the opportunity to communicate with a parent. "
        "You will be limited to 15 minutes. Alternatively, you may end the session."
    )

    # Initialize start_time only if it's not already set
    if 'start_time' not in st.session_state or st.session_state.start_time is None:
        st.session_state.start_time = time.time()

    # Calculate elapsed time
    elapsed_time = (time.time() - st.session_state.start_time) / 60

    # Display patient information
    if elapsed_time < 15:
        with st.form("question_form"):
            user_input = st.text_input("Introduce yourself to start the simulation.")
            submit_button = st.form_submit_button("Submit")

            if submit_button and user_input:
                virtual_patient_response = get_chatgpt_response(user_input)
                st.write(f"Virtual Patient: {virtual_patient_response}")
    else:
        st.warning("Session time is up. Please end the session.")
        if st.button("End Session"):
            st.session_state.start_time = None  # Reset start_time only when ending session
            st.session_state.page = "ending"
            st.success("Session ended. You can start a new session.")

    # Option to move to a new screen
    if st.button("End Session"):
        st.session_state.start_time = None
        st.session_state.page = "ending"
        st.rerun()
        st.write("Redirecting to a new screen...")


