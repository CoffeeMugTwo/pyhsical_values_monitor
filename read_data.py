"""This module controls the data reading.
"""

import csv
import logging
import sys
import time

import serial

READOUT_FREQUENCY_S = 2

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


# Serial setup
logging.info("Initialize Arduino Connection ")
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
ser.flushInput()
ser.flush()


def read_sensor(pin_id: str):
    """Receive the value of the respective sensor"""
    ser.flushInput()
    time.sleep(0.5)
    ser.write(f"{pin_id}\n".encode("utf-8"))
    time.sleep(0.5)

    if ser.in_waiting > 0:
        response = ser.readline().decode("utf-8")
        time.sleep(0.5)
        return response


def main():
    """Main method"""

    time.sleep(2)

    with open("data.csv", "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "#",
                "Timestamp[unix]",
                "Temperature[C]",
                "Humidity[%]",
                "Soil Humidity [a.u.]",
                "Light Value[a.u.]",
            ]
        )

        while True:

            try:

                timestamp = time.time()

                # get temp and humidity
                dht_22_answer = read_sensor("D7")
                humidity_value = float(dht_22_answer.split(":")[1].split("-")[0])
                temp_value = float(dht_22_answer.split(":")[1].split("-")[1])

                # get soil humidity
                soil_humidity_value = float(read_sensor("A0").split(":")[1])

                # get light value
                light_value = float(read_sensor("A2").split(":")[1])

                row = [
                    timestamp,
                    temp_value,
                    humidity_value,
                    soil_humidity_value,
                    light_value,
                ]

                writer.writerow(row)

                f.flush()

                logging.info(f"Current Reading: {row}")

                time.sleep(READOUT_FREQUENCY_S)

            except (AttributeError, ValueError) as e:

                logging.error(f"Error reading values from arduino: {e}")


if __name__ == "__main__":
    logging.info("Start reading data.")
    main()
    logging.info("Stop reading data.")
