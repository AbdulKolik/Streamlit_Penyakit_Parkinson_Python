import pickle
import numpy as np
import streamlit as st

# loading the saved models

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Parkinson's Prediction Page
st.title('Parkinsons Prediction')
    
col1, col2, col3, col4, col5 = st.columns(5)  
    
with col1:
    fo = st.number_input('MDVP:Fo(Hz)')
        
with col2:
    fhi = st.number_input('MDVP:Fhi(Hz)')
        
with col3:
    flo = st.number_input('MDVP:Flo(Hz)')
        
with col4:
    Jitter_percent = st.number_input('MDVP:Jitter(%)')
        
with col5:
    Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')
        
with col1:
    RAP = st.number_input('MDVP:RAP')
        
with col2:
    PPQ = st.number_input('MDVP:PPQ')
        
with col3:
    DDP = st.number_input('Jitter:DDP')
        
with col4:
    Shimmer = st.number_input('MDVP:Shimmer')
        
with col5:
    Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')
        
with col1:
    APQ3 = st.number_input('Shimmer:APQ3')
        
with col2:
    APQ5 = st.number_input('Shimmer:APQ5')
        
with col3:
    APQ = st.number_input('MDVP:APQ')
        
with col4:
    DDA = st.number_input('Shimmer:DDA')
        
with col5:
    NHR = st.number_input('NHR')
        
with col1:
    HNR = st.number_input('HNR')
        
with col2:
    RPDE = st.number_input('RPDE')
        
with col3:
    DFA = st.number_input('DFA')
        
with col4:
    spread1 = st.number_input('spread1')
        
with col5:
    spread2 = st.number_input('spread2')
        
with col1:
    D2 = st.number_input('D2')
        
with col2:
    PPE = st.number_input('PPE')
        
    
    
# code for Prediction
parkinsons_diagnosis = ''
    
# creating a button for Prediction    
if st.button("Hasil Tes Parkinson"):
    parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
    if (parkinsons_prediction[0] == 1):
        parkinsons_diagnosis = "Orang tersebut menderita penyakit Parkinson"
    else:
        parkinsons_diagnosis = "Orang tersebut tidak menderita penyakit Parkinson"
        
st.success(parkinsons_diagnosis)