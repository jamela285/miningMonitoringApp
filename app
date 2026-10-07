import streamlit as st

st.title("Mining Monitoring Application")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "administrator123" and password == "administrator987":
        st.success("Login successful")
        st.write("Role: Administrator")
    elif username == "safety123" and password == "safety987":
        st.success("Login successful")
        st.write("Role: Safety Officer")
    elif username == "mining123" and password == "mining987":
        st.success("Login successful")
        st.write("Role: Mining Engineer")
    elif username == "maintenance123" and password == "maintenance987":
        st.success("Login successful")
        st.write("Role: Maintenance Engineer")
    elif username == "manager123" and password == "manager987":
        st.success("Login successful")
        st.write("Role: Manager")
    else:
        st.error("Invalid username or password")
