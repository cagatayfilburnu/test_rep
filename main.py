import streamlit as st
import pandas as pd
import hashlib
from PIL import Image

# Initialize the user data DataFrame and auth status in session state if they don't exist
if 'users' not in st.session_state:
    st.session_state.users = pd.DataFrame(columns=['username', 'password'])
if 'auth_status' not in st.session_state:
    st.session_state.auth_status = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None


# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to register a new user
def register_user(username, password):
    if username in st.session_state.users['username'].values:
        return False
    new_user = pd.DataFrame([[username, hash_password(password)]], columns=['username', 'password'])
    st.session_state.users = pd.concat([st.session_state.users, new_user], ignore_index=True)
    return True


# Function to check login credentials
def login_user(username, password):
    hashed_password = hash_password(password)
    user = st.session_state.users[
        (st.session_state.users['username'] == username) & (st.session_state.users['password'] == hashed_password)]
    return not user.empty


# Function to display the registration page
def show_register_page():
    st.title("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    password_confirmation = st.text_input("Confirm Password", type='password')
    if st.button("Register"):
        if password == password_confirmation:
            if register_user(username, password):
                st.success("You have successfully registered!")
            else:
                st.error("Username already exists!")
        else:
            st.error("Passwords do not match!")


# Function to display the login page
def show_login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        if login_user(username, password):
            st.success("Logged in successfully!")
            st.session_state.auth_status = True
            st.session_state.current_user = username
        else:
            st.error("Invalid username or password")


# Function to display the operations page
def show_operations_page():
    st.markdown(f"Welcome, **{st.session_state.current_user}**!")

    st.balloons()
    st.markdown('<h1 style="color:orange;">İyi ki Doğdunnnnnnnnnnnnnnnnnnnnnnnnnnnnn',
                unsafe_allow_html=True)

    image = Image.open("ss2.jpeg")
    st.image(image)

    st.markdown('<h3 style="color:orange;">Doğum günün kutlu olsun Betüşşşşşşşşşşşşşşşşşşşşşşşşş',
                unsafe_allow_html=True)

    image = Image.open("ss1.jpg")
    st.image(image)

    st.markdown('<h3 style="color:green;">Çokçokçokkkkkkkkkkkkkkkkkkkkkkkkkk nice senelereeeeeeeeeeeee',
                unsafe_allow_html=True)

    VIDEO_URL = "https://www.youtube.com/watch?v=jLj4uqnvig4"
    st.video(VIDEO_URL)

    st.markdown(
        """
        ---
        Created with ❤️ by cagatay
        """
    )



# Main function to run the Streamlit app
def main():
    st.markdown('<h1 style="color:green;">Welcome to Trip Planner AI', unsafe_allow_html=True)
    st.sidebar.title("Navigation")

    if st.session_state.auth_status:
        page = st.sidebar.radio("Go to", ["Planner", "About ", "Logout"])

        if page == "Planner":
            show_operations_page()

        if page == "About":
            st.write("This is the about page")

        else:
            st.session_state.auth_status = False
            st.session_state.current_user = None
            st.sidebar.radio("Go to", ["Login", "Register"])
    else:
        page = st.sidebar.radio("Go to", ["Login", "Register", "Click after login"])

        if page == "Login":
            show_login_page()
        if page == "Register":
            show_register_page()
        if page == "Click after login":
            st.write("Waiting for login...")


if __name__ == '__main__':
    main()
