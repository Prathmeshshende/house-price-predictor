# 🏠 House Price Prediction Web App

👉 **[🌐 Try the Live App Here](https://house-price-predictor-krw6szxazxbbkjjtjqeabu.streamlit.app/)**

---

## 📌 Project Overview

This project implements an end-to-end machine learning pipeline to predict house prices using structured housing data.  
The application allows users to input property features and receive real-time price predictions through an interactive web interface.

---

## 📊 Dataset

The model was trained using a structured Housing Prices dataset containing both numerical and categorical features, including:

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

Categorical variables were handled using one-hot encoding.

---

## 🤖 Model Details

- **Algorithm:** Ridge Regression (L2 Regularization)
- **R² Score:** 0.72 on test data
- **Total Features Used:** 20 engineered features

### Why Ridge Regression?
- Controls overfitting using L2 regularization  
- Handles multicollinearity effectively  
- Produces stable and reliable coefficient estimates  
- Well-suited for structured tabular data  

---

## ⚙️ Machine Learning Workflow

1. Data preprocessing  
2. Feature engineering  
3. One-hot encoding of categorical variables  
4. Train-test split  
5. Model training using Ridge Regression  
6. Model serialization using `joblib`  
7. Deployment using Streamlit Cloud  

---

## 🌐 Deployment

The model is deployed as a public web application using Streamlit Cloud.

Live Application:
👉 **https://house-price-predictor-krw6szxazxbbkjjtjqeabu.streamlit.app/**

---

## 🛠 Tech Stack

- Python  
- NumPy  
- pandas  
- scikit-learn  
- Streamlit  
- joblib  

---

## ▶ Run Locally

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py

---

## 📌 Future Improvements

- Model comparison (Ridge vs Gradient Boosting)  
- Hyperparameter tuning  
- Performance optimization  
- Enhanced UI styling  
- Data visualization integration  
