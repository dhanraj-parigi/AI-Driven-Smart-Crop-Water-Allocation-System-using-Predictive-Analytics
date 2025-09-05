import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle

# =====================
# Load Trained Model
# =====================
with open("excellent_water_allocation_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💧 AI-Driven Smart Crop Water Allocation System using Predictive Analytics")

# =====================
# User Inputs
# =====================
crop = st.selectbox("Select Crop", ["Paddy", "Wheat", "Maize", "Sugarcane"])
year = st.slider("Enter Year", min_value=2000, max_value=2100, value=2025, step=1)
rainfall = st.slider("Enter Rainfall (mm)", min_value=0.0, max_value=500.0, value=23.0, step=0.1)
moisture = st.slider("Enter Soil Moisture (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)

# =====================
# Prediction Function
# =====================
def predict_water_allocation(crop, year, rainfall, moisture):
    try:
        # Model expects rainfall as feature
        prediction = model.predict([[rainfall]])[0]

        # Simple adjustment using soil moisture
        allocation = prediction - (moisture * 0.1)

        # Clip values between 0–100
        allocation = max(0, min(100, allocation))
        return allocation
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        return None

# =====================
# Run Prediction
# =====================
if st.button("Predict Water Allocation"):
    result = predict_water_allocation(crop, year, rainfall, moisture)

    if result is not None:
        st.success(f"💧 Water Allocated: {result:.2f}%")

        # Add status message
        if result > 70:
            st.success("High Water Needed 🚰")
        elif 30 <= result <= 70:
            st.warning("Moderate Water Needed 💧")
        else:
            st.info("No Water Needed ✅")

        # --- Bar Chart ---
        st.subheader("📊 Water Allocation for Selected Crop")
        fig1, ax1 = plt.subplots()
        bars = ax1.bar([crop], [result], color="skyblue")
        ax1.set_ylim(0, 100)
        ax1.set_ylabel("Water Allocation (%)")
        ax1.set_title("Water Allocation Prediction")

        # Add value label
        for bar in bars:
            yval = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2, yval + 2, f"{yval:.1f}%", ha='center', va='bottom')

        st.pyplot(fig1)

        # --- Trend Line Chart ---
        st.subheader("📈 Water Allocation Trend with Rainfall")
        rainfall_range = np.linspace(0, 200, 50)
        allocations = [predict_water_allocation(crop, year, r, moisture) for r in rainfall_range]

        fig2, ax2 = plt.subplots()
        ax2.plot(rainfall_range, allocations, color="skyblue", linewidth=2)
        ax2.scatter([rainfall], [result], color="blue", s=80, label="Your Input")
        ax2.set_ylim(0, 100)
        ax2.set_xlabel("Rainfall (mm)")
        ax2.set_ylabel("Water Allocation (%)")
        ax2.set_title(f"Trend of Water Allocation vs Rainfall ({crop})")
        ax2.legend()

        st.pyplot(fig2)
