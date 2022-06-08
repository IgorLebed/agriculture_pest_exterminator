import serial, string
output  = " "
ser = serial.Serial("/dev/ttyUSB0", 57600, 8, 'N', 1, timeout=1)
while True:
    output = ser.readline()
    print(output)
