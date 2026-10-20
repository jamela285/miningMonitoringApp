
import sqlite3
import hashlib
import streamlit as st

# Set page configuration
st.set_page_config(
page_title="Mining Monitoring Application",
layout="wide"
)


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
  return hashlib.sha256(password.encode()).hexdigest()


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
"Administrator": [
"Dashboard", "Worker Safety", "Safety Incidents", "Equipment database",
"Equipment Monitoring", "Maintenance", "Risk Assessment",
"Alerts & Notifications", "Manage Users"
],
"Safety Officer": [
"Dashboard", "Worker Safety", "Safety Incidents",
"Risk Assessment", "Alerts & Notifications"
],
"Mining Engineer": [
"Dashboard", "Worker Safety", "Safety Incidents", "Equipment database",
"Equipment Monitoring", "Maintenance", "Risk Assessment", "Alerts & Notifications"
],
"Maintenance Engineer": [
"Dashboard", "Equipment database", "Equipment Monitoring",
"Maintenance", "Alerts & Notifications"
],
"Manager": [
"Dashboard", "Worker Safety", "Safety Incidents", "Equipment database",
"Equipment Monitoring", "Maintenance", "Risk Assessment", "Alerts & Notifications"
]
}


def navigation_page():
  st.title("⛏️ Mining Management System")
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

def signup_page():
  st.title("Create Your Account")
  st.write("Enter your details below. Your account information will be saved so you can log in again later.")

  full_name = st.text_input("Full Name", key="signup_name")
  username = st.text_input("Choose a Username", key="signup_username")
  password = st.text_input("Create a Password", type="password", key="signup_password")
  confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
  role = st.selectbox(
  "Select Your Role",
  ["Administrator", "Safety Officer", "Mining Engineer", "Maintenance Engineer", "Manager"]
  )

if st.button("SAVE ACCOUNT", use_container_width=True):
if not full_name.strip() or not username.strip() or not password:
 st.error("Please complete all required fields.")
elif password != confirm_password:
 st.error("The passwords do not match.")
elif len(password) < 8:
 st.error("Your password must contain at least 8 characters.")
else:
try:
 cursor.execute(
 "INSERT INTO users (full_name, username, password_hash, role) VALUES (?, ?, ?, ?)",
 (full_name.strip(), username.strip(), hash_password(password), role)
 )
 conn.commit()
 st.success("Account created successfully! You can now log in using your new credentials.")
 st.session_state.page = "Login"
 st.rerun()
 except sqlite3.IntegrityError:
 st.error("That username already exists. Please choose another username.")

if st.button("BACK TO NAVIGATION"):
 st.session_state.page = "Navigation"
 st.rerun()

def login_page():
 st.title("User Login")
 username = st.text_input("Username", key="login_username")
 password = st.text_input("Password", type="password", key="login_password")

if st.button("LOGIN", use_container_width=True):
 cursor.execute(
 "SELECT full_name, username, password_hash, role FROM users WHERE username = ?",
 (username.strip(),)
 )
 user = cursor.fetchone()

if user and user[2] == hash_password(password):
 st.session_state.logged_in = True
 st.session_state.full_name = user[0]
 st.session_state.username = user[1]
 st.session_state.role = user[3]
 st.session_state.page = "Home"
 st.rerun()
else:
 st.error("Invalid username or password.")

if st.button("CREATE A NEW ACCOUNT"):
 st.session_state.page = "Sign Up"
 st.rerun()
if st.button("BACK TO NAVIGATION"):
 st.session_state.page = "Navigation"
 st.rerun()

def home_page():
 st.title(f"Welcome, {st.session_state.full_name}!")
 st.success(f"You are logged in as: {st.session_state.role}")
 st.write("Welcome to your Mining Management System dashboard.")

allowed_modules = permissions.get(st.session_state.role, [])
module = st.sidebar.selectbox("Select Module", allowed_modules)

