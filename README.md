# 🏠 House Price Prediction Web App

This project implements an end-to-end machine learning pipeline to predict house prices using structured housing data.

## 📊 Dataset
Housing Prices dataset with multiple numerical and categorical features including:
- Area
- Bedrooms
- Bathrooms
- Stories
- Parking
- Main road access
- Guest room availability
- Basement
- Hot water heating
- Air conditioning
- Preferred area
- Furnishing status

Categorical variables were one-hot encoded for model compatibility.

## 🤖 Model
Algorithm: Ridge Regression  
Why Ridge?
- Handles multicollinearity
- Reduces overfitting through L2 regularization
- Stable coefficient estimates

Performance:
- R² Score: 0.72 on test data

## ⚙️ Workflow
1. Data preprocessing
2. Feature encoding
3. Train-test split
4. Model training
5. Model serialization using joblib
6. Deployment using Streamlit

## 🌐 Live Demo
[Your Streamlit Link Here]

## 🛠 Tech Stack
- Python
- NumPy
- pandas
- scikit-learn
- Streamlit
- joblib

## ▶ Run Locally
pip install -r requirements.txt
streamlit run app.py
