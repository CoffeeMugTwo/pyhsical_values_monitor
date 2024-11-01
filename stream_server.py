import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt


# Load data
def load_data():
    return pd.read_csv("/home/thomas/projects/grow_cabinet/data.csv")


# Set up Streamlit app
st.title("Live Temperature and Humidity Monitor")
placeholder = st.empty()

while True:
    data = load_data()
    fig, ax = plt.subplots()
    ax.plot(data["Timestamp"], data["Temperature"], label="Temperature (°C)")
    ax.plot(data["Timestamp"], data["Humidity"], label="Humidity (%)")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Value")
    ax.legend()

    placeholder.pyplot(fig)
    time.sleep(5)  # Update every 5 seconds
