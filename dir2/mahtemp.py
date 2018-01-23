import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

the_dir = '/sys/bus/w1/devices/'
my_device = glob.glob(the_dir + '28*')[0]
the_file = my_device + '/w1_slave'

def temp_raw():
    f = open(the_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def whats_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.5)
        lines = temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_value = lines[1][equals_pos+2:]
        temp_c = float(temp_value) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

while True:
  print(whats_temp())
  time.sleep(1)

