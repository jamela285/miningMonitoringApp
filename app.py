
import sqlite3
import hashlib
import streamlit as st

st.set_page_config(page_title="Mining Monitoring Application", layout="wide")

conn = sqlite3.connect("mining_users.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL
    )
""")
conn.commit()

def hash_password(password):
    """Hash a password (use a dedicated password-hashing library in production)."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "Navigation"
if "incidents" not in st.session_state:
    st.session_state.incidents = {
        "incident_ids": [], "dates": [], "times": [], "shifts": [],
        "locations": [], "departments": [], "incident_types": [],
        "severities": [], "injury_statuses": [], "lost_time_injuries": [],
        "causes": [], "corrective_actions": [], "incident_statuses": []
    }
if "equipment" not in st.session_state:
    st.session_state.equipment = {
        "equipment_ids": [], "equipment_types": [], "manufacturers": [],
        "operating_hours": [], "temperatures": [], "vibrations": [],
        "fuel_consumptions": [], "brake_statuses": [], "tyre_statuses": [],
        "engine_statuses": [], "maintenance_statuses": [], "downtimes": [],
        "availabilities": []
    }

if "near_misses_records" not in st.session_state:
    st.session_state.near_misses_records = []

permissions = {
    "Administrator": ["Dashboard", "Worker Safety", "Safety Incidents", "Equipment database", "Equipment Monitoring", "Maintenance", "Risk Assessment", "Alerts & Notifications", "Manage Users"],
    "Safety Officer": ["Dashboard", "Worker Safety", "Safety Incidents", "Risk Assessment", "Alerts & Notifications"],
    "Mining Engineer": ["Dashboard", "Worker Safety", "Safety Incidents", "Equipment database", "Equipment Monitoring", "Maintenance", "Risk Assessment", "Alerts & Notifications"],
    "Maintenance Engineer": ["Dashboard", "Equipment database", "Equipment Monitoring", "Maintenance", "Alerts & Notifications"],
    "Manager": ["Dashboard", "Worker Safety", "Safety Incidents", "Equipment database", "Equipment Monitoring", "Maintenance", "Risk Assessment", "Alerts & Notifications"]
}


def navigation_page():
    st.title(" Mining Management System")
    st.subheader("Welcome to the Mining Management System")
    st.write("Please sign up to create your account, or log in if you already have an account.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("CREATE ACCOUNT", use_container_width=True):
            st.session_state.page = "Sign Up"
            st.rerun()
    with col2:
        if st.button("LOGIN", use_container_width=True):
            st.session_state.page = "Login"
            st.rerun()






 


 
 




 





 




 
 













