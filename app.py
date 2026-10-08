import streamlit as st

st.set_page_config(
    page_title="Mining Monitoring System",
    page_icon="⛏️",
    layout="wide"
)

incident_ids = []
dates = []
times = []
shifts = []
locations = []
departments = []
incident_types = []
severities = []
injury_statuses = []
lost_time_injuries = []
causes = []
corrective_actions = []
incident_statuses = []

st.title("⛏️ Mining Monitoring System")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("LOGIN"):
    if username == "administrator123" and password == "administrator987":
        st.session_state.logged_in = True
        st.session_state.role = "Administrator"
    elif username == "safety123" and password == "safety987":
        st.session_state.logged_in = True
        st.session_state.role = "Safety Officer"
    elif username == "mining123" and password == "mining987":
        st.session_state.logged_in = True
        st.session_state.role = "Mining Engineer"
    elif username == "maintenance123" and password == "maintenance987":
        st.session_state.logged_in = True
        st.session_state.role = "Maintenance Engineer"
    elif username == "manager123" and password == "manager987":
        st.session_state.logged_in = True
        st.session_state.role = "Manager"
    else:
        st.error("Invalid username or password")

if st.session_state.get("logged_in", False):

    st.success("Login successful")
    st.write("Role:", st.session_state.role)

    module = st.selectbox(
        "Select Module",
        [
            "Dashboard",
            "Worker Safety",
            "Safety Incidents",
            "Equipment",
            "Equipment Monitoring",
            "Maintenance",
            "Risk Assessment",
            "Alerts"
        ]
    )

    if module == "Worker Safety":

        st.header("Worker Health and Safety Monitoring")

        worker_id = st.text_input("Worker ID")
        department = st.text_input("Department")
        job_role = st.text_input("Job Role")
        shift = st.selectbox("Shift", ["Day", "Night"])
        ppe = st.selectbox(
            "Is PPE compliance satisfactory?",
            ["Yes", "No"]
        )
        training = st.selectbox(
            "Is safety training up to date?",
            ["Yes", "No"]
        )
        fatigue = st.selectbox(
            "Enter fatigue level",
            ["Low", "Medium", "High"]
        )
        observations = st.text_area("Enter Safety Observations")
        near_misses = st.number_input(
            "Enter Number of Near Misses",
            min_value=0,
            step=1
        )
        previous_incidents = st.number_input(
            "Enter Number of Previous Incidents",
            min_value=0,
            step=1
        )
        risk_level = st.selectbox(
            "Enter Risk Level",
            ["Low", "Medium", "High"]
        )

        if st.button("Assess Worker Safety"):

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
                warnings.append(
                    "PPE compliance is unsatisfactory."
                )

            if training.lower() == "no":
                warnings.append(
                    "Safety training is not up to date."
                )

            if fatigue.lower() == "high":
                warnings.append(
                    "Worker has a high fatigue level."
                )

            if near_misses > 0:
                warnings.append(
                    "Worker has recorded near misses."
                )

            if previous_incidents > 0:
                warnings.append(
                    "Worker has previous safety incidents."
                )

            if risk_level.lower() == "high":
                warnings.append(
                    "Worker has a HIGH risk level."
                )

            st.subheader("Safety Assessment")

            if len(warnings) > 0:

                st.warning(
                    "Potentially unsafe conditions detected."
                )

                for warning in warnings:
                    st.write("⚠️", warning)

            else:

                st.success(
                    "No major unsafe conditions detected."
                )

                st.success(
                    "Worker is currently considered safe."
                )

            st.info(
                "Worker safety monitoring complete."
            )

    if module == "Safety Incidents":

        st.header("Safety Incident Database")

        option = st.selectbox(
            "Select an option",
            [
                "Add Incident",
                "View Incidents",
                "Search Incidents",
                "Filter Incidents",
                "Categorise Incidents",
                "Count Incidents",
                "Analyse Incident Trends"
            ]
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
            lost_time_injury = st.selectbox(
                "Was it a lost-time injury?", ["Yes", "No"]
            )
            cause = st.text_input("Cause")
            corrective_action = st.text_input("Corrective Action")
            incident_status = st.selectbox(
                "Incident Status", ["Open", "Closed"]
            )

            if st.button("Save Incident"):

                incident_ids.append(incident_id)
                dates.append(str(date))
                times.append(str(time))
                shifts.append(shift)
                locations.append(location)
                departments.append(department)
                incident_types.append(incident_type)
                severities.append(severity)
                injury_statuses.append(injury_status)
                lost_time_injuries.append(lost_time_injury)
                causes.append(cause)
                corrective_actions.append(corrective_action)
                incident_statuses.append(incident_status)

                st.success("Incident successfully added!")

        elif option == "View Incidents":

            if len(incident_ids) == 0:
                st.info("No incidents recorded.")
            else:
                for i in range(len(incident_ids)):
                    st.subheader("Incident " + str(i + 1))

                    st.write("Incident ID:", incident_ids[i])
                    st.write("Date:", dates[i])
                    st.write("Time:", times[i])
                    st.write("Shift:", shifts[i])
                    st.write("Location:", locations[i])
                    st.write("Department:", departments[i])
                    st.write("Incident Type:", incident_types[i])
                    st.write("Severity:", severities[i])
                    st.write("Injury Status:", injury_statuses[i])
                    st.write("Lost-Time Injury:", lost_time_injuries[i])
                    st.write("Cause:", causes[i])
                    st.write("Corrective Action:", corrective_actions[i])
                    st.write("Incident Status:", incident_statuses[i])

        elif option == "Search Incidents":

            search = st.text_input(
                "Enter Incident ID, Location or Department"
            ).lower()

            if st.button("Search"):

                found = False

                for i in range(len(incident_ids)):

                    if (
                        search in incident_ids[i].lower()
                        or search in locations[i].lower()
                        or search in departments[i].lower()
                    ):
                        st.write("Incident ID:", incident_ids[i])
                        st.write("Date:", dates[i])
                        st.write("Location:", locations[i])
                        st.write("Department:", departments[i])
                        st.write("Incident Type:", incident_types[i])
                        st.write("Severity:", severities[i])

                        found = True

                if found == False:
                    st.warning("No matching incidents found.")

        elif option == "Filter Incidents":

            filter_type = st.selectbox(
                "Filter by",
                ["Severity", "Department", "Shift", "Incident Type"]
            )

            value = st.text_input("Enter value").lower()

            if st.button("Apply Filter"):

                for i in range(len(incident_ids)):

                    if filter_type == "Severity":
                        match = severities[i].lower() == value
                    elif filter_type == "Department":
                        match = departments[i].lower() == value
                    elif filter_type == "Shift":
                        match = shifts[i].lower() == value
                    else:
                        match = incident_types[i].lower() == value

                    if match:
                        st.write(
                            incident_ids[i],
                            "-",
                            incident_types[i],
                            "-",
                            severities[i]
                        )

        elif option == "Categorise Incidents":

            categories = []

            for incident in incident_types:

                if incident not in categories:
                    categories.append(incident)

            if len(categories) == 0:
                st.info("No incidents recorded.")
            else:
                for category in categories:

                    count = incident_types.count(category)

                    st.write(
                        category,
                        ":",
                        count,
                        "incident(s)"
                    )

        elif option == "Count Incidents":

            st.metric(
                "Total Incidents",
                len(incident_ids)
            )

        elif option == "Analyse Incident Trends":

            if len(incident_ids) == 0:
                st.info("No incidents available for analysis.")
            else:

                low = severities.count("Low")
                medium = severities.count("Medium")
                high = severities.count("High")

                st.write("Low severity incidents:", low)
                st.write("Medium severity incidents:", medium)
                st.write("High severity incidents:", high)

                if high >= medium and high >= low:
                    st.warning("Most common severity: High")
                elif medium >= high and medium >= low:
                    st.info("Most common severity: Medium")
                else:
                    st.success("Most common severity: Low")

    if module == "Equipment":

        st.header("Equipment Database")

        option = st.selectbox(
            "Select an option",
            [
                "Add Equipment",
                "View Equipment",
                "Search Equipment",
                "Filter Equipment",
                "Count Equipment",
                "Check Equipment Status"
            ]
        )

        if option == "Add Equipment":

            equipment_id = st.text_input("Equipment ID")
            equipment_type = st.selectbox(
                "Equipment Type",
                [
                    "Haul Truck",
                    "Loader",
                    "Excavator",
                    "Drilling Machine",
                    "Bulldozer",
                    "Scraper Winch",
                    "Crusher",
                    "Conveyor"
                ]
            )
            manufacturer = st.text_input("Manufacturer")
            operating_hours = st.number_input(
                "Operating Hours",
                min_value=0.0,
                step=1.0
            )
            temperature = st.number_input(
                "Temperature",
                min_value=0.0,
                step=1.0
            )
            vibration = st.number_input(
                "Vibration",
                min_value=0.0,
                step=0.1
            )
            fuel_consumption = st.number_input(
                "Fuel Consumption",
                min_value=0.0,
                step=0.1
            )
            brake_status = st.selectbox(
                "Brake Status",
                ["Good", "Faulty"]
            )
            tyre_status = st.selectbox(
                "Tyre Status",
                ["Good", "Worn"]
            )
            engine_status = st.selectbox(
                "Engine Status",
                ["Good", "Faulty"]
            )
            maintenance_status = st.selectbox(
                "Maintenance Status",
                ["Up to date", "Overdue"]
            )
            downtime = st.number_input(
                "Downtime Hours",
                min_value=0.0,
                step=1.0
            )
            availability = st.number_input(
                "Availability Percentage",
                min_value=0.0,
                max_value=100.0,
                step=1.0
            )

            if st.button("Save Equipment"):

                equipment_ids.append(equipment_id)
                equipment_types.append(equipment_type)
                manufacturers.append(manufacturer)
                operating_hours.append(operating_hours)
                temperatures.append(temperature)
                vibrations.append(vibration)
                fuel_consumptions.append(fuel_consumption)
                brake_statuses.append(brake_status)
                tyre_statuses.append(tyre_status)
                engine_statuses.append(engine_status)
                maintenance_statuses.append(maintenance_status)
                downtimes.append(downtime)
                availabilities.append(availability)

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

            if len(equipment_ids) == 0:
                st.info("No equipment recorded.")
            else:

                for i in range(len(equipment_ids)):

                    st.subheader(
                        "Equipment " + str(i + 1)
                    )

                    st.write(
                        "Equipment ID:",
                        equipment_ids[i]
                    )
                    st.write(
                        "Equipment Type:",
                        equipment_types[i]
                    )
                    st.write(
                        "Manufacturer:",
                        manufacturers[i]
                    )
                    st.write(
                        "Operating Hours:",
                        operating_hours[i]
                    )
                    st.write(
                        "Temperature:",
                        temperatures[i]
                    )
                    st.write(
                        "Vibration:",
                        vibrations[i]
                    )
                    st.write(
                        "Fuel Consumption:",
                        fuel_consumptions[i]
                    )
                    st.write(
                        "Brake Status:",
                        brake_statuses[i]
                    )
                    st.write(
                        "Tyre Status:",
                        tyre_statuses[i]
                    )
                    st.write(
                        "Engine Status:",
                        engine_statuses[i]
                    )
                    st.write(
                        "Maintenance Status:",
                        maintenance_statuses[i]
                    )
                    st.write(
                        "Downtime:",
                        downtimes[i]
                    )
                    st.write(
                        "Availability:",
                        availabilities[i],
                        "%"
                    )

        elif option == "Search Equipment":

            search = st.text_input(
                "Enter Equipment ID, Type or Manufacturer"
            ).lower()

            if st.button("Search Equipment"):

                found = False

                for i in range(len(equipment_ids)):

                    if (
                        search in equipment_ids[i].lower()
                        or search in equipment_types[i].lower()
                        or search in manufacturers[i].lower()
                    ):

                        st.subheader(
                            "Equipment " + equipment_ids[i]
                        )

                        st.write(
                            "Equipment Type:",
                            equipment_types[i]
                        )
                        st.write(
                            "Manufacturer:",
                            manufacturers[i]
                        )
                        st.write(
                            "Operating Hours:",
                            operating_hours[i]
                        )
                        st.write(
                            "Availability:",
                            availabilities[i],
                            "%"
                        )

                        found = True

                if found == False:
                    st.warning(
                        "No matching equipment found."
                    )

        elif option == "Filter Equipment":

            filter_type = st.selectbox(
                "Filter by",
                [
                    "Equipment Type",
                    "Manufacturer",
                    "Brake Status",
                    "Engine Status",
                    "Maintenance Status"
                ]
            )

            value = st.text_input(
                "Enter filter value"
            ).lower()

            if st.button("Apply Filter"):

                found = False

                for i in range(len(equipment_ids)):

                    if filter_type == "Equipment Type":
                        match = (
                            equipment_types[i].lower()
                            == value
                        )

                    elif filter_type == "Manufacturer":
                        match = (
                            manufacturers[i].lower()
                            == value
                        )

                    elif filter_type == "Brake Status":
                        match = (
                            brake_statuses[i].lower()
                            == value
                        )

                    elif filter_type == "Engine Status":
                        match = (
                            engine_statuses[i].lower()
                            == value
                        )

                    else:
                        match = (
                            maintenance_statuses[i].lower()
                            == value
                        )

                    if match:

                        st.write(
                            equipment_ids[i],
                            "-",
                            equipment_types[i],
                            "-",
                            availabilities[i],
                            "%"
                        )

                        found = True

                if found == False:
                    st.warning(
                        "No equipment matches the filter."
                    )

        elif option == "Count Equipment":

            st.metric(
                "Total Equipment",
                len(equipment_ids)
            )

        elif option == "Check Equipment Status":

            if len(equipment_ids) == 0:

                st.info("No equipment recorded.")

            else:

                for i in range(len(equipment_ids)):

                    st.subheader(
                        "Equipment ID: "
                        + equipment_ids[i]
                    )

                    if (
                        brake_statuses[i].lower() == "faulty"
                        or tyre_statuses[i].lower() == "worn"
                        or engine_statuses[i].lower() == "faulty"
                        or maintenance_statuses[i].lower() == "overdue"
                    ):

                        st.warning(
                            "Status: ATTENTION REQUIRED"
                        )

                    else:

                        st.success(
                            "Status: Equipment is OK"
                        )
