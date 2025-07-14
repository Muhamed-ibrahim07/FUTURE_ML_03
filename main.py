import streamlit as st
from google.cloud import dialogflow_v2 as dialogflow
import uuid
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ur file here"

PROJECT_ID = "helpbot-anvc"

def get_dialogflow_response(user_input, session_id):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PROJECT_ID, session_id)

    text_input = dialogflow.TextInput(text=user_input, language_code="en")
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    return response.query_result.fulfillment_text


st.set_page_config(page_title="🤖 HelpBot Chat", page_icon="💬")
st.title("🤖 HelpBot - Customer Support Chatbot")
st.markdown("Talk to our friendly assistant below 👇")


if "history" not in st.session_state:
    st.session_state.history = []


with st.form(key="chat_form", clear_on_submit=True):
    user_message = st.text_input("Type your message", "")
    submitted = st.form_submit_button("Send")

if submitted and user_message:

    session_id = str(uuid.uuid4())

    bot_reply = get_dialogflow_response(user_message, session_id)


    st.session_state.history.append(("You", user_message))
    st.session_state.history.append(("Bot", bot_reply))


st.markdown("---")
for sender, message in st.session_state.history:
    if sender == "You":
        st.markdown(f"<div style='text-align: right; color: blue;'><b>{sender}:</b> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; color: green;'><b>{sender}:</b> {message}</div>", unsafe_allow_html=True)
