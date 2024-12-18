import pickle
import streamlit as st

# Load the pickled model
model = pickle.load(open(r'D:\VS_CODE(PROJECTS-NARESH-IT)\Ensamble learning\model.pkl', 'rb'))

# Function to predict and return the result
def predict_note_authentication(CreditScore, Geography_1, Geography_2, Geography_3, gender, age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary):   
    prediction = model.predict([[CreditScore, Geography_1, Geography_2, Geography_3, gender, age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]])
    print(prediction)
    return prediction

# Streamlit app title
st.title('Churn Prediction')

# Input fields for the model features
CreditScore = st.number_input('CreditScore')
Geography_1 = st.number_input('Geography_1 (1 for Delhi, 0 for others)')
Geography_2 = st.number_input('Geography_2 (1 for Bangalore, 0 for others)')
Geography_3 = st.number_input('Geography_3 (1 for Mumbai, 0 for others)')
gender = st.radio("Select Gender", options=[0, 1], index=0)
age = st.number_input('Age')
Tenure = st.number_input('Tenure')
Balance = st.number_input('Balance')
NumOfProducts = st.number_input('NumOfProducts')
HasCrCard = st.radio("Has Credit Card?", options=[0, 1], index=0)
IsActiveMember = st.radio("Is Active Member?", options=[0, 1], index=0)
EstimatedSalary = st.number_input('EstimatedSalary')

# When the 'Predict' button is clicked, make a prediction
if st.button('Predict'):
    result = predict_note_authentication(CreditScore, Geography_1, Geography_2, Geography_3, gender, age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary)
    st.success(result)
    if result==0:
        st.write('The customer will not leave the bank')
    else:
        st.write('The customer will leave the bank')
