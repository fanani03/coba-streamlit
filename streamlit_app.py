import streamlit as st
import pandas as pd


st.title("Belajar KNN")
st.header("Ini Header - Belajar KNN")

#Pengukuran Burung
url = "https://vincentarelbundock.github.io/Rdatasets/csv/Stat2Data/Cuckoo.csv"
df = pd.read_csv(url)


df.info()

df.head(10)

#Mean
st.write("Mean nya adalah ",df["Length"].mean())

#median
st.write("Median nya adalah ",df["Length"].median())

#Modus
st.write("Modusnya ",df["Length"].mode())

