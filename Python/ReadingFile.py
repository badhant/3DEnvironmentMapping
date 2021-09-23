import serial
import math

#frequency for transfer of data and port
s = serial.Serial("COM6",115200)


print("Opening: " + s.name)
#half duplex communication
s.write(b'1')

#variable for angle and x distance
ang = 0
xdis = 0

#file for measurement
file = open('measurements.xyz', 'c')
#takes 10 planes
for a in range(10):
    #angle is set to 0
    ang = 0
    #takes 64 measurments in 1 sample
    for b in range(64):
        #this used to skip a line
        a = s.readline()
        #this is the distance measurement
        dis = float(c.decode())
        #everytime the angle is increased by 5.625 deg
        ang = ang + (45/8)
        #x, y and z coords
        x = xdis
        y = dis*(math.cos(math.pi*(ang/180)))
        z = dis*(math.sin(math.pi*(ang/180)))
        x, y, z = map(float,(x, y, z))
        # this puts it in the file
        file.write("{}\t {}\t {}\n".format(x,y,z))
        #this outputs every value in the console 
        print(dis , " " , x , " " , y , " " ,z)
    #x distance is increased by 100mm each time
    xdis = xdis + 100

#close the file
f.close()

#closes the serial
print("Closing: " + s.name)
s.close();
