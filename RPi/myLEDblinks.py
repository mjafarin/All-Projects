import RPi.GPIO as GPIO #RPI.GPIO is GPIO
import time

GPIO.setmode(GPIO.BOARD) 
ledPin = 16
GPIO.setup(ledPin, GPIO.OUT)
blinks =int(input("Times to blink?"))

for i in range(0,blinks):
    GPIO.output(ledPin, True)
    time.sleep(1)
    GPIO.output(ledPin, False)
    time.sleep(1)
    
GPIO.cleanup()


        
