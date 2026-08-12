import streamlit as st
import requests

# Allows streamlit frontend to interact with the backend via fastapi endpoints
FastAPI_URL = "http://localhost:8000"

st.title("Pantry App")
st.write("Welcome to the Pantry App!")

#input boxes
EmailInput = st.text_input("Enter your email:")
UserNameInput = st.text_input("Enter your username:")
PasswordInput = st.text_input("Enter your password:", type="password")

# Uses the post endpoint 
SignupButton = st.button("Sign Up")
if SignupButton:
    response = requests.post(f"{FastAPI_URL}/users", json={"username": UserNameInput, "email": EmailInput, "password": PasswordInput})
    if response.status_code == 200:
        st.success("User created successfully!")
    else:
        st.error("Error creating user")

# Uses the get endpoint
# A 200 error code only means the sql query went through, not that a user was found, so the code checks the response to see if the user was found or not
LoginButton = st.button("Login")
if LoginButton:
    response = requests.get(f"{FastAPI_URL}/users", params={"username": UserNameInput, "email": EmailInput})
    if response.status_code == 200 and response.json().get("message") != "User not found":
        user_data = response.json()
        passcheck = requests.get(f"{FastAPI_URL}/users", params={"username": UserNameInput, "email": EmailInput, "password": PasswordInput})
        user_pass_data = passcheck.json()
        if user_pass_data.get("message") == "User not found":
           st.error("Incorrect Credentials")
        elif user_data.get("users"):
            st.success("Login successful!")
    else:
        st.error("Error logging in")

      