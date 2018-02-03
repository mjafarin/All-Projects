import bluetooth

bd_addr = "5C:F3:70:84:B3:FA"

port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

sock.connect((bd_addr, port))

sock.send("hello")

sock.close()
