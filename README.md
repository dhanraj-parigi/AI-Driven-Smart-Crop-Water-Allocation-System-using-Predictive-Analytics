💧 AI-Driven Smart Crop Water Allocation System using Predictive Analytics

🌾 Agriculture consumes a significant portion of freshwater resources. Efficient water allocation is essential to ensure sustainable farming and meet the needs of agriculture, domestic, and industrial sectors.

This project uses Machine Learning & Predictive Analytics to recommend smart water allocation for crops based on rainfall, soil moisture, and crop type.

🚀 Features

📊 Data Preprocessing & EDA – Cleaned and analyzed crop yield & rainfall datasets.

🤖 Machine Learning Models – Trained Linear Regression, Random Forest, Gradient Boosting & HistGradientBoosting.

🏆 Best Model Selection – Saved the top-performing model as best_water_allocation_model.pkl.

🌐 Streamlit Web App – Interactive interface for farmers & decision-makers.

🔮 Predictions – Input crop type, year, rainfall, and soil moisture → get water allocation % and recommendations.

📈 Visualizations – Trend graphs & bar charts to make results easy to understand.

🛠️ Tech Stack

Languages & Tools: Python, Pandas, NumPy, Matplotlib, Seaborn

ML Frameworks: Scikit-learn

Frontend: Streamlit

Deployment Ready: Saved models in .pkl for real-time predictions

📂 Project Workflow

Dataset Preparation

Crop Yield Dataset

Rainfall Dataset

Preprocessing & Feature Engineering

Cleaned columns, merged datasets, handled NaN values

Model Training & Evaluation

Trained multiple ML models

Evaluated using R² Score & MSE

Best Model Saved

best_water_allocation_model.pkl used in Streamlit app

Streamlit App

User enters crop type, rainfall, soil moisture, year

App predicts water allocation %

Displays recommendation + graphs

🎯 Example Prediction

Input:

Crop: Paddy

Year: 2025

Rainfall: 23 mm

Soil Moisture: 5%

Output:

💧 Water Allocated: 72.5%

🚰 Status: High Water Needed

📊 Bar & Line Chart for visualization

📸 Screenshots

<img width="1920" height="1080" alt="Screenshot 2025-09-08 202254" src="https://github.com/user-attachments/assets/198d6ac6-8461-406c-8f84-85659529610f" />

<img width="1920" height="1080" alt="Screenshot 2025-09-09 195127" src="https://github.com/user-attachments/assets/b299d3cc-460a-472f-9405-83deb3db0c39" />

<img width="1920" height="1080" alt="Screenshot 2025-09-09 195144" src="https://github.com/user-attachments/assets/fe96e7ac-b528-4657-ac0f-65de18fc413f" />

<img width="1920" height="1080" alt="Screenshot 2025-09-09 195157" src="https://github.com/user-attachments/assets/133c5036-910e-4a97-b98d-a22e480febe2" />

<img width="1920" height="1080" alt="Screenshot 2025-09-09 195208" src="https://github.com/user-attachments/assets/1ad35ca6-9e9f-42e1-b6bb-66b0b288571b" />


⚡ How to Run Locally
# Clone the repo
git clone https://github.com/your-username/Smart-Water-Allocation.git
cd Smart-Water-Allocation

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py


🌍 Future Scope

Integrate with IoT sensors for real-time data

Deploy as a web service for farmers

Expand dataset for multiple regions & more crops

✨ This project showcases how AI can power sustainable agriculture through smart water management. 🌱💧
