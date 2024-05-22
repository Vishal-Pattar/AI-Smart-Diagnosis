import streamlit as st
import hashlib

# Function to generate MD5 hash of a password
def md5_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

# Login authentication function
def authenticate_login(predefined_password_hash):
    st.title("Login Authentication")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Hash the input password
        password_hash = md5_hash(password)

        # Check if the hashed password matches the predefined password hash
        if password_hash == predefined_password_hash:
            st.success("Login successful!")
            return True
        else:
            st.error("Invalid password. Please try again.")
            return False

# Function to store login state
def store_login_state(login_successful):
    st.session_state.login_successful = login_successful
