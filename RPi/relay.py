import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

GPIO.output(16, GPIO.LOW)
time.sleep(3)
GPIO.output(16, GPIO.HIGH)

GPIO.cleanup()
print("Done!")





