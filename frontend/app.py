import os
os.environ["TORCH_USE_RTLD_GLOBAL"] = "1"
import streamlit as st
import uuid
import datetime
import requests
import sys
import os
sys.path.append(r'C:\Users\Bhushan\Desktop\rag_chatbot')
from backend.rag_knowledge import answer_question
st.set_page_config(page_title="RAG Complaint Chatbot", layout="centered")
st.title("💬 RAG Complaint Chatbot")

if "stage" not in st.session_state:
    st.session_state.stage = "start"
    st.session_state.complaint_data = {}
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

st.write("Talk to the chatbot by typing below.")

form = st.form("chat_form", clear_on_submit=True)
user_input = form.text_input("You:", key="input_box")
submitted = form.form_submit_button("Send")

if submitted and user_input:
    stage = st.session_state.stage
    data = st.session_state.complaint_data

    if stage == "start":
        if "complaint" in user_input.lower():
            st.session_state.stage = "name"
            st.chat_message("assistant").write("I'm sorry to hear that. Please provide your name.")
        elif any(x in user_input.lower() for x in ["what is", "how", "return"]):
            response = answer_question(user_input)
            st.chat_message("assistant").write(response)
        else:
            st.chat_message("assistant").write("I'm here to help with complaints and policy questions. How can I assist?")

    elif stage == "name":
        data['name'] = user_input
        st.session_state.stage = "phone"
        st.chat_message("assistant").write(f"Thank you, {data['name']}. What is your phone number?")

    elif stage == "phone":
        data['phone_number'] = user_input
        st.session_state.stage = "email"
        st.chat_message("assistant").write("Got it. What's your email address?")

    elif stage == "email":
        data['email'] = user_input
        st.session_state.stage = "details"
        st.chat_message("assistant").write("Thanks. Can you share the complaint details?")

    elif stage == "details":
        data['complaint_details'] = user_input
        try:
            response = requests.post("http://localhost:8000/complaints", json=data)
            if response.ok:
                res_data = response.json()
                complaint_id = res_data.get("complaint_id")
                created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.chat_message("assistant").markdown(f"""
                **Your complaint has been registered!**
                - Complaint ID: `{complaint_id}`
                - Name: {data['name']}
                - Phone: {data['phone_number']}
                - Email: {data['email']}
                - Details: {data['complaint_details']}
                - Created At: {created_at}
                """)
            else:
                st.chat_message("assistant").write("❌ Failed to register complaint. Please try again.")
        except Exception as e:
            st.chat_message("assistant").write(f"⚠️ Error: {e}")

        st.session_state.stage = "start"
        st.session_state.complaint_data = {}
        st.chat_message("assistant").write("How else can I help you today?")

