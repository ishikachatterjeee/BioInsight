import pandas as pd
import random

faults = [
    "Low Pressure Alarm",
    "Battery Failure",
    "Sensor Failure",
    "Flow Error",
    "Calibration Drift",
    "Power Supply Failure",
    "Display Error",
    "Communication Error"
]

actions = [
    "Replaced Battery",
    "Replaced Tubing",
    "Calibration Performed",
    "Sensor Replaced",
    "Software Updated",
    "Power Unit Repaired",
    "System Restarted"
]

logs = []

for i in range(1, 201):

    logs.append({
        "Log_ID": f"M{i:03}",
        "Equipment_ID": f"EQ{random.randint(1,50):03}",
        "Fault": random.choice(faults),
        "Action": random.choice(actions),
        "Downtime_Hours": random.randint(1,12)
    })

df = pd.DataFrame(logs)

df.to_csv("maintenance_logs.csv", index=False)

print("Maintenance logs created!")
print(df.head())