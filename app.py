
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import os
import gdown # <-- make sure gdown is in requirements.txt

# ==========================
# Load trained model, scaler, encoder
# ==========================

# Large model (download from Google Drive if missing)
model_path = "best_model_RandomForest.pkl"
file_id = "1TxBM8F164ohAS5He1Lglk5ea-0pmND0L"  # Google Drive File ID
url = f"https://drive.google.com/uc?id={file_id}"

# Download only if not present
if not os.path.exists(model_path):
    st.info("Downloading large model from Google Drive... ⏳")
    gdown.download(url, model_path, quiet=False)

# Load models
model = joblib.load(model_path)  
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("crop_label_encoder.pkl")


st.title("💧 AI-Driven Smart Crop Water Allocation System using Predictive Analytics")

# ==========================
# User inputs
# ==========================
crop = st.selectbox("Select Crop", label_encoder.classes_)
year = st.slider("Enter Year", min_value=2000, max_value=2100, value=2025, step=1)
rainfall = st.slider("Enter Rainfall (mm)", min_value=0.0, max_value=5000.0, value=1000.0, step=10.0)
moisture = st.slider("Enter Soil Moisture (%)", min_value=0.0, max_value=100.0, value=30.0, step=1.0)
area = st.slider("Enter Area (hectares)", min_value=0.0, max_value=1000.0, value=100.0, step=1.0)
production = st.slider("Enter Production (tons)", min_value=0.0, max_value=1000.0, value=50.0, step=1.0)

# ==========================
# Prediction
# ==========================
if st.button("Predict Water Allocation"):
    # Encode crop
    crop_encoded = label_encoder.transform([crop])[0]

    # Prepare features
    features = np.array([[crop_encoded, year, rainfall, moisture, area, production]])
    features_scaled = scaler.transform(features)

    # Predict
    prediction = model.predict(features_scaled)[0]

    # Show result
    st.success(f"💧 Water Allocated: {prediction:.2f}%")

    if prediction > 70:
        st.success("High Water Needed 🚰")
    elif 30 <= prediction <= 70:
        st.warning("Moderate Water Needed 💧")
    else:
        st.info("Low Water Needed ✅")

    # --- Plotly Bar Chart ---
    st.subheader("📊 Water Allocation for Selected Crop")
    fig_bar = px.bar(
        x=[crop],
        y=[prediction],   # <-- use model output
        text=[f"{prediction:.1f}%"],
        labels={"x": "Crop", "y": "Water Allocation (%)"},
        title="Water Allocation Prediction",
        color_discrete_sequence=["lightblue"]
    )
    fig_bar.update_traces(textposition="outside")
    fig_bar.update_yaxes(range=[0, 100])
    st.plotly_chart(fig_bar)

    # --- Plotly Trend Line Chart ---
    st.subheader("📈 Water Allocation Trend with Rainfall")

    # Create a smooth rainfall range
    rainfall_range = np.linspace(0, 200, 50)

    # Recompute predictions by changing rainfall, keeping other inputs fixed
    allocations = []
    for r in rainfall_range:
        features = np.array([[crop_encoded, year, r, moisture, area, production]])
        features_scaled = scaler.transform(features)
        alloc = model.predict(features_scaled)[0]
        allocations.append(alloc)

    fig_line = px.line(
        x=rainfall_range,
        y=allocations,
        labels={"x": "Rainfall (mm)", "y": "Water Allocation (%)"},
        title=f"Trend of Water Allocation vs Rainfall ({crop})"
    )

    # Add marker for user input
    fig_line.add_scatter(
        x=[rainfall], y=[prediction],
        mode="markers+text",
        text=["Your Input"],
        textposition="top center",
        marker=dict(size=12, color="blue")
    )
    fig_line.update_yaxes(range=[0, 100])
    st.plotly_chart(fig_line)
