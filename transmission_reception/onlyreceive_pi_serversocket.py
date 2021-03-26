
import time	

import socket 

host = ''
port = 5562

storedvalue = 'I am receiving'

def setupServer():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print("socket created")
	try:
		s.bind((host,port))

	except:
		print('ERROR')

	return s

def setupConnection():
	s.listen(1)
	conn,address = s.accept()
	return conn







s= setupServer()
conn = setupConnection()

while True:

	
		
	conn.sendall(str.encode(storedvalue))
	time.sleep(0.05)
	
conn.close()

	



