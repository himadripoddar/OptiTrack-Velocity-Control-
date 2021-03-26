import socket
import time 
host = '192.168.0.197'
port = 5562    

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while True:

        reply = s.recv(1024)
        print(reply.decode('utf-8'))


s.close()

