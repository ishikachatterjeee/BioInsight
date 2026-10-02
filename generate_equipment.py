import pandas as pd
import random

equipment_types = [
    ("Ventilator", "ICU"),
    ("Patient Monitor", "ICU"),
    ("Infusion Pump", "ICU"),
    ("Syringe Pump", "ICU"),
    ("Defibrillator", "Emergency"),
    ("ECG Machine", "Cardiology"),
    ("Holter Monitor", "Cardiology"),
    ("Stress Test System", "Cardiology"),
    ("Ultrasound Machine", "Radiology"),
    ("X-Ray Machine", "Radiology"),
    ("CT Scanner", "Radiology"),
    ("MRI Scanner", "Radiology"),
    ("Incubator", "NICU"),
    ("Phototherapy Unit", "NICU"),
    ("Anesthesia Workstation", "OT"),
    ("Electrosurgical Unit", "OT"),
    ("Centrifuge", "Laboratory"),
    ("Hematology Analyzer", "Laboratory"),
    ("Biochemistry Analyzer", "Laboratory"),
    ("Blood Gas Analyzer", "Laboratory")
]

manufacturers = [
    "Philips",
    "GE Healthcare",
    "Siemens Healthineers",
    "Drager",
    "Mindray",
    "B Braun",
    "Zoll",
    "Fresenius"
]

status_options = [
    "Active",
    "Active",
    "Active",
    "Maintenance",
    "Calibration Due"
]

equipment_data = []

for i in range(1, 51):

    equipment, department = random.choice(equipment_types)

    equipment_data.append({
        "Equipment_ID": f"EQ{i:03}",
        "Equipment_Name": equipment,
        "Department": department,
        "Manufacturer": random.choice(manufacturers),
        "Purchase_Year": random.randint(2018, 2025),
        "Status": random.choice(status_options),
        "Health_Score": random.randint(60, 100),
        "Failure_Count": random.randint(0, 8),
        "Utilization_Hours": random.randint(500, 12000),
        "Calibration_Due_Days": random.randint(0, 180)
    })

df = pd.DataFrame(equipment_data)

df.to_csv("equipment.csv", index=False)

print("Equipment database created successfully!")
print(df.head())