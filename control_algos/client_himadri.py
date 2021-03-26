import socket 
import struct
import serial
import time
import math
import numpy as np
import scipy.linalg as la



#creating and binding the host with port

host = '192.168.0.128'
port = 5562
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

#starting the serial communication with mbed

ser = serial.Serial('/dev/ttyS0',9600)



print('Connected')

def solve_dare(A, B, Q, R):

    x = Q
    x_next = Q
    max_iter = 150
    eps = 0.01

    for i in range(max_iter):
        x_next = A.T @ x @ A - A.T @ x @ B @ \
                 la.inv(R + B.T @ x @ B) @ B.T @ x @ A + Q
        if (abs(x_next - x)).max() < eps:
            break
        x = x_next

    return x_next



def dlqr(A, B, Q, R):

    X = solve_dare(A, B, Q, R)


    K = la.inv(B.T @ X @ B + R) @ (B.T @ X @ A)

    eig_result = la.eig(A - B @ K)

    return K, X, eig_result[0]


def lqr_speed_control(vf,sp,Q,R,indox):

	#indox= indox +1

	v = vf #velocity from motion capture

	tv = sp[indox]

	A = np.zeros ((1,1))
	A[0,0] = 1.0

	B = np.zeros((1,1))
	B[0,0] = dt

	K,_,_ = dlqr(A,B,Q,R)

	x =np.zeros((1,1))

	x[0,0] = v -tv

	ustar = -K @ x

	accel = ustar[0,0]

	vel_inp = vf + accel * dt

	return vel_inp, accel




# LQR control scheme

lqr_Q = np.eye(1)
lqr_R = np.eye(1)
dt =0.1
ind = 0
indix = 0
print("LQR speed control starts!")
vi = 0
vel = [2.0, 6.0, 7.0, 11.0, 4.0]
time_t = 0.0

T = 500.0
while T>= time_t:
	
	reply = s.recv(1024)
	vf = reply.decode('utf-8')
	vf = float(vf)

	# print(vf)

	vi, ai = lqr_speed_control(vf,vel,lqr_Q,lqr_R,indix)
	
	vi_s = str(vi)

	#print(vi)
	#sending the data over serial port
	ser.write(str.encode(vi_s + '\n'))

	
	time_t = round(time_t + dt,2)

	if time_t % 5. == 0.:
		indix = indix +1
		print("feedback = " + str(vf) + "  input = " + str(vi))

s.close()

