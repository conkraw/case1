import streamlit as st
import json
import openai
from docx import Document
import time

import streamlit as st
import openai

# Set up OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Initialize the message history in session state
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Role play a parent who is going to receive bad news from a doctor."}
    ]

def get_chatgpt_response(user_input):
    # Append the user input to the message history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Call the OpenAI API with the full message history
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )
    
    # Get the assistant's response and append it to the message history
    assistant_response = response['choices'][0]['message']['content']
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    
    return assistant_response

def run_virtual_patient():
    st.title("Virtual Patient: Case #1")

    user_input = st.text_input("Ask the virtual patient a question about their symptoms:")
    
    if st.button("Submit") and user_input:
        virtual_patient_response = get_chatgpt_response(user_input)
        st.write(f"Virtual Patient: {virtual_patient_response}")

if __name__ == "__main__":
    run_virtual_patient()



