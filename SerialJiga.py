from time import sleep

import serial
ser = serial.Serial('/dev/ttyUSB0', baudrate = 115200,timeout = 1)  # Aguia

i=0
while i<1:  
    ser.write(b'root\r\n')
    #a=ser.readline()
    #print(a)
    sleep (5)
    ser.write(b'123123123\r\n')
    #b=ser.readline()
    #print(b)
    ser.write(b'echo 1 > /sys/class/gpio/gpio502/value\r\n')
    #c=ser.readline()
    #print(c)
    #ser.write(b'echo 0 > /sys/class/gpio/gpio502/value\r\n')
    i = i+1