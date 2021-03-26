
import struct
import socket
import serial 
import time

# commint = 0.02

host = '192.168.0.128'
port = 5562

ser = serial.Serial("/dev/ttyS0",9600)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print("connected")
tic = time.time()
command = 'x'
while True:
	
   b = 23.42
   b_s = str(b)
   #print(b_s)
   ser.write(str.encode(b_s + '\n'))
   time.sleep(0.1)


s.close()

