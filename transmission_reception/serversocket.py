
	

import socket 

host = ''
port = 5561

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


def GET():
	reply = storedvalue
	return reply




def dataTransfer(conn):
	while True:
		
		#get command from client

		data = conn.recv(1024)
		data = data.decode('utf-8')
		

		dataMessage = data.split(' ',1)
		command = dataMessage[0]

		if command == 'get':
			reply = GET()
			print("I am transmitting")


		conn.sendall(str.encode(reply))
	conn.close()

s= setupServer()
conn = setupConnection()

while True:
	
		

		dataTransfer(conn)

	



