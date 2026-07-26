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
if LoginButton:
    response = requests.get(f"{FastAPI_URL}/users", params={"username": UserNameInput, "email": EmailInput})
    if response.status_code == 200:
        user_data = response.json()
        passcheck = requests.get(f"{FastAPI_URL}/users", params={"username": UserNameInput, "email": EmailInput, "password": PasswordInput})
        user_pass_data = passcheck.json()
        if user_pass_data.get("message") == "User not found":
           st.error("Incorrect Password")
           print(user_data)
        elif user_data.get("users"):
            st.success("Login successful!")
        else:
            st.error("User not found")
    else:
        st.error("Error logging in")

#Uses the post endpoint NEEDS TO BE CONNECTED TO THE BACKEND
SignupButton = st.button("Sign Up")
if SignupButton:
    response = requests.post(f"{FastAPI_URL}/users", json={"username": UserNameInput, "email": EmailInput, "password": PasswordInput})
    if response.status_code == 200:
        st.success("User created successfully!")
      
    else:
        st.error("Error creating user")
      