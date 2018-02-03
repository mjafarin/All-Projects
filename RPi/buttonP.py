import RPi.GPIO as GPIO #RPI.GPIO is GPIO
import time

GPIO.setmode(GPIO.BOARD) 

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(16)
    if input_state == False:        
        print("Button pressed")
        time.sleep(0.5)
    
GPIO.cleanup()


        
