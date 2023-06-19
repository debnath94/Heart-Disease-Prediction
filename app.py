# -*- coding: utf-8 -*-
"""
Created on Mon May  8 00:02:44 2023

@author: debna
"""

import os
import streamlit as st
import numpy as np
import pickle
from pickle import load
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier



#scaler = load(open('standard_scaler.pkl', 'rb'))
lr = load(open('heart_disease_forest_new.pickle', 'rb'))



st.title(":red[Heart Disease Prediction]")


Age = st.slider(":blue[Select Your Age]",21, 80, 30 )

Sex = st.radio(":blue[Select Your Gender]", ["Male", "Female"])
if Sex == "Male":
    Sex = 1
else:
    Sex = 0


Chest_Pain_Level = st.radio(":blue[Select Chest Pain Type]",["Microvascular", "Stable", "Unstable", "Variant"])
if Chest_Pain_Level == "Microvascular":
    Chest_Pain_Level=0
elif Chest_Pain_Level == "Stable":
    Chest_Pain_Level = 1
elif Chest_Pain_Level == "Unstable":
    Chest_Pain_Level = 2
elif Chest_Pain_Level == "Variant":
    Chest_Pain_Level = 3


Resting_Blood_Pressure = st.slider(":blue[Select your Resting Blood Pressure]", 90, 200, 105)


Cholestrol = st.slider(":blue[Select Your Cholestrol Level]", 250, 540, 300)


Fasting_Blood_Sugar = st.radio(":blue[Fasting Blood Sugar]", ["Yes", "No"])
if Fasting_Blood_Sugar == "Yes":
    Fasting_Blood_Sugar = 1
else:
    Fasting_Blood_Sugar = 0


Resting_ECG = st.radio(":blue[Select Resting ECG Type]", ["Normal", "Abnormal", "High"])
if Resting_ECG == "Normal":
    Resting_ECG = 0
elif Resting_ECG == "Abnormal":
    Resting_ECG = 1
elif Resting_ECG == "High":
    Resting_ECG = 2


Max_Heart_Rate = st.radio(":blue[Select Your Max Heart Rate]", list(range(0, 201, 25)))


Exercise_Induced_Angina = st.radio(":blue[Select Excercise Induced Angina]", ["Yes", "No"])
if Exercise_Induced_Angina == "Yes":
    Exercise_Induced_Angina = 1
else:
    Exercise_Induced_Angina = 0


Depression = st.slider(":blue[Select Your Depression Level]", 0.0, 6.2,2.0)


SlopeC = st.radio(":blue[Select the Slope Type]", ["Downsloping", "Flat","Upsloping"])
if SlopeC == "Downsloping":
    SlopeC = 0
elif SlopeC == "Flat":
    SlopeC = 1
elif SlopeC == "Upsloping":
    SlopeC = 2


Major_Vessels = st.slider(":blue[Select the Major Vessels]", 1,3, 2)


Thalassemia_Level = st.radio(":blue[Select The Thalassemia Level]", ["Fixed Defect", "Normal", "Reversable Defect"])
if Thalassemia_Level == "Fixed Defect":
    Thalassemia_Level = 0
elif Thalassemia_Level == "Normal":
    Thalassemia_Level = 1
elif Thalassemia_Level == "Reversable Defect":
    Thalassemia_Level = 2

Age_Group = st. radio(":blue[Select the Age Group]",["Senior Citizens", "Super Senior Citizens", "Youngster"])
if Age_Group == "Senior Citizens":
    Age_Group = 0
elif Age_Group == "Super Senior Citizens":
    Age_Group == 1
elif Age_Group == "Youngster":
    Age_Group = 2




if st.button('Predict'):
    query_point = np.array([Age, Sex, Chest_Pain_Level, Resting_Blood_Pressure, Cholestrol, Fasting_Blood_Sugar, Resting_ECG, Max_Heart_Rate, Exercise_Induced_Angina, Depression, SlopeC, Major_Vessels, Thalassemia_Level, Age_Group])
    query_point = query_point.reshape(1, -1)
    #query_point_transformed = scaler.transform(query_point)
    prediction = lr.predict(query_point)


#streamlit run app.py & npx localtunnel --port 8501 






