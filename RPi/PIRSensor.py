import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN) #PIR
GPIO.setup(18, GPIO.OUT) #LED

try:
    time.sleep(2) 

    while True:
        if GPIO.input(16):
            GPIO.output(18, True)
            time.sleep(2)
            GPIO.output(18, False)
            print("Motion detected")
            time.sleep(5) #avoiding multiple detections
        time.sleep(1) #loop delay for detection 
except:
    GPIO.cleanup()


