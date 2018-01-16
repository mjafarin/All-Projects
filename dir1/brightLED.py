import RPi.GPIO as GPIO #RPI.GPIO is GPIO
import time

GPIO.setmode(GPIO.BOARD) 
ledPinR = 16
#ledPinG = 18
#ledPinY = 22

GPIO.setup(ledPinR, GPIO.OUT)
#GPIO.setup(ledPinG, GPIO.OUT)
#GPIO.setup(ledPinY, GPIO.OUT)

pwm_led = GPIO.PWM(ledPinR, 500)
pwm_led.start(100)

while True:
    duty_s = input("Enter desired Brightness (0 - 100): ")
    duty = int(duty_s)
    pwm_led.ChangeDutyCycle(duty)
    
GPIO.cleanup()


        
