#!/usr/bin/env python
# coding: utf-8


# In[3]:

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

st.title("Versions des modules Python nécessaires à l'éxécution du script")

st.write("version de st =>", st.__version__)
st.write("version de pd =>", pd.__version__)
st.write("version de sns =>", sns.__version__)
st.write("version de plt =>", matplotlib.__version__)


# In[4]:


st.title("Exportation et visualisation d'un jeu de données sur les voitures")

df_car = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")


# In[5]:


df_car


# In[28]:
st.title("Carte de chaleur des corrélations observables dans le data set présenté plus haut")


viz_correlation = sns.heatmap(df_car.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True), annot=True)

st.pyplot(viz_correlation.figure)


# In[9]:


st.write("On observe des corrélations assez fortes dans le cluster Cylinders-Cubicinches-hp-weightlbs")


# In[35]:
st.title("Observation détaillée de la corrélation entre le volume des véhicules et leur puissance en chevaux")

df_corr = df_car[["cubicinches", "hp", "continent"]]

v1 = st.radio("Continent", df_corr["continent"].unique())

st.line_chart(data=df_corr.loc[df_car["continent"] == v1])


