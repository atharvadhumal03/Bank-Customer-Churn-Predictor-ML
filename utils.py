import pandas as pd

def model_input(Credit_Score, Geography, Gender, Age, Tenure, Balance, Num_Of_Products, Has_Cr_Card, Is_Active_Member, Estimated_Salary):
    
    input_data = pd.DataFrame({
        'CreditScore': [Credit_Score],
        'Geography': [Geography],
        'Gender': [Gender],
        'Age': [Age],
        'Tenure': [Tenure],
        'Balance': [Balance],
        'NumOfProducts': [Num_Of_Products],
        'HasCrCard': [Has_Cr_Card],
        'IsActiveMember': [Is_Active_Member],
        'EstimatedSalary': [Estimated_Salary]
    })
    
    return input_data

def predict_churn(X, final_churn_model, threshold=0.35):

    """Predict churn with custom threshold"""
    probabilities = final_churn_model.predict_proba(X)[:, 1]
    return (probabilities >= threshold).astype(int)

