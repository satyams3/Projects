import requests
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
    response = requests.get('http://google.com')
    print(int(response.status_code))
    if response.status_code == requests.codes.ok:
            GPIO.output(17, GPIO.HIGH)
            print ("ALIVE")
    else:
            GPIO.output(17, GPIO.LOW)
            print ("DISCONNECTED")
    time.sleep(1)
