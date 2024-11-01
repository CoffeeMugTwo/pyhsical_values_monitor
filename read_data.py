import serial
import csv
import time

import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


logging.info("Start reading data from Arduino")

# Serial setup
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
ser.flush()

with open("/home/thomas/projects/grow_cabinet/data.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "Temperature", "Humidity", "Light Value"])

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode("utf-8").rstrip()
            if "Temperature" in line and "Humidity" in line and "Light Value" in line:
                parts = line.split(" ")
                temp = float(parts[1])
                humidity = float(parts[4])
                light_value = float(parts[8])
                writer.writerow([time.time(), temp, humidity, light_value])
                f.flush()
                time.sleep(1)

logging.info("Stop reading data.")
