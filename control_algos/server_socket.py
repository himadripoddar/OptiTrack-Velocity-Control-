import socket 
import time
from NatNetClient import NatNetClient
host = ''
port = 5560



def receiveNewFrame( frameNumber, markerSetCount, unlabeledMarkersCount, rigidBodyCount, skeletonCount,
                    labeledMarkerCount, timecode, timecodeSub, timestamp, isRecording, trackedModelsChanged ):
    print( "Received frame", frameNumber )

def receiveRigidBodyFrame( id, position, rotation ):
    cordinates.append(position [0] * 50)
    velocity = (cordinates[-1]-cordinates[-2])/dt
    return velocity


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


def dataTransfer(conn):
	while True:

		reply = storedvalue
		conn.sendall(str.encode(reply))
	conn.close()

s= setupServer()

while True:

	streamingClient = NatNetClient()
	# streamingClient.newFrameListener = receiveNewFrame
	# streamingClient.rigidBodyListener = receiveRigidBodyFrame
	streamingClient.run()
	


	storedvalue = receiveRigidBodyFrame
	
	conn = setupConnection()

	dataTransfer(conn)
	

	

	


	


	