import socket 
import time
from NatNetClient import NatNetClient
host = ''
port = 5562

coordinates = []
velocity = [0]
dt = 0.1
current_coords = 0
prev_coords = 0
t = 0.0
tic = time.time()

def receiveNewFrame( frameNumber, markerSetCount, unlabeledMarkersCount, rigidBodyCount, skeletonCount,
                    labeledMarkerCount, timecode, timecodeSub, timestamp, isRecording, trackedModelsChanged ):
    # print( "Received frame", frameNumber )
    global dt,tic
    toc = time.time()

    if toc-tic >= dt:
#        print('toc-tic = ' + str(toc-tic))
        tic = time.time()

    return None

def receiveRigidBodyFrame( id, position, rotation ):
    global coordinates, current_coords, prev_coords
    current_coords = position [0] * 50
    coordinates.append(current_coords)
#    print(coordinates[-1]-coordinates)
#    velocity.append(abs(coordinates[-1]-coordinates[-2])/dt) 
#    print('vel diff = ' + str(abs(coordinates[-1]-coordinates[-2])))
    
    
def vel_calc(coord_array):
    global current_coords,prev_coords
    dt = 0.1
    deltax = abs(current_coords-prev_coords)
    prev_coords = current_coords
    vel = deltax/dt
    
    return vel

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

#def GET():
#    v = round(vel_calc(coordinates),3)
#    print('v = ' + str(v))
#    velocity.append(v)
#    time.sleep(dt)
#    storedvalue = str(v)
#    conn.sendall(str.encode(storedvalue))  
    
def dataTransfer(conn):
    global t
    while True:
#        data = conn.recv(1024)
#        a = data.decode('utf-8')
#        Message = data.split(' ',1)
#        command = dataMessage[0]
#        if command == 'get':
#            reply = GET()
        v = round(vel_calc(coordinates),3)
#        print('v = ' + str(v))
        t = round(t + 1,2)
        if t%5 == 0:
            print('v ='+ str(v))
        velocity.append(v)
        time.sleep(dt)
        storedvalue = str(velocity[-1])
        conn.sendall(str.encode(storedvalue))
        time.sleep(0.2)

		
        
        
        


s= setupServer()

streamingClient = NatNetClient()
streamingClient.newFrameListener = receiveNewFrame
streamingClient.rigidBodyListener = receiveRigidBodyFrame
streamingClient.run()

while True:
    

    conn = setupConnection()
    print('Connection set!')
    dataTransfer(conn)

conn.close()

	

	

	


	


	