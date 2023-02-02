import pandas as pd
import numpy as np
import pickle
import streamlit as st
import time

pickle_in = open('model_uas.pkl', 'rb')
model_uas = pickle.load(pickle_in)

st.set_page_config(page_title="PremiPredict Apps")

def prediction(age, sex, bmi, children, smoker):
    prediction = model_uas.predict([[age, sex, bmi, children, smoker]])
    print(prediction)
    return prediction

def main():
    st.title("Prediksi Pembayaran Premi Asuransi Menggunakan Algoritma Regresi Linear")
    st.markdown("<strong><span style='color:red'>&nbsp;Agung Gunawan / 2019230012</span></strong>", unsafe_allow_html=True)
    st.write('\n')
    
    st.write('\n')
    st.write('\n')
    
    st.sidebar.markdown("<strong><span style='color:red'>Mohon input data sebelum memprediksi.</span></strong>", 
                        unsafe_allow_html=True)
    
    sex_dict = {'Male':0, 'Female':1}
    smoke_dict = {'No':0, 'Yes':1}
    
    age = st.sidebar.number_input("Age", 0)
    sex = st.sidebar.radio('Sex', tuple(sex_dict.values()))
    bmi = st.sidebar.slider("BMI (body mass index)", 0, 200, 0)
    children = st.sidebar.number_input("Children", 0)
    smoker = st.sidebar.radio('Smoker', tuple(smoke_dict.values()))
    
    result =""
    
    st.write('\n')
    if st.button("SUBMIT"):
        result = prediction(age, sex, bmi, children, smoker)
        
        st.write('\n')
        st.write('\n')
        st.write('\n')
        with st.spinner('Sedang diproses'):
            time.sleep(2)
        #st.success(f'Sukses, diprediksi spesies {result_predict}.')
        st.success(f'Sukses, diprediksi premi {result}.')
            
if __name__=='__main__':
    main()
    
    
#menghilangkan burger dan made with streamlit
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
