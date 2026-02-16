import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("house_price_model.pkl")

# App title
st.set_page_config(page_title="🏠 House Price Predictor", layout="centered")
st.title("🏠 House Price Predictor")
st.markdown("Enter details of the house below to predict its **estimated price**:")

st.write("---")

# 1️⃣ Property Basic Info
st.header("📊 Basic Property Information")
area        = st.number_input("📏 Area (in sq. ft)", min_value=0.0, step=0.1)
bedrooms    = st.number_input("🛏️ Bedrooms", min_value=0, step=1)
bathrooms   = st.number_input("🛁 Bathrooms", min_value=0, step=1)
stories     = st.number_input("🏢 Stories", min_value=1, step=1)
parking     = st.number_input("🚗 Parking Spots", min_value=0, step=1)

st.write("---")

# 2️⃣ Road Access
st.header("🛣️ Road & Facilities")
mainroad_yes = st.radio("Main Road Access?", ("Yes", "No"))
mainroad_yes = 1 if mainroad_yes == "Yes" else 0

guestroom_yes = st.radio("Guest Room Available?", ("Yes", "No"))
guestroom_yes = 1 if guestroom_yes == "Yes" else 0

basement_yes = st.radio("Basement Available?", ("Yes", "No"))
basement_yes = 1 if basement_yes == "Yes" else 0

hotwaterheating_yes = st.radio("Hot Water Heating?", ("Yes", "No"))
hotwaterheating_yes = 1 if hotwaterheating_yes == "Yes" else 0

airconditioning_yes = st.radio("Air Conditioning?", ("Yes", "No"))
airconditioning_yes = 1 if airconditioning_yes == "Yes" else 0

prefarea_yes = st.radio("Preferred Area Location?", ("Yes", "No"))
prefarea_yes = 1 if prefarea_yes == "Yes" else 0

st.write("---")

# 3️⃣ Furnishing Status
st.header("🛋 Furnishing Status")
furn_status = st.selectbox(
    "Furnishing Status",
    ("Unfurnished", "Semi-Furnished", "Furnished")
)

# One-hot encoding for furnishing
furn_furnished       = 1 if furn_status == "Furnished" else 0
furn_semi_furnished  = 1 if furn_status == "Semi-Furnished" else 0
furn_unfurnished     = 1 if furn_status == "Unfurnished" else 0

st.write("---")

# Predict button
if st.button("👉 Predict Price"):
    # Prepare input array in the exact order your model expects
    input_data = np.array([[
        area,
        bedrooms,
        bathrooms,
        stories,
        parking,
        1-mainroad_yes,     # mainroad_no
        mainroad_yes,
        1-guestroom_yes,    # guestroom_no
        guestroom_yes,
        1-basement_yes,     # basement_no
        basement_yes,
        1-hotwaterheating_yes,  # hotwaterheating_no
        hotwaterheating_yes,
        1-airconditioning_yes,  # airconditioning_no
        airconditioning_yes,
        1-prefarea_yes,     # prefarea_no
        prefarea_yes,
        furn_furnished,
        furn_semi_furnished,
        furn_unfurnished
    ]])

    # Make prediction
    prediction = model.predict(input_data)
    
    # Format and display
    price_est = round(prediction[0], 2)
    st.success(f"💰 **Estimated House Price: ₹ {price_est:,}**")

    st.write("---")
    st.caption("Prediction based on your feature inputs.")

