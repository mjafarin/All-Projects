import RPi.GPIO as GPIO #RPI.GPIO is GPIO
import time

ledPin = 11 #physical pin 11

def setup():
    GPIO.setmode(GPIO.BOARD) # Setting GPIO numbering of pins
    GPIO.setup(ledPin, GPIO.OUT)    # Set LED pin as OUTPUT
    GPIO.output(ledPin, GPIO.LOW)   # Set ledPin to LOW for turning off the LED

def loop():
    while True:
        print ('LED on')
        GPIO.output(ledPin, GPIO.HIGH)  #LED On
        time.sleep(1.0)
        print ('LED off')
        GPIO.output(ledPin, GPIO.LOW) #LED Off
        time.sleep(1.0)

def endprogram():
    GPIO.output(ledPin, GPIO.LOW)   #LED Off
    GPIO.cleanup() #Release resources

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the destroy() will be executed.
        endprogram()
        
