import bluetooth

print("Searching for bluetooth devices...")
bluedevices = bluetooth.discover_devices(lookup_names = True)
print("found %d devices" % len(nearby_devices))

for addr, name in bluedevices:
    print("%s - %s" %(addr, name))
