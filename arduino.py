from serial import Serial
import time

class Arduino:
    def __init__(self):
        self.my_serial = Serial('/dev/ttyACM0', 9600)
        time.sleep(2)

    def send(self, string):
        user_in = str.encode(string)
        self.my_serial.write(user_in)

    def __del__(self):
        self.my_serial.flush()
        self.my_serial.close()
