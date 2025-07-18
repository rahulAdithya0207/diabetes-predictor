# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 16:45:40 2025

@author: Rahul
"""

import numpy as np 
import pickle 
import streamlit as st

loaded_model = pickle.load(open('trained_model.sav','rb'))
#creating a function for prediction
def diabetes_prediction(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardize the input data

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
def main():
    
    #making the title 
    st.title('Diabetes Prediction Web App')
    #getting the input data from the use
    Pregnancies = st.text_input('Number if Pregnanacies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin thickness value')
    Insulin = st.text_input('Insulin value')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('age of the person')


    #code for prediction
    diagnosis = ''
    
    #creating a button for prediciton
    if st.button('Diabetes Test Result'):
       diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]) 
       
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