if st.sidebar.button("LOG OUT"):
 st.session_state.logged_in = False
 st.session_state.page = "Navigation"
for key in ["full_name", "username", "role"]:
 st.session_state.pop(key, None)
 st.rerun()


inc = st.session_state.incidents
eq = st.session_state.equipment

if module == "Dashboard":
 st.header("Mining Monitoring Dashboard")
 col1, col2, col3 = st.columns(3)
 col4, col5, col6 = st.columns(3)
 col7, col8, col9 = st.columns(3)
 col10, col11 = st.columns(2)

 col1.metric("Total Workers", 200)
 col2.metric("Total Safety Incidents", len(inc["incident_ids"]))
 col3.metric("Near Misses", sum(st.session_state.near_misses_records))
 col4.metric("High-Risk Observations", 0)
 col5.metric("PPE Compliance", "N/A")
 col6.metric("Total Equipment", len(eq["equipment_ids"]))
 col7.metric("Equipment Available", 0)
 col8.metric("Equipment Under Maintenance", 0)
 col9.metric("Equipment Alerts", 0)
 col10.metric("Average Equipment Availability", "N/A")
 col11.metric("Critical Equipment Alerts", 0)

elif module == "Worker Safety":
 st.header("Worker Health and Safety Monitoring")
 worker_id = st.text_input("Worker ID")
 department = st.text_input("Department")
 job_role = st.text_input("Job Role")
 shift = st.selectbox("Shift", ["Day", "Night"])
 ppe = st.selectbox("Is PPE compliance satisfactory?", ["Yes", "No"])
 training = st.selectbox("Is safety training up to date?", ["Yes", "No"])
 fatigue = st.selectbox("Enter fatigue level", ["Low", "Medium", "High"])
 observations = st.text_area("Enter Safety Observations")
 near_misses = st.number_input("Enter Number of Near Misses", min_value=0, step=1)
 previous_incidents = st.number_input("Enter Number of Previous Incidents", min_value=0, step=1)
 risk_level = st.selectbox("Enter Risk Level", ["Low", "Medium", "High"])

if st.button("Assess Worker Safety"):
 st.session_state.near_misses_records.append(near_misses)
 st.subheader("Worker Safety Record")
 st.write("Worker ID:", worker_id)
 st.write("Department:", department)
 st.write("Job Role:", job_role)
 st.write("Shift:", shift)
 st.write("PPE Compliance:", ppe)
 st.write("Safety Training:", training)
 st.write("Fatigue Level:", fatigue)
 st.write("Safety Observations:", observations)
 st.write("Near Misses:", near_misses)
 st.write("Previous Incidents:", previous_incidents)
 st.write("Risk Level:", risk_level)

 warnings = []
if ppe.lower() == "no":
 warnings.append("PPE compliance is unsatisfactory.")
if training.lower() == "no":
 warnings.append("Safety training is not up to date.")
if fatigue.lower() == "high":
 warnings.append("Worker has a high fatigue level.")
if near_misses > 0:
 warnings.append("Worker has recorded near misses.")
if previous_incidents > 0:
 warnings.append("Worker has previous safety incidents.")
if risk_level.lower() == "high":
 warnings.append("Worker has a HIGH risk level.")

 st.subheader("Safety Assessment")
if warnings:
 st.warning("Potentially unsafe conditions detected.")
for warning in warnings:
 st.write("⚠️", warning)
else:
 st.success("No major unsafe conditions detected.")
 st.success("Worker is currently considered safe.")
 st.info("Worker safety monitoring complete.")

elif module == "Safety Incidents":
 st.header("Safety Incident Database")
 option = st.selectbox(
 "Select an option",
 ["Add Incident", "View Incidents", "Search Incidents", "Filter Incidents", "Categorise Incidents", "Count Incidents", "Analyse Incident Trends"]
 )

