import bluetooth
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
ledPinR = 18
GPIO.setwarnings(False)
GPIO.setup(ledPinR, GPIO.OUT)

def Blink(numTimes, speed):
    for i in range (0, numTimes):
        GPIO.output(ledPinR, True)
        print("Blinking" + str(i+1))
        time.sleep(speed)
        GPIO.output(ledPinR, False)
        time.sleep(speed)
    print("Done blinking LED")

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1
server_socket.bind(("",port))
server_sock.listen(1)

client_sock.address = server_sock.accept()
print("Accepted connection from ", address)

while True:
    data = client_sock.recv(1024)
    print("received [%s]", %data)
    if (data == "1"):
        print("LED ON")
        GPIO.output(ledPinR, GPIO.HIGH)
    if (data == "0"):
        print("LED OFF")
        GPIO.output(ledPinR, GPIO.LOW)
    if (data == "5"):
        print("LED BLINK")
        Blink(16, 0.1)
    if (data == "e"):
        print ("EXIT")
        break

client_sock.close()
server_sock.close()
    








    
