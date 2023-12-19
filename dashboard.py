import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from babel.numbers import format_currency
sns.set(style='dark')

hour_df = pd.read_csv("https://raw.githubusercontent.com/AlfanArzaqi/bike-sharing-dataset/main/hour.csv")

day_df = pd.read_csv("https://raw.githubusercontent.com/AlfanArzaqi/bike-sharing-dataset/main/day.csv")

hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

hour_df['temp'] = hour_df['temp'] * 41
hour_df['atemp'] = hour_df['atemp'] * 50
hour_df['hum'] = hour_df['hum'] * 100
hour_df['windspeed'] = hour_df['windspeed'] * 67

day_df['temp'] = day_df['temp'] * 41
day_df['atemp'] = day_df['atemp'] * 50
day_df['hum'] = day_df['hum'] * 100
day_df['windspeed'] = day_df['windspeed'] * 67

st.title("Bike Share Dashboard :sparkles:")

if st.checkbox("Show Raw Data from Hour Dataset"):
    st.subheader("Raw Data")
    st.write(hour_df)

if st.checkbox("Show Raw Data from Day Dataset"):
    st.subheader("Raw Data")
    st.write(day_df)

with st.sidebar:
    st.header ("About Me")
    st.subheader ("Alfan Miftah Arzaqi")


season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day_df["season_label"] = day_df["season"].map(season_mapping)

season_count = day_df.groupby("season_label")["cnt"].sum().reset_index()
fig_season_count = px.bar(season_count, x="season_label",
                            y="cnt", title="Season-wise Bike Share Count")
st.plotly_chart(fig_season_count, use_container_width=True)

weather_mapping = {1: "Clear", 2: "Mist + Cloudy", 3: "Light Snow/Rain", 4: "Heavy Rain/Snow"}
hour_df["weather_label"] = hour_df["weathersit"].map(weather_mapping)

weather_count = hour_df.groupby("weather_label")["cnt"].sum().reset_index()
fig_weather_count = px.bar(weather_count, x="weather_label",
                            y="cnt", title="Weather Rent Bike Share Count")
st.plotly_chart(fig_weather_count, use_container_width=True)

st.caption('Copyright (c) AlfanArzaqi 2023') 