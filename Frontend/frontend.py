import streamlit as st
import requests

### API URL

API_URL = "http://localhost:8000/predict"

### Streamlit App
st.title("Insurance Premium Category Predictor")
st.markdown(
    """
This application predicts the insurance premium category based on user inputs.
Please fill in the details below and click on 'Predict' to see the result.
"""
)
### User Inputs
age = st.number_input("Age", min_value=0, max_value=120, value=30)
weight = st.number_input("Weight (in pounds)", min_value=0.0, value=150.0)
height = st.number_input("Height (in meters)", min_value=0.0, value=1.75)
income_lpa = st.number_input("Income (in LPA)", min_value=0.0, value=5.0)
smoker = st.selectbox("Do you smoke?", options=[True, False])
city = st.text_input("City")
occupation = st.selectbox(
    "Occupation",
    options=[
        "retired",
        "freelancer",
        "student",
        "government_job",
        "business_owner",
        "unemployed",
        "private_job",
    ],
)
if st.button("Predict"):
    user_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation,
    }
    
    try:
        ### Make API Request
        response = requests.post(API_URL, json=user_data)
        result = response.json()

        if response.status_code == 200:
            st.success(
                f"Predicted Insurance Premium Category: **{result['predicted_category']}**"
            )
        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Make sure it's running.")