if option == "Add Incident":
 incident_id = st.text_input("Incident ID")
 date = st.date_input("Date")
 time = st.time_input("Time")
 shift = st.selectbox("Shift", ["Day", "Night"])
 location = st.text_input("Location")
 department = st.text_input("Department")
 incident_type = st.text_input("Incident Type")
 severity = st.selectbox("Severity", ["Low", "Medium", "High"])
 injury_status = st.selectbox("Was there an injury?", ["Yes", "No"])
 lost_time_injury = st.selectbox("Was it a lost-time injury?", ["Yes", "No"])
 cause = st.text_input("Cause")
 corrective_action = st.text_input("Corrective Action")
 incident_status = st.selectbox("Incident Status", ["Open", "Closed"])

if st.button("Save Incident"):
 inc["incident_ids"].append(incident_id)
 inc["dates"].append(str(date))
 inc["times"].append(str(time))
 inc["shifts"].append(shift)
 inc["locations"].append(location)
 inc["departments"].append(department)
 inc["incident_types"].append(incident_type)
 inc["severities"].append(severity)
 inc["injury_statuses"].append(injury_status)
 inc["lost_time_injuries"].append(lost_time_injury)
 inc["causes"].append(cause)
 inc["corrective_actions"].append(corrective_action)
 inc["incident_statuses"].append(incident_status)
 st.success("Incident successfully added!")

elif option == "View Incidents":
if not inc["incident_ids"]:
 st.info("No incidents recorded.")
else:
for i in range(len(inc["incident_ids"])):
 st.subheader(f"Incident {i + 1}")
 st.write("Incident ID:", inc["incident_ids"][i])
 st.write("Date:", inc["dates"][i])
 st.write("Time:", inc["times"][i])
 st.write("Shift:", inc["shifts"][i])
 st.write("Location:", inc["locations"][i])
 st.write("Department:", inc["departments"][i])
 st.write("Incident Type:", inc["incident_types"][i])
 st.write("Severity:", inc["severities"][i])
 st.write("Injury Status:", inc["injury_statuses"][i])
 st.write("Lost-Time Injury:", inc["lost_time_injuries"][i])
 st.write("Cause:", inc["causes"][i])
 st.write("Corrective Action:", inc["corrective_actions"][i])
 st.write("Incident Status:", inc["incident_statuses"][i])

elif option == "Search Incidents":
 search = st.text_input("Enter Incident ID, Location or Department").lower()
if st.button("Search"):
 found = False
for i in range(len(inc["incident_ids"])):
if (search in inc["incident_ids"][i].lower() or
 search in inc["locations"][i].lower() or
 search in inc["departments"][i].lower()):
 st.write("Incident ID:", inc["incident_ids"][i])
 st.write("Date:", inc["dates"][i])
 st.write("Location:", inc["locations"][i])
 st.write("Department:", inc["departments"][i])
 st.write("Incident Type:", inc["incident_types"][i])
 st.write("Severity:", inc["severities"][i])
 found = True
if not found:
 st.warning("No matching incidents found.")

elif option == "Filter Incidents":
 filter_type = st.selectbox("Filter by", ["Severity", "Department", "Shift", "Incident Type"])
 value = st.text_input("Enter value").lower()
if st.button("Apply Filter"):
for i in range(len(inc["incident_ids"])):
if filter_type == "Severity":
 match = inc["severities"][i].lower() == value
elif filter_type == "Department":
 match = inc["departments"][i].lower() == value
elif filter_type == "Shift":
 match = inc["shifts"][i].lower() == value
else:
match = inc["incident_types"][i].lower() == value
if match:
 st.write(f"{inc['incident_ids'][i]} - {inc['incident_types'][i]} - {inc['severities'][i]}")

elif option == "Categorise Incidents":
 categories = list(set(inc["incident_types"]))
if not categories:
 st.info("No incidents recorded.")
else:
for category in categories:
 count = inc["incident_types"].count(category)
 st.write(f"{category}: {count} incident(s)")

