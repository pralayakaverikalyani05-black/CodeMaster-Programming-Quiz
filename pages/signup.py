import streamlit as st
import sqlite3

st.set_page_config(page_title="Sign Up", page_icon="📝")

st.title("📝 Create Your Account")

name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Create Account"):

    if name == "" or email == "" or password == "":
        st.error("Please fill all fields!")

    else:
        conn = sqlite3.connect("database/codemaster.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users(name,email,password) VALUES(?,?,?)",
                (name, email, password)
            )

            conn.commit()
            st.success("🎉 Account Created Successfully!")

        except sqlite3.IntegrityError:
            st.error("Email already exists!")

        conn.close()