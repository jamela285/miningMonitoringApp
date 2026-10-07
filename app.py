import streamlit as st

st.set_page_config(
    page_title="Mining Monitoring System",
    page_icon="⛏️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #f5f5f5;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #1f2937;
    margin-top: 30px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #6b7280;
    margin-bottom: 35px;
}

.login-box {
    max-width: 500px;
    margin: auto;
    padding: 35px;
    background-color: white;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">⛏️ Mining Monitoring System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Safety • Equipment • Risk Management</div>', unsafe_allow_html=True)

st.markdown('<div class="login-box">', unsafe_allow_html=True)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("LOGIN", use_container_width=True):
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

st.markdown('</div>', unsafe_allow_html=True)