elif option == "Count Incidents":
 st.metric("Total Incidents", len(inc["incident_ids"]))

elif option == "Analyse Incident Trends":
if not inc["incident_ids"]:
 st.info("No incidents available for analysis.")
else:
 low = inc["severities"].count("Low")
 medium = inc["severities"].count("Medium")
 high = inc["severities"].count("High")
 st.write("Low severity incidents:", low)
 st.write("Medium severity incidents:", medium)
 st.write("High severity incidents:", high)
if high >= medium and high >= low:
 st.warning("Most common severity: High")
elif medium >= high and medium >= low:
 st.info("Most common severity: Medium")
else:
 st.success("Most common severity: Low")

elif module == "Equipment database":
 st.header("Equipment Database")
 option = st.selectbox(
 "Select an option",
 ["Add Equipment", "View Equipment", "Search Equipment", "Filter Equipment", "Count Equipment", "Check Equipment Status"]
 )

if option == "Add Equipment":
 equipment_id = st.text_input("Equipment ID")
 equipment_type = st.selectbox("Equipment Type", ["Haul Truck", "Loader", "Excavator", "Drilling Machine", "Bulldozer", "Scraper Winch", "Crusher", "Conveyor"])
 manufacturer = st.text_input("Manufacturer")
 operating_hours = st.number_input("Operating Hours", min_value=0.0, step=1.0)
 temperature = st.number_input("Temperature", min_value=0.0, step=1.0)
 vibration = st.number_input("Vibration", min_value=0.0, step=0.1)
 fuel_consumption = st.number_input("Fuel Consumption", min_value=0.0, step=0.1)
 brake_status = st.selectbox("Brake Status", ["Good", "Faulty"])
 tyre_status = st.selectbox("Tyre Status", ["Good", "Worn"])
 engine_status = st.selectbox("Engine Status", ["Good", "Faulty"])
 maintenance_status = st.selectbox("Maintenance Status", ["Up to date", "Overdue"])
 downtime = st.number_input("Downtime Hours", min_value=0.0, step=1.0)
 availability = st.number_input("Availability Percentage", min_value=0.0, max_value=100.0, step=1.0)

if st.button("Save Equipment"):
 eq["equipment_ids"].append(equipment_id)
 eq["equipment_types"].append(equipment_type)
 eq["manufacturers"].append(manufacturer)
 eq["operating_hours"].append(operating_hours)
 eq["temperatures"].append(temperature)
 eq["vibrations"].append(vibration)
 eq["fuel_consumptions"].append(fuel_consumption)
 eq["brake_statuses"].append(brake_status)
 eq["tyre_statuses"].append(tyre_status)
 eq["engine_statuses"].append(engine_status)
 eq["maintenance_statuses"].append(maintenance_status)
 eq["downtimes"].append(downtime)
 eq["availabilities"].append(availability)
 st.success("Equipment successfully added.")

if brake_status.lower() == "faulty":
 st.warning("Brake fault detected.")
if tyre_status.lower() == "worn":
 st.warning("Tyres need attention.")
if engine_status.lower() == "faulty":
 st.warning("Engine fault detected.")
if maintenance_status.lower() == "overdue":
 st.warning("Maintenance is overdue.")

elif option == "View Equipment":
if not eq["equipment_ids"]:
 st.info("No equipment recorded.")
else:
for i in range(len(eq["equipment_ids"])):
 st.subheader(f"Equipment {i + 1}")
 st.write("Equipment ID:", eq["equipment_ids"][i])
 st.write("Equipment Type:", eq["equipment_types"][i])
 st.write("Manufacturer:", eq["manufacturers"][i])
 st.write("Operating Hours:", eq["operating_hours"][i])
 st.write("Temperature:", eq["temperatures"][i])
 st.write("Vibration:", eq["vibrations"][i])
 st.write("Fuel Consumption:", eq["fuel_consumptions"][i])
 st.write("Brake Status:", eq["brake_statuses"][i])
 st.write("Tyre Status:", eq["tyre_statuses"][i])
 st.write("Engine Status:", eq["engine_statuses"][i])
 st.write("Maintenance Status:", eq["maintenance_statuses"][i])
 st.write("Downtime:", eq["downtimes"][i])
 st.write("Availability:", f"{eq['availabilities'][i]}%")

