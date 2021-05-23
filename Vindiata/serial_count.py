import serial
import time
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=5)
#ser1 = serial.Serial('/dev/USB1', 9600, timeout=1)
# read from Arduino
input = ser.read()
print ("Read input " + input.decode("utf-8") + " from Arduino")

while True:
        # write something back
        ser.write(b'A')
        # read response back from Arduino
        for i in range (0,6):
                input = ser.read()
                input_number = str(input)
                print ("Read input back: " + str(input_number))
        time.sleep(1)
