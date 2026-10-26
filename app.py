
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









 


 
 




 





 




 
 













