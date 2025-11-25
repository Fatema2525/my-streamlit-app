import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/DELL/Downloads/trained_model.sav','rb'))

def diabetes_prediction(info):
    
   info_as_numpy_array=np.asarray(info)
   info_reshaped=info_as_numpy_array.reshape(1,-1)

   

   prediction=loaded_model.predict(info_reshaped)

   if(prediction[0]==0):
     return 'The person is not diabetic'
   else:
     return 'The person is diabetic'
def main():
    st.title('Diabetes Prediction Wed App')
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure =  st.text_input('Blood Pressure level')
    SkinThickness =  st.text_input('Skin Thickness value')
    Insulin	=  st.text_input('Insulin level')
    BMI	=  st.text_input('BMI')
    DiabetesPedigreeFunction =  st.text_input('Diabetes Pedigree Function value')
    Age =  st.text_input('Age of the person')