elif option == "Search Equipment":
 search = st.text_input("Enter Equipment ID, Type or Manufacturer").lower()
if st.button("Search Equipment"):
 found = False
for i in range(len(eq["equipment_ids"])):
if (search in eq["equipment_ids"][i].lower() or
 search in eq["equipment_types"][i].lower() or
 search in eq["manufacturers"][i].lower()):
 st.subheader(f"Equipment {eq['equipment_ids'][i]}")
 st.write("Equipment Type:", eq["equipment_types"][i])
 st.write("Manufacturer:", eq["manufacturers"][i])
 st.write("Operating Hours:", eq["operating_hours"][i])
 st.write("Availability:", f"{eq['availabilities'][i]}%")
 found = True
if not found:
 st.warning("No matching equipment found.")

elif option == "Filter Equipment":
 filter_type = st.selectbox("Filter by", ["Equipment Type", "Manufacturer", "Brake Status", "Engine Status", "Maintenance Status"])
 value = st.text_input("Enter filter value").lower()
if st.button("Apply Filter"):
 found = False
for i in range(len(eq["equipment_ids"])):
if filter_type == "Equipment Type":
  match = eq["equipment_types"][i].lower() == value
elif filter_type == "Manufacturer":
 match = eq["manufacturers"][i].lower() == value
elif filter_type == "Brake Status":
 match = eq["brake_statuses"][i].lower() == value
elif filter_type == "Engine Status":
 match = eq["engine_statuses"][i].lower() == value
else:
 match = eq["maintenance_statuses"][i].lower() == value
if match:
 st.write(f"{eq['equipment_ids'][i]} - {eq['equipment_types'][i]} - {eq['availabilities'][i]}%")
 found = True
if not found:
 st.warning("No equipment matches the filter.")

elif option == "Count Equipment":
 st.metric("Total Equipment", len(eq["equipment_ids"]))

elif option == "Check Equipment Status":
if not eq["equipment_ids"]:
st.info("No equipment recorded.")
else:
for i in range(len(eq["equipment_ids"])):
st.subheader(f"Equipment ID: {eq['equipment_ids'][i]}")
if (eq["brake_statuses"][i].lower() == "faulty" or
eq["tyre_statuses"][i].lower() == "worn" or
eq["engine_statuses"][i].lower() == "faulty" or
eq["maintenance_statuses"][i].lower() == "overdue"):
st.warning("Status: ATTENTION REQUIRED")
else:
st.success("Status: Equipment is OK")

elif module == "Risk Assessment":
st.header("Mining Risk Assessment")
hazard = st.text_input("Enter Hazard")
likelihood = st.selectbox("Likelihood (1-5)", [1, 2, 3, 4, 5])
consequence = st.selectbox("Consequence (1-5)", [1, 2, 3, 4, 5])

if st.button("Assess Risk"):
risk_score = likelihood * consequence
st.subheader("Risk Assessment Results")
st.write("Hazard:", hazard)
st.write("Likelihood:", likelihood)
st.write("Consequence:", consequence)
st.metric("Risk Score", risk_score)

if risk_score <= 4:
classification = "Low"
elif risk_score <= 9:
classification = "Medium"
elif risk_score <= 16:
classification = "High"
else:
classification = "Critical"

st.write("Risk Classification:", classification)
if classification == "High":
st.warning("High risk identified. Action is required.")
elif classification == "Critical":
st.error("Critical risk identified. Immediate action is required.")
elif classification == "Medium":
st.info("Medium risk identified. Appropriate control measures are required.")
else:
st.success("Low risk identified. Continue monitoring the hazard.")

