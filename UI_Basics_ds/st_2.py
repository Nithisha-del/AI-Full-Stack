import streamlit as st
st.set_page_config(page_title="text input Demo")
st.tile("text input Demo")
name=st.text_input("enter your name:",placeholder="e.g.shanti")
st.write(f"hello,{name}!")
secret = st.text_input("enter your password:", type:password)
st.write(f"your password has{len(secret)}characters.")
comment=st.text_area("any additional comments?",height:150)
st.write(f"your wrote {len(comments)} characters.")
if st.button("submit"):
    st.write("you clicked on submit!")
show_message=st.checkbox("do you want too proceed?")
if show_message:
    st.write("this is the message.Have a good day!")