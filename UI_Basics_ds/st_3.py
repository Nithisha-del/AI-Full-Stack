import Streamlit as st
import time

st.set_page_config(page_title="ChatBot App Demo")
st.tile("ChatBot UI Demo")

with st.chat_message("assistant"):
    st.write("hello,I'm your assistant.Type something to get started ")
user_message=st.chat_input("Type something.....")
if user_message:
    with st.chat_message("user"):
        st.write(user_message)
    with st.chat_message("assistant"):
        with st.spinner("Thinking...."):
            time.sleep(1.5)
        st.write(f"hey you wrote:{user_message},but I'm in development.I can't reply.")