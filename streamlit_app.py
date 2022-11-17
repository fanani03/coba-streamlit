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
    if inp_pred == 0:
        st.write("Setosa")
    else if inp_pred == 1:
        st.write("Versicolor")
    else:
        st.write("Virginica")


    
    

