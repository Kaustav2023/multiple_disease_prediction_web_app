# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 22:14:44 2024

@author: I Am KD
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading saved models

diabetes_model=pickle.load(open('C:/Users/I Am KD/Desktop/Multiple Disease Prediction/Model Saved/final_diabetes_model.sav','rb'))

heart_disease_model=pickle.load(open('C:/Users/I Am KD/Desktop/Multiple Disease Prediction/Model Saved/final_heart_disease_model.sav','rb'))

parkinsons_model=pickle.load(open('C:/Users/I Am KD/Desktop/Multiple Disease Prediction/Model Saved/final_parkinsons_model.sav','rb'))


with st.sidebar:
    
    selected= option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinson Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
if(selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    
    col1, col2, col3= st.columns(3)
    
    with col1:
         Pregnancies=st.text_input('Number of Pregnancies')
         
    with col2:
         Glucose=st.text_input('Glucose Level')
        
    with col3:
         BloodPressure=st.text_input('Blood Pressure Level')
        
    with col1:
         SkinThickness=st.text_input('Skin Thickness Value')
         
    with col2:
         Insulin=st.text_input('Insulin Level')
    
    with col3:
         BMI=st.text_input('BMI Value')
    
    with col1:
         DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    
    with col2:
         Age=st.text_input('Age of the Person')

    diabetes_diagnosis=''

    if st.button('Diabetes Test Result'):
        diabetes_prediction= diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
        if(diabetes_prediction[0]==1):
            diabetes_diagnosis='The person is Diabetic'
        else:
            diabetes_diagnosis='The person is not Diabetic'
            
    st.success(diabetes_diagnosis)
    
if(selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3= st.columns(3)
    
    with col1:
         Age=st.text_input('Age of the Person')
         
    with col2:
         Sex=st.text_input('Sex of the Person')
        
    with col3:
         CP=st.text_input('CP Value')
        
    with col1:
         Trestbps=st.text_input('Trestbps Value')
         
    with col2:
         Chol=st.text_input('Cholestrol Level')
    
    with col3:
         FBS=st.text_input('FBS Value')
    
    with col1:
         Restecg=st.text_input('Rest ECG Level')
    
    with col2:
         Thalach=st.text_input('Thalach Level')
         
    with col3:
         Exang=st.text_input('Exang Level')
    
    with col1:
         Oldpeak=st.text_input('Old Peak Value')
    
    with col2:
         Slope=st.text_input('Slope Value')
         
    with col3:
         CA=st.text_input('CA Level')
         
    with col1:
         Thal=st.text_input('thal: 0 = normal;1 = fixed defect; 2 = reversable defect')
         
    heart_diagnosis=''

    if st.button('Heart Disease Test Result'):
        user_input=[Age,Sex,CP,Trestbps,Chol,FBS,Restecg,Thalach,Exang,Oldpeak,Slope,CA,Thal]
       
        user_input=[float(x) for x in user_input]
        
        heart_prediction=heart_disease_model.predict([user_input])
        
        
        if(heart_prediction[0]==1):
            heart_diagnosis='The person has a Heart Disease'
        else:
            heart_diagnosis='The person does not have a Heart Disease'
            
    st.success(heart_diagnosis)
    
if(selected=='Parkinson Prediction'):
    st.title('Parkinson Prediction using ML')
    
    col1, col2, col3, col4, col5= st.columns(5)
   
    
    with col1:
        MDVP_Fo_Hz=st.text_input('MDVP:Fo(Hz) Levels')
        
    with col2:
        MDVP_Fhi_Hz=st.text_input('MDVP:Fhi(Hz) Levels')
       
    with col3:
        MDVP_Flo_Hz=st.text_input('MDVP:Flo(Hz) Levels')
       
    with col4:
        MDVP_Jitter_percentage=st.text_input('MDVP:Jitter(%) Percentage')
        
    with col5:
        MDVP_Jitter_Abs=st.text_input('MDVP:Jitter(Abs) Value')
   
    with col1:
        MDVP_RAP=st.text_input('MDVP:RAP Value')
   
    with col2:
        MDVP_PPQ=st.text_input('MDVP:PPQ Value')
   
    with col3:
        Jitter_DDP=st.text_input('Jitter:DDP Value')
        
    with col4:
        MDVP_Shimmer=st.text_input('MDVP:Shimmer Level')
   
    with col5:
        MDVP_Shimmer_DB=st.text_input('MDVP:Shimmer(dB) Value')
   
    with col1:
        Shimmer_APQ3=st.text_input('Shimmer:APQ3 Value')
        
    with col2:
        Shimmer_APQ5=st.text_input('Shimmer:APQ5 Value')
        
    with col3:
        MDVP_APQ=st.text_input('MDVP:APQ Level')
        
    with col4:
        Shimmer_DDA=st.text_input('Shimmer:DDA Value')
   
    with col5:
        NHR=st.text_input('NHR Value')
   
    with col1:
        HNR=st.text_input('HNR Value')
   
    with col2:
        RPDE=st.text_input('RPDE Value')
        
    with col3:
        DFA=st.text_input('DFA Level')
   
    with col4:
        spread1=st.text_input('spread1 Value')
   
    with col5:
        spread2=st.text_input('spread2 Value')
        
    with col1:
        D2=st.text_input('D2 Value')   
        
    with col2:
        PPE=st.text_input('PPE Value') 
        
    parkinson_diagnosis=''
   
    if st.button('Parkinson Test Result'):
        user_input= [MDVP_Fo_Hz,MDVP_Fhi_Hz,MDVP_Flo_Hz,MDVP_Jitter_percentage,MDVP_Jitter_Abs, MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_DB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        
        user_input=[float(x) for x in user_input]
        
        parkinson_prediction=parkinsons_model.predict([user_input])
        
        if(parkinson_prediction[0]==1):
            parkinson_diagnosis='The person is Parkinson Positive'
        else:
            parkinson_diagnosis='The person is Healthy'
            
    st.success(parkinson_diagnosis)

