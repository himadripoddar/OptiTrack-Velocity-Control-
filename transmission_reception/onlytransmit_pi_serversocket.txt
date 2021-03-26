
import socket
import time 

host = ''
port = 5561

storedvalue = 'b+20c+40d+60b+20c+40d+60b+20c+40d+60b+20c+40d+60b+20c+40d+60b+20c+40d+60b+20c+40d+60b+20c+40d+60'

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

def repeat(dataMessage):
	reply = dataMessage[1]


def dataTransfer(conn):
	while True:
		
		#get command from client

		data = conn.recv(1024)
		data = data.decode('utf-8')
		

		dataMessage = data.split(' ',1)
		command = dataMessage[0]

		if command == 'get':
			print("transmit")

		
	conn.close()

s= setupServer()

while True:

		conn = setupConnection()

		dataTransfer(conn)
		


