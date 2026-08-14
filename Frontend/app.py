import streamlit as st
import requests

# Allows streamlit frontend to interact with the backend via fastapi endpoints
FastAPI_URL = "http://localhost:8000"

st.title("Pantry App")
st.write("Welcome to the Pantry App!")

# User info not in session state -> open login page
if ("username" not in st.session_state) or ("email" not in st.session_state):
    # Input boxes
    email_input = st.text_input("Enter your email:")
    username_input = st.text_input("Enter your username:")
    password_input = st.text_input("Enter your password:", type="password")

    # Uses the post endpoint
    signup_button = st.button("Sign Up")
    if signup_button:
        response = requests.post(
            f"{FastAPI_URL}/users",
            json={
                "username": username_input,
                "email": email_input,
                "password": password_input,
            },
        )
        if response.status_code == 200:
            st.success("User created successfully!")
        else:
            st.error("Error creating user")

    # Uses the get endpoint
    # A 200 error code only means the SQL query went through, not that a user was found, so the code checks the response to see if the user was found or not
    login_button = st.button("Login")
    if login_button:
        response = requests.get(
            f"{FastAPI_URL}/users",
            params={"username": username_input, "email": email_input},
        )
        if response.status_code == 200 and response.json().get("message") != "User not found":
            user_data = response.json()
            passcheck = requests.get(
                f"{FastAPI_URL}/users",
                params={
                    "username": username_input,
                    "email": email_input,
                    "password": password_input,
                },
            )
            user_pass_data = passcheck.json()
            if user_pass_data.get("message") == "User not found":
                st.error("Incorrect Credentials")
            elif user_data.get("users"):
                st.success("Login successful!")
                st.session_state["email"] = email_input
                st.session_state["username"] = username_input
                #rerun causes the script to run again with the session_state variables set, so it leaves the login page after pressing login with the right creds
                st.rerun()
        else:
            st.error("Error logging in")
elif("email" in st.session_state or "username" in st.session_state):
    st.write("ur in")