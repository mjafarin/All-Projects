import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
green = 11
GPIO.setup(green, GPIO.OUT)
mah_pwm = GPIO.PWM(green,100)
mah_pwm.start(0)
while(1):
    bright = int(input("Ho bright you want the LED?(1-6) "))
    mah_pwm.ChangeDutyCycle(2**bright)
my_pwm.stop()
GPIO.cleanup()
    
