import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11, True)
GPIO.output(11, False)
GPIO.output(11, True)
mah_pwm = GPIO.PWM(11,1)  #(pin,freq[Hz]);100Hz=1/10ms=1/10^-2=10^2=100 :)
mah_pwm.start(50)
mah_pwm.ChangeDutyCycle(1)

