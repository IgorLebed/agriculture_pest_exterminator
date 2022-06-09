import serial, string, time
import json

input_ = " "
ser = serial.Serial("/dev/ttyUSB0", 57600, 8, 'N', 1, timeout=1)
n = 0


path_to_json = ("/home/igor/agriculture_pest_exterminator/gui/coverage_path_planning/trajectory.json")


def read_from_json():
    try:
        trajectory = []
        f = open(path_to_json)
        data = json.load(f)  
        
        for i in data:
            trajectory.append(i)
        f.close()
        return trajectory
    except:
        print("Json not found in method!")
        exit(0)

trajectory = read_from_json()
#print(trajectory)

while True:
    byte = "chr(0x40)"
    
    #line_x = "this is line "
    input_ = ser.write(str(trajectory).encode())
    n += 1
    print("Message sent! "+"#"+str(n))
    time.sleep(5)