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
avg_rooms = st.number_input("Number of Rooms per Household", min_value=0.0, step=0.1)
avg_bedrooms = st.number_input("Number of Bedrooms per Household", min_value=0.0, step=0.1)
population = st.number_input("Population in Block", min_value=0.0, step=1.0)
households = st.number_input("Households in Block", min_value=0.0, step=1.0)
latitude= 37.85
longitude= -122.25

# Predict button
if st.button("Predict"):
    # Prepare the input data
    input_data = np.array([[median_income, house_age, avg_rooms, avg_bedrooms, population, households,latitude, longitude]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the result
    st.success(f"Predicted House Price: ${prediction[0] * 100000:.2f}")
