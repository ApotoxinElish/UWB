import serial
import time

ser = serial.Serial("COM5", 921600, timeout=5)
ser.flushInput()


def main():
    while True:
        count = ser.inWaiting()
        if count != 0:
            recv = ser.read(ser.in_waiting)
            print(time.time(), " --- recv --> ", recv)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
