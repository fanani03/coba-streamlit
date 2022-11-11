import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Pengukuran Burung
url = "https://vincentarelbundock.github.io/Rdatasets/csv/Stat2Data/Cuckoo.csv"
dataset = pd.read_csv(url)

#Menampilkan informasi tipe data di semua kolom
dataset.info()

# Menampilkan 5 baris teratas
dataset.head(10)

#Mean
dataset["Length"].mean()

#median
dataset["Length"].median()

#Modus
dataset["Length"].mode()

plt.figure()
sns.distplot(dataset["Length"])
plt.show()