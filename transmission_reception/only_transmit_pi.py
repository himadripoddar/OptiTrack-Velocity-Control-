import socket 
host = '192.168.0.197'
port = 5561	

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while True:

	command = 'get'
	s.send(str.encode(command))

	
	

s.close()

