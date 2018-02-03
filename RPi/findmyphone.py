import bluetooth

target_name = "Pixel"
target_address = None

nearby_devices = bluetooth.discover_devices()

for baddr in nearby_devices:
    if target_name == bluetooth.lookup_name(baddr):
        target_address = baddr
        break

if target_address is not None:
    print("found target bluetooth device with address", target_address)
else:
    print ("could not find target bluetooth device nearby")