elif module == "Equipment Monitoring":
st.header("Equipment Condition Monitoring")
equipment_id = st.text_input("Enter Equipment ID")
temperature = st.number_input("Enter Temperature (°C)", min_value=0.0, step=1.0)
vibration = st.number_input("Enter Vibration (mm/s)", min_value=0.0, step=0.1)

if st.button("Monitor Equipment"):
st.subheader("Monitoring Results")
st.write("Equipment ID:", equipment_id)

if temperature < 80:
temperature_status = "NORMAL"
st.success("NORMAL: Equipment temperature is within monitoring limits.")
elif temperature <= 100:
temperature_status = "WARNING"
st.warning("WARNING: Equipment temperature is approaching the threshold.")
else:
temperature_status = "CRITICAL"
st.error("CRITICAL: Equipment temperature exceeds the threshold.")

if vibration < 5:
vibration_status = "NORMAL"
st.success("NORMAL: Equipment vibration is within monitoring limits.")
elif vibration <= 8:
vibration_status = "WARNING"
st.warning("WARNING: Equipment vibration is approaching the threshold.")
else:
vibration_status = "CRITICAL"
st.error("CRITICAL: Equipment vibration exceeds the threshold.")

st.subheader("Overall Equipment Status")
if temperature_status == "CRITICAL" or vibration_status == "CRITICAL":
st.error("Inspection required.")
elif temperature_status == "WARNING" or vibration_status == "WARNING":
st.warning("Monitoring required.")
else:
st.success("Equipment operating normally.")

elif module == "Maintenance":
st.title("Maintenance Management")
equipment_id = st.text_input("Enter Equipment ID", key="maintenance_equipment_id")
equipment_type = st.selectbox(
"Enter Equipment Type",
["Haul Truck", "Loader", "Excavator", "Drill", "Bulldozer", "Crusher", "Conveyor", "Other"],
key="maintenance_equipment_type"
)
operating_time = st.number_input("Operating Time (hours)", min_value=0.0, key="maintenance_operating_time")
downtime = st.number_input("Downtime (hours)", min_value=0.0, key="maintenance_downtime")
repeated_alerts = st.number_input("Number of Repeated Alerts", min_value=0, step=1, key="maintenance_repeated_alerts")
maintenance_status = st.selectbox(
"Maintenance Status",
["Normal", "Due", "Overdue", "Under Maintenance"],
key="maintenance_status"
)

if st.button("Check Maintenance Status"):
if not equipment_id.strip():
st.error("Please enter an Equipment ID.")
elif operating_time + downtime == 0:
st.error("Operating time and downtime cannot both be zero.")
else:
availability = (operating_time / (operating_time + downtime)) * 100
st.subheader("Maintenance Report")
st.write("Equipment ID:", equipment_id)
st.write("Equipment Type:", equipment_type)
st.write("Operating Time:", operating_time, "hours")
st.write("Downtime:", downtime, "hours")
st.write("Availability:", round(availability, 2), "%")

if maintenance_status == "Due":
st.warning("Equipment is due for maintenance.")
elif maintenance_status == "Overdue":
st.error("Equipment is overdue for maintenance.")
elif maintenance_status == "Under Maintenance":
st.info("Equipment is under maintenance.")
else:
st.success("Maintenance is up to date.")

if downtime > 20:
st.warning("Equipment has excessive downtime.")
if repeated_alerts >= 3:
st.warning("Equipment has repeated alerts.")
if availability < 80:
st.warning("Equipment has low availability.")

if (maintenance_status == "Normal" and downtime <= 20 and repeated_alerts < 3 and availability >= 80):
st.success("Equipment is operating normally.")

if not st.session_state.logged_in:
if st.session_state.page == "Navigation":
navigation_page()
elif st.session_state.page == "Sign Up":
signup_page()
elif st.session_state.page == "Login":
login_page()
else:
home_page()
