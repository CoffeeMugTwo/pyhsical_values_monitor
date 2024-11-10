import serial
import time

ser = serial.Serial("/dev/ttyACM0", 9600)
ser.flush()
time.sleep(2)


def read_sensor(pin_id: str):
    ser.flushInput()
    time.sleep(0.5)
    ser.write(f"{pin_id}\n".encode("utf-8"))
    time.sleep(0.5)

    if ser.in_waiting > 0:
        response = ser.readline().decode("utf-8")
        return response


if __name__ == "__main__":

    print(read_sensor("A0"))
    print(read_sensor("A1"))
    print(read_sensor("D7"))
