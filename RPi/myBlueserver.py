#created Feb 1, 2018
import bluetooth
import RPi.GPIO as GPIO

LED = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,0)

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1
server_socket.bind(("",port))
server_socket.listen(1)

client_socket.address = server_socket.accept()
print ("Accepted connection from ", address)

while 1:
    data = client_socket.recv(1024)
    print("Received: %s",data)
    if (data == "0"):
        print("PIN 40 LOW, LED OFF ")
        GPIO.output(LED, 0)
    if (data == "1"):
        print("PIN 40 HIGH, LED ON ")
        GPIO.output(LED, 1)
    if (data == "q"):
        print("Quit")
        break

    client_socket.close()
    server_socket.close()
    
