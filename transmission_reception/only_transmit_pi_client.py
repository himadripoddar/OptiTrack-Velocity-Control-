import socket 
import time
host = '10.64.39.54'
port = 5561	

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
command = 'get'
while True:

	
	s.send(str.encode(command))
	time.sleep(0.05)

	
	

s.close()

