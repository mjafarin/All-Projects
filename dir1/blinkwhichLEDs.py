import RPi.GPIO as GPIO #RPI.GPIO is GPIO
import time

pins = [16, 18, 22]

pin_led_states = [
    [1, 0, -1],
    [0, 1, -1],
    [-1, 1, 0],
    [-1, 0, 1],
    [1, -1, 0],
    [0, -1, 1]
    ]

GPIO.setmode(GPIO.BOARD) 

def set_pin(pin_index, pin_state):
    if pin_state == -1:
        GPIO,setup(pins[pin_index], GPIO.IN)
    else:
        GPIO.setup(pins[pin_index], GPIO.OUT)
        GPIO.output(pins[pin_index], pin_state)

def light_led(led_number):
    for pin_index, pin_state in enumerate(pin_led_states[led_number]):
        set_pin(pin_index, pin_state)

set_pin(0, -1)
set_pin(1, -1)
set_pin(2, -1)

while True:
    x = int(raw_input("Pin (0, 4):"))
    light_led(x)
    
GPIO.cleanup()


        
