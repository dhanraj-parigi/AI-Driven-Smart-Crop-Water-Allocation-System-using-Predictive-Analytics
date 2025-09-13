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

Enter Area: 142

Enter Production: 118

Output:

💧 Water Allocated: 72.5%

🚰 Status: High Water Needed

📊 Bar & Line Chart for visualization

📸 Screenshots

<img width="1920" height="1080" alt="Screenshot 2025-09-13 191904" src="https://github.com/user-attachments/assets/17da78a7-3d04-4e5f-827e-7271dfa2268c" />

<img width="1920" height="1080" alt="Screenshot 2025-09-13 191916" src="https://github.com/user-attachments/assets/aaccb4e5-daa7-43e2-9e94-b2d037efe13a" />

<img width="1920" height="1080" alt="Screenshot 2025-09-13 191935" src="https://github.com/user-attachments/assets/61052566-1d4b-415e-8fd8-6e1ef9c803a8" />

<img width="1920" height="1080" alt="Screenshot 2025-09-13 191945" src="https://github.com/user-attachments/assets/21fe3a1f-9b35-4d3f-bcc6-c6452322b84c" />

<img width="1920" height="1080" alt="Screenshot 2025-09-13 192006" src="https://github.com/user-attachments/assets/699f401b-24ff-4ae0-b0a8-da36a2ab3130" />




🎥 Sample Video 


https://github.com/user-attachments/assets/63dfeed9-b8bd-429b-9668-fdd828cbee85




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
