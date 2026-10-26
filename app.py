
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







 


 
 




 





 




 
 













