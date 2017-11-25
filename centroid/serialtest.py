import serial
import time

ser = serial.Serial(port='COM14', baudrate = '9600')
r=30
z='l'+'-'+str(r)
print z
ser.write("30")

