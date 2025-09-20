import streamlit as st
from utils import model_input, predict_churn
# import pandas as pd
# import pickle
import joblib

# with open("model.pkl", "rb") as f:
#     model_pipeline = pickle.load(f)

model_pipeline = joblib.load('model.joblib')

# predict_churn = funcs["predict_churn"]
# model_input = funcs["model_input"]


# st.title("Customer Churn Prediction")
st.markdown("<h1 style='text-align: center;'>Bank Customer Churn Prediction</h1>", unsafe_allow_html=True)

# GUI code
st.markdown(
    """
    
    <div style='text-align: center; color: black; font-size: 13px;'>
        © Atharva Dhumal | A bank customer churn predictor model.
    </div>
    <hr style="margin-top: 10px;"/>
    """,
    unsafe_allow_html=True
)
st.markdown(
"""
    <style>
    .stApp {
        background-color: #005EB8;
    }
    </style>
    """,
    unsafe_allow_html=True
    # 31487A
)

st.markdown(
    """
    <style>
    .stButton > button {
        width: 100%;
        background-color: white;
        color: black;
        height: 2.5em;
        border-radius: 10px;
        border: none;
        font-size: 20px;
        font-weight: bold;
        transition: all 0.3s;
        margin-top: 25px;
    } 

     .stButton > button:hover {
        background-color: #FF6B6B;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(255, 75, 75, 0.4);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --- Inputs ---

col1, col2, col3 = st.columns(3)

with col1:
    credit_score = st.number_input("Credit Score", min_value=300, max_value=900, step=1)

    geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
    
    gender = st.selectbox("Gender", ["Male", "Female"])

    age = st.number_input("Age", min_value=18, max_value=95, step=1)



with col2:
    tenure = st.number_input("Tenure (years with bank)", min_value=0, max_value=45, step=1)

    balance = st.number_input("Balance", min_value=0.0, step=100.0, format="%.2f")

    num_products = st.number_input("Number of Products", min_value=0, max_value=9, step=1)

    estimated_salary = st.number_input("Estimated Salary", min_value=0.0, step=100.0, format="%.2f")



with col3:
    has_card = st.radio("Has Credit Card?", ["Yes", "No"])

    is_active = st.radio("Is Active Member?", ["Yes", "No"])


has_card = 1.0 if has_card == "Yes" else 0.0
is_active = 1.0 if is_active == "Yes" else 0.0


# def model_input(Credit_Score, Geography, Gender, Age, Tenure, Balance, Num_Of_Products, Has_Cr_Card, Is_Active_Member, Estimated_Salary):

if st.button("Predict Churn"):
    input_ready_data = model_input(credit_score, geography, gender, age, tenure, balance, num_products, has_card, is_active, estimated_salary)
    prediction = predict_churn(input_ready_data, model_pipeline)
    
    if prediction[0] == 0:
        st.success(f"Prediction: Given customer will not churn!")
    else:
        st.info(f"Prediction: Given customer will churn!")