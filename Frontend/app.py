import streamlit as st
import requests

FastAPI_URL = "http://localhost:8000"

st.title("Pantry App")
st.write("Welcome to the Pantry App!")

UserNameInput = st.text_input("Enter your username:")
EmailInput = st.text_input("Enter your email:")
PasswordInput = st.text_input("Enter your password:", type="password")

#Uses the get endpoint NEEDS TO BE CONNECTED TO THE BACKEND
LoginButton = st.button("Login")

#Uses the post endpoint NEEDS TO BE CONNECTED TO THE BACKEND
SignupButton = st.button("Sign Up")