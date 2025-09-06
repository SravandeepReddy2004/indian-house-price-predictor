import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(page_title="🏠 Indian House Price Predictor", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: #4B0082;'>🏠 Indian House Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Estimate the price of a house using important features.</p>", unsafe_allow_html=True)
st.write("---")

# Layout: split input into two columns
col1, col2 = st.columns(2)

with col1:
    city = st.selectbox("🏙 City", ["Ahmedabad", "Bengaluru", "Delhi NCR", "Pune", "Chennai", "Kolkata", "MMR", "Hyderabad"])
    property_type = st.selectbox("🏠 Property Type", ["Apartment", "Independent House", "Villa", "Penthouse", "Studio"])
    bhk = st.slider("🛏 Number of BHK", 0, 10, 2)
    bathrooms = st.slider("🛁 Number of Bathrooms", 1, 10, 2)
    balconies = st.slider("🌿 Number of Balconies", 0, 5, 1)

with col2:
    furnishing = st.selectbox("🛋 Furnishing", ["Furnished", "Semi-Furnished", "Unfurnished"])
    facing = st.selectbox("🌞 Facing", ["North", "South", "East", "West", "North-East", "North-West", "South-West"])
    building_type = st.selectbox("🏢 Building Type", ["Bungalow", "Low Rise", "High Rise", "Mid Rise", "Gated Community", "Standalone Building"])
    carpet_area = st.number_input("📐 Carpet Area (sqft)", min_value=100, max_value=10000, value=1000)
    floor = st.number_input("🏢 Current Floor", min_value=0, max_value=100, value=1)
age_years = st.slider("⏳ Age of Property (Years)", 0, 100, 10)
# Collect features into DataFrame
features = pd.DataFrame([{
    "City": city,
    "Furnishing": furnishing,
    "Facing": facing,
    "PropertyType": property_type,
    "BuildingType": building_type,
    "BHK": bhk,
    "Bathrooms": bathrooms,
    "Balconies": balconies,
    "CarpetArea_sqft": carpet_area,
    "Floor": floor,
    "AgeYears": age_years
}])

# Convert number to Indian notation
def format_inr(amount):
    if amount >= 1e7:
        return f"{amount/1e7:.2f} Cr"
    elif amount >= 1e5:
        return f"{amount/1e5:.0f} Lakh"
    else:
        return f"₹{amount:,.0f}"

# Prediction button
if st.button("💰 Predict House Price"):
    prediction = model.predict(features)[0]
    formatted_price = format_inr(prediction)
    st.success(f"🏡 Estimated House Price: **{formatted_price}**")
