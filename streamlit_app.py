import streamlit as st
import pandas as pd
import joblib
from sklearn.neighbors import KNeighborsClassifier


st.title("Belajar KNN")
st.header("dataset IRIS")

SL = st.number_input('Insert Sepal Length')
SW = st.number_input('Insert Sepal Width')
PL = st.number_input('Insert Petal Length')
PW = st.number_input('Insert Petal Width')

data_baru = [[SL, SW, PL, PW]] 


if st.button("Tentukan"):
    knn = joblib.load("modelKnnIris.pkl")
    inp_pred = knn.predict(data_baru)
    if inp_pred[[0]] == 0:
        st.success("Hasil Prediksi adalah Setosa")
    elif inp_pred[[0]] == 1:
        st.success("Hasil Prediksi adalah Versicolor")
    else:
        st.success("Hasil Prediksi adalah Virginica")


    
    

