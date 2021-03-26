from NatNetClient import NatNetClient
coordinates = []

def receiveNewFrame( frameNumber, markerSetCount, unlabeledMarkersCount, rigidBodyCount, skeletonCount,
                    labeledMarkerCount, timecode, timecodeSub, timestamp, isRecording, trackedModelsChanged ):
    print( "Received frame", frameNumber )

def receiveRigidBodyFrame( id, position, rotation ):
    cordinates.append(position [0] * 50)
    cordinates.append(position [1] * 50)
    cordinates.append(position [2] * 50)
    print( "Pos and rot for "+str(id) + " = " + str(cordinates))
    cordinates.clear()

streamingClient = NatNetClient()

streamingClient.newFrameListener = receiveNewFrame
streamingClient.rigidBodyListener = receiveRigidBodyFrame

streamingClient.run()