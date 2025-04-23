# main.py
import streamlit as st
from data_processing import FloodDataProcessor
from Risk_Prediction import FloodPredictor
from Alert_System import MultilingualAlertSystem
from Monitoring_Dashboard import MonitoringDashboard

# Initialize components
data_processor = FloodDataProcessor()
historical_data = data_processor.get_real_time_data()
predictor = FloodPredictor(data_path="flood_training_data.csv")
alert_system = MultilingualAlertSystem()
dashboard = MonitoringDashboard()

# Streamlit UI
st.title("Mumbai Flood Alert System")

# 1. Risk Prediction Section
st.header("Risk Assessment")
area_data = st.number_input("Enter rainfall (mm):", 0.0, 100.0, 50.0)
if st.button("Predict Flood Risk"):
   # Create a dictionary with the required keys
    real_time_data = {
        'rainfall': area_data,
        'water_level': 1.5,  # Example value
        'tide_level': 'high'  # Example value, adjust as needed
    }
    prediction = predictor.predict_risk(real_time_data)
    st.write(f"Predicted Risk Level: **{prediction.upper()}**")
# 2. Alert Generation Section
st.header("Alert Management")
language = st.selectbox("Select Language", ["en", "mr", "hi"])
if st.button("Generate Alert"):
    alert = alert_system.generate_alert("Dharavi", "high", language)
    st.code(alert)


# 3. Monitoring Dashboard
st.header("System Monitoring")
dashboard.show_summary(["Sample Alert 1", "Sample Alert 2"])