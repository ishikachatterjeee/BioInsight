import streamlit as st
import pandas as pd
import plotly.express as px
import networkx as nx
import matplotlib.pyplot as plt

# ==========================
# LOAD DATA
# ==========================

equipment = pd.read_csv("equipment.csv")
maintenance = pd.read_csv("maintenance_logs.csv")

# ==========================
# RISK SCORE
# ==========================

equipment["Risk_Score"] = (
    (100 - equipment["Health_Score"])
    + equipment["Failure_Count"] * 5
)

# ==========================
# DEVICE CONDITION
# ==========================

def classify_device(score):

    if score >= 85:
        return "Healthy"

    elif score >= 70:
        return "Monitor"

    else:
        return "Critical"


equipment["Condition"] = equipment["Health_Score"].apply(
    classify_device
)

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="BioInsight",
    layout="wide"
)

# ==========================
# HEADER
# ==========================

st.title("🏥 BioInsight")
st.subheader("Clinical Engineering Dashboard")

# ==========================
# KPI CARDS
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Devices",
        len(equipment)
    )

with col2:
    st.metric(
        "Average Health Score",
        round(equipment["Health_Score"].mean(), 1)
    )

with col3:
    st.metric(
        "Devices in Maintenance",
        len(
            equipment[
                equipment["Status"] == "Maintenance"
            ]
        )
    )

with col4:
    st.metric(
        "Total Maintenance Records",
        len(maintenance)
    )

# ==========================
# DEPARTMENT DISTRIBUTION
# ==========================

st.divider()

st.subheader("🏢 Department-wise Equipment Distribution")

dept_counts = equipment["Department"].value_counts()

st.bar_chart(dept_counts)

# ==========================
# LOW HEALTH DEVICES
# ==========================

st.divider()

st.subheader("⚠ Devices Needing Attention")

low_health = equipment.sort_values(
    by="Health_Score"
).head(5)

st.dataframe(low_health)

# ==========================
# HIGH RISK DEVICES
# ==========================

st.divider()

st.subheader("🚨 High Risk Devices")

high_risk = equipment.sort_values(
    by="Risk_Score",
    ascending=False
).head(10)

st.dataframe(high_risk)

# ==========================
# CALIBRATION ALERTS
# ==========================

st.divider()

st.subheader("📅 Calibration Due Soon")

due_devices = equipment[
    equipment["Calibration_Due_Days"] < 30
]

st.dataframe(due_devices)

# ==========================
# CONDITION OVERVIEW
# ==========================

st.divider()

st.subheader("❤️ Equipment Condition Overview")

condition_counts = equipment["Condition"].value_counts()

st.bar_chart(condition_counts)

# ==========================
# EXECUTIVE ALERTS
# ==========================

st.divider()

st.subheader("🚑 Executive Alerts")

critical_devices = equipment[
    equipment["Condition"] == "Critical"
]

st.error(
    f"{len(critical_devices)} critical devices require immediate attention."
)

st.warning(
    f"{len(due_devices)} devices require calibration within 30 days."
)

# ==========================
# FAILURE ANALYTICS
# ==========================

st.divider()

st.subheader("🔧 Most Common Failures")

failure_counts = maintenance["Fault"].value_counts()

st.bar_chart(failure_counts)

# ==========================
# DOWNTIME ANALYTICS
# ==========================

st.divider()

st.subheader("⏱ Downtime by Fault")

downtime = maintenance.groupby(
    "Fault"
)["Downtime_Hours"].sum()

st.bar_chart(downtime)

# ==========================
# SEARCH EQUIPMENT
# ==========================

st.divider()

st.subheader("🔍 Search Equipment")

search_id = st.text_input(
    "Enter Equipment ID (Example: EQ001)"
)

if search_id:

    result = equipment[
        equipment["Equipment_ID"].str.contains(
            search_id,
            case=False,
            na=False
        )
    ]

    if len(result) > 0:
        st.dataframe(result)

    else:
        st.info("No equipment found.")

# ==========================
# MAINTENANCE RECORDS
# ==========================

st.divider()

st.subheader("📋 Recent Maintenance Records")

st.dataframe(
    maintenance.head(20)
)

# ==========================
# EQUIPMENT INVENTORY
# ==========================

st.divider()

st.subheader("🩺 Equipment Inventory")

st.dataframe(equipment)

# ==========================
# TROUBLESHOOTING ASSISTANT
# ==========================

st.divider()

st.subheader("🧠 Biomedical Troubleshooting Assistant")

knowledge_base = {

    "Low Pressure Alarm": {
        "cause": "Circuit Leak",
        "action": "Inspect tubing and replace damaged tubing"
    },

    "Battery Failure": {
        "cause": "Battery Degradation",
        "action": "Replace Battery"
    },

    "Sensor Failure": {
        "cause": "Sensor Malfunction",
        "action": "Replace or Recalibrate Sensor"
    },

    "Flow Error": {
        "cause": "Occlusion in Tubing",
        "action": "Inspect and Clear Blockage"
    },

    "Calibration Drift": {
        "cause": "Calibration Expired",
        "action": "Perform Calibration"
    },

    "Power Supply Failure": {
        "cause": "Faulty Power Unit",
        "action": "Replace Power Supply"
    },

    "Communication Error": {
        "cause": "Network or Interface Failure",
        "action": "Check Connections and Restart System"
    }
}

selected_fault = st.selectbox(
    "Select a Fault",
    list(knowledge_base.keys())
)

st.success(
    f"Possible Cause: {knowledge_base[selected_fault]['cause']}"
)

st.info(
    f"Recommended Action: {knowledge_base[selected_fault]['action']}"
)
# ==========================
# BIOMEDICAL KNOWLEDGE GRAPH
# ==========================

st.divider()

st.subheader("🕸 Biomedical Failure Knowledge Graph")

graph_data = {

    "Low Pressure Alarm": {
        "equipment": "Ventilator",
        "cause": "Circuit Leak",
        "action": "Replace Tubing"
    },

    "Battery Failure": {
        "equipment": "Patient Monitor",
        "cause": "Battery Degradation",
        "action": "Replace Battery"
    },

    "Sensor Failure": {
        "equipment": "Patient Monitor",
        "cause": "Sensor Malfunction",
        "action": "Replace Sensor"
    },

    "Flow Error": {
        "equipment": "Infusion Pump",
        "cause": "Tubing Occlusion",
        "action": "Clear Blockage"
    },

    "Communication Error": {
        "equipment": "ECG Machine",
        "cause": "Network Failure",
        "action": "Restart System"
    }
}

selected_graph_fault = st.selectbox(
    "Select Fault for Graph",
    list(graph_data.keys())
)

equipment_name = graph_data[selected_graph_fault]["equipment"]
cause = graph_data[selected_graph_fault]["cause"]
action = graph_data[selected_graph_fault]["action"]

G = nx.DiGraph()

G.add_edge(equipment_name, selected_graph_fault)
G.add_edge(selected_graph_fault, cause)
G.add_edge(cause, action)

fig, ax = plt.subplots(figsize=(8, 5))

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3500,
    font_size=9,
    ax=ax
)

st.pyplot(fig)
# ==========================
# FOOTER
# ==========================

st.divider()

st.caption(
    "BioInsight v1.0 | Clinical Engineering Dashboard & Biomedical Equipment Failure Knowledge Graph"
)