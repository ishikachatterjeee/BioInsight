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

alarm = input("Enter Fault: ")

if alarm in knowledge_base:

    print("\nPossible Cause:")
    print(knowledge_base[alarm]["cause"])

    print("\nRecommended Action:")
    print(knowledge_base[alarm]["action"])

else:
    print("Fault not found in knowledge base")