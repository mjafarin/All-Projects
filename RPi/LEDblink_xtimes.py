import RPi.GPIO as GPIO #RPI.GPIO is GPIO
import time

ledPin = 22 #physical pin 22

GPIO.setmode(GPIO.BOARD) 

GPIO.setup(ledPin, GPIO.OUT)
blinks = int(input("Times to blink?"))

for i in range(0,blinks):
    GPIO.output(ledPin, True)
    time.sleep(1)
    GPIO.output(ledPin, False)
    time.sleep(1)
    
GPIO.cleanup()


        
