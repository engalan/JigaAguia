
import serial
#import serial.tools.list_ports
from time import sleep

ser = serial.Serial('/dev/ttyUSB0', baudrate = 9600,timeout = 1)  # Aguia
i=0
while i<3:
    #ser = serial.Serial ('/dev/ttyACM1', baudrate = 9600,timeout = 2) #Arduino
    #ser = serial.Serial ('/dev/ttyUSB0', baudrate = 115200,timeout = 1)  # Aguia
  

    #ser.write("e".encode('utf-8'))
    ser.write(b'a')
    s=ser.readline()
    print(s)
    sleep(0.5)
    ser.write(b'A')
    sleep(0.5)
    i = i+1
  


  