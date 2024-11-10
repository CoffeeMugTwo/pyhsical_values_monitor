import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt


def streamlit_app():
    # Set up Streamlit app
    st.title("Live Tomato Data Monitor")
    temp_chart = st.empty()
    humidity_chart = st.empty()
    soil_humidity = st.empty()
    light_value = st.empty()
    text_box = st.empty()

    while True:

        # load and format data
        data = pd.read_csv(
            "data.csv",
            header=None,
            index_col=None,
            comment="#",
            names=[
                "timestamp",
                "temperature",
                "humidity",
                "soil_humidity_value",
                "light_value",
            ],
        )

        data["Timestamp[datetime64]"] = pd.to_datetime(data["timestamp"], unit="s")

        text_box.write(
            data[
                [
                    "Timestamp[datetime64]",
                    "temperature",
                    "humidity",
                    "soil_humidity_value",
                    "light_value",
                ]
            ].iloc[-5:]
        )

        temp_chart.line_chart(
            data=data,
            x="timestamp",
            y="temperature",
            x_label="Timestamp",
            y_label="Temparature[°C]",
        )

        humidity_chart.line_chart(
            data=data,
            x="timestamp",
            y="humidity",
            x_label="Timestamp",
            y_label="Humidity[%]",
        )

        soil_humidity.line_chart(
            data=data,
            x="timestamp",
            y="soil_humidity_value",
            x_label="Timestamp",
            y_label="Soil Humidity[a.u.]",
        )

        light_value.line_chart(
            data=data,
            x="timestamp",
            y="light_value",
            x_label="Timestamp",
            y_label="Light Value[a.u.]",
        )

        time.sleep(5)  # Update every 5 seconds
        print("alive")


def main():
    """Main function"""
    streamlit_app()


if __name__ == "__main__":
    main()
