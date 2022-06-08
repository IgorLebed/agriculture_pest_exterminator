import serial, string, time
input_ = " "
ser = serial.Serial("/dev/ttyUSB0", 57600, 8, 'N', 1, timeout=1)
n = 0
while True:
    #line_x = "this is line "
    input_ = ser.write(b'Line')
    n += 1
    print("Message sent! "+"#"+str(n))
    time.sleep(5)