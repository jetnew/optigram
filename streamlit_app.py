import streamlit as st

st.title("Title of App")
st.header("Header")

user_input = st.text_input("Insert user input here")
st.text(f"This is what was typed: {user_input}")
