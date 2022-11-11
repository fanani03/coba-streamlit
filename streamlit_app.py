import streamlit as st
import pandas as pd

#Pengukuran Burung
url = "https://vincentarelbundock.github.io/Rdatasets/csv/Stat2Data/Cuckoo.csv"
df = pd.read_csv(url)

#Menampilkan informasi tipe data di semua kolom
df.info()

# Menampilkan 5 baris teratas
df.head(10)

#Mean
st.write("Mean nya adalah ",df["Length"].mean())

#median
st.write("Median nya adalah ",df["Length"].median())

#Modus
st.write("Modusnya ",df["Length"].mode())
