import RPi.GPIO as GPIO #RPI.GPIO is GPIO
import time

GPIO.setmode(GPIO.BOARD) 
ledPinR = 16
ledPinG = 18
ledPinY = 22

GPIO.setup(ledPinR, GPIO.OUT)
GPIO.setup(ledPinG, GPIO.OUT)
GPIO.setup(ledPinY, GPIO.OUT)

blinks =int(input("Times to blink? "))

for i in range(0,blinks):
    GPIO.output(ledPinR, True)
    time.sleep(1)
    GPIO.output(ledPinG, True)
    time.sleep(1)
    GPIO.output(ledPinY, True)
    time.sleep(1)
    GPIO.output(ledPinR, False)
    time.sleep(1)
    GPIO.output(ledPinG, False)
    time.sleep(1)
    GPIO.output(ledPinY, False)
    time.sleep(1)
    
GPIO.cleanup()


        
