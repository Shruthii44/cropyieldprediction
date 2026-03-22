import streamlit as st
import pandas as pd
import joblib

# Load files
preprocessor = joblib.load("preprocessor (3).pkl")
model = joblib.load("model (2).pkl")

st.title("🌱 Crop Yield Prediction App")

st.write("Enter details to predict crop yield")

# -------- INPUT FIELDS -------- #

rainfall = st.number_input("Rainfall (mm)")
temperature = st.number_input("Temperature (°C)")
days = st.number_input("Days to Harvest")

region = st.selectbox("Region", ["East", "West", "North", "South"])
soil = st.selectbox("Soil Type", ["Clay", "Sandy", "Loam", "Peaty", "Silt", "Chalky"])
crop = st.selectbox("Crop", ["Rice", "Wheat", "Maize", "Barley", "Soybean", "Cotton"])
weather = st.selectbox("Weather Condition", ["Sunny", "Rainy", "Cloudy"])

fertilizer = st.selectbox("Fertilizer Used", ["Yes", "No"])
irrigation = st.selectbox("Irrigation Used", ["Yes", "No"])

# Convert Yes/No → 1/0
fertilizer = 1 if fertilizer == "Yes" else 0
irrigation = 1 if irrigation == "Yes" else 0

# -------- PREDICTION -------- #

if st.button("Predict Yield"):

    input_data = pd.DataFrame({
        'Rainfall_mm': [rainfall],
        'Temperature_Celsius': [temperature],
        'Days_to_Harvest': [days],
        'Region': [region],
        'Soil_Type': [soil],
        'Crop': [crop],
        'Weather_Condition': [weather],
        'Fertilizer_Used': [fertilizer],
        'Irrigation_Used': [irrigation]
    })

    # Apply preprocessing
    input_transformed = preprocessor.transform(input_data)

    # Predict
    prediction = model.predict(input_transformed)

    st.success(f"🌾 Predicted Yield: {prediction[0]:.2f} tons/hectare")