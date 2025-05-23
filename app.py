import streamlit as st
import numpy as np
import pickle
# from sklearn.datasets import fetch_california_housing 
# from xgboost import XGBRegressor


filename = "house_prediction_model.pkl"
model= pickle.load(open(filename, 'rb'))


# Streamlit app
st.title("California House Price Prediction")
st.write("Enter the details below to predict the house price:")

# Input fields for user
median_income = st.number_input("Median Income (in $10,000s)", min_value=0.0, step=0.1)
house_age = st.number_input("House Age (in years)", min_value=0.0, step=0.1)
avg_rooms = st.number_input("Number of  Rooms per Household", min_value=0.0, step=0.1)
avg_bedrooms = st.number_input("Number of  Bedrooms per Household", min_value=0.0, step=0.1)
population = st.number_input("Population in Block", min_value=0.0, step=1.0)
households = st.number_input("Households in Block", min_value=0.0, step=1.0)

area = st.selectbox("Select Area", ["Bay Area", "Los Angeles", "San Diego", "Sacramento", "Fresno", "San Jose", "Orange County", "Riverside", "San Francisco", "Oakland"])

# Area to latitude/longitude mapping
area_coords = {
    "bay area": (37.7749, -122.4194),
    "los angeles": (34.0522, -118.2437),
    "san diego": (32.7157, -117.1611),
    "sacramento": (38.5816, -121.4944),
    "fresno": (36.7378, -119.7871),
    "san jose": (37.3382, -121.8863),
    "orange county": (33.7175, -117.8311),
    "riverside": (33.9806, -117.3755),
    "san francisco": (37.7749, -122.4194),
    "oakland": (37.8044, -122.2711),
}

# Default coordinates if area not found
default_latitude = 37.85
default_longitude = -122.25

coords = area_coords.get(area.strip().lower(), (default_latitude, default_longitude))
latitude, longitude = coords

# Predict button
if st.button("Predict"):
    # Prepare the input data
    input_data = np.array([[median_income, house_age, avg_rooms, avg_bedrooms, population, households,latitude, longitude]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the result
    st.success(f"Predicted House Price: ${prediction[0] * 100000:.2f}")
