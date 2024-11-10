import streamlit as st
import pandas as pd
import time

st.title("Live Tomato Data Monitor")
chart = st.empty()
text_box = st.empty()

while True:

    # load and format data
    data = pd.read_csv("data.csv", header=0, index_col=None)
    data["Timestamp[datetime64]"] = pd.to_datetime(data["Timestamp[unix]"], unit="s").dt.strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    text_box.write(data.iloc[-5:])
    data.set_index(data["Timestamp[datetime64]"], inplace=True)
    data.index = data.index.map(str)
    values = data[["Temperature[C]", "Humidity[%]", "Light Value[a.u.]"]]
    values.index = values.index.map(str)
    chart.line_chart(values)

    print("index dtype: ", values.index.dtype)
    print(values)

    time.sleep(1)  # Update every 5 seconds
    print("alive")
