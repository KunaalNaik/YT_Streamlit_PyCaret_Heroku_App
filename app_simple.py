from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

# Load Model
model = load_model('deployment_28042020')

# Create Predict Function
def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

# Create Function to load form for use to input
def run():
    # Load Images
    from PIL import Image
    image_hospital = Image.open('hospital.jpg')

    # Display Information on the Sidebar
    st.sidebar.info('This app is created to predict patient hospital charges')
    st.sidebar.success('https://youtube.com/KunaalNaik')
    st.sidebar.image(image_hospital)

    # App Title
    st.title("Insurance Charges Prediction App")

    # Capture User Inputs
    age = st.number_input('Age', min_value=1, max_value=100, value=25)
    sex = st.selectbox('Sex', ['male', 'female'])
    bmi = st.number_input('BMI', min_value=10, max_value=50, value=10)
    children = st.selectbox('Children', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    if st.checkbox('Smoker'):
        smoker = 'yes'
    else:
        smoker = 'no'

    region = st.selectbox('Region', ['southwest', 'northwest', 'northeast', 'southeast'])

    output = ""

    # Create Dict to provide to Predict Function, also convert to Pandas Dataframe
    input_dict = {'age': age, 'sex': sex, 'bmi': bmi, 'children': children, 'smoker': smoker, 'region': region}
    input_df = pd.DataFrame([input_dict])

    # Prediction happens when Predict Button is pressed
    if st.button("Predict"):
        output = predict(model=model, input_df=input_df)
        output = '$' + str(output)

    # Display the Prediction
    st.success('The output is {}'.format(output))


if __name__ == '__main__':
    run()