import streamlit as st
import pandas as pd


import matplotlib.pyplot as plt
import seaborn as sns

st.title("Belajar KNN")
st.header("Ini Header - Belajar KNN")

#Pengukuran Burung
url = "https://vincentarelbundock.github.io/Rdatasets/csv/Stat2Data/Cuckoo.csv"
df = pd.read_csv(url)

st.write("Menampilkan informasi tipe data di semua kolom")
st.write(df.info())


st.write("Menampilkan 5 baris teratas")
st.write(df.head(10))

#Mean
st.write("Mean nya adalah ",df["Length"].mean())

#median
st.write("Median nya adalah ",df["Length"].median())

#Modus
st.write("Modusnya ",df["Length"].mode())


plt.figure()
sns.distplot(df["Length"])
plt.show()
