import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm = GPIO.PWM(11,50)  #(pin,freq[Hz]);100Hz=1/10ms=1/10^-2=10^2=100 :)
pwm.start(5)
pwm.ChangeDutyCycle(1)

