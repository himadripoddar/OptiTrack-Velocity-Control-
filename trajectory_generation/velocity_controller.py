import math
import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la







lqr_Q = np.eye(1)
lqr_R = np.eye(1)
dt =1
#L = 0.5
ind = 0
#max_steer = np.deg2rad(45.0)

show_animation = True

class State:

	def __init__(self,x=0.0,y=0.0,v=0.0):
 		self.x = x
 		self.y = y
 		self.v = v

def update(state,a):

 	
	state.x = state.x + state.v * dt
	state.y = state.y
	state.v = state.v + a*dt
	return state


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


def lqr_speed_control(state,sp,Q,R,indox):

	#indox= indox +1

	v = state.v

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

	return indox, accel

def do_simulation(speed_profile, goal,indix,a):

	T = 500.0
	#goal_dis = 0.3
	stop_speed = 0.05

	state = State(x =0.0, y = 5.0, v =0.0)

	time = 0.0

	x = [state.x]
	y = [state.y]
	v = [state.v]
	t = [0.0]

	while T>= time:
		
		target_ind, ai = lqr_speed_control(state,speed_profile,lqr_Q,lqr_R,indix)
		

		state = update(state,ai)

		#if abs(state.v)<= stop_speed:
		#	target_ind +=1
		
		if(state.v == goal):
			break

		#if (round(state.v,2)) == speed_profile(indix):
		
		#	indix = indix+1
		time = round(time + dt,2)
		
		if time%5. == 0.:
			indix = indix +1
			print(state.v)
		if indix == a+1:
			break

		x.append(state.x)
		y.append(state.y)
		v.append(state.v)
		t.append(time)
		# if target_ind % 1 == 0 and show_animation:
		plt.cla()
		plt.gcf().canvas.mpl_connect('key_release_event',
				lambda event: [exit(0) if event.key == 'escape' else None])
		#plt.plot(x,y,"ob", label="trajectory")
		plt.plot(t,x,"ob", label="trajectory")
		#plt.axis("equal")
		plt.grid(True)
		plt.title("speed[km/h]:" + str(state.v) + ",target_index:" + str(target_ind))
		plt.pause(0.0001)
	return t, x, y, v
        
    

def main():

	ind = 0

	print("LQR speed control starts!")

	vel = [2.0, 6.0, 7.0, 11.0, 4.0]
	a = len(vel)-1
	goal = [vel[-1]]
	t, x, y, v = do_simulation(vel,goal,ind,a)

	if show_animation:
		plt.close()
		plt.subplots(1)
		plt.plot(t,x, "-g", label ="tracking")
		plt.grid(True)
		plt.axis("equal")
		plt.legend()

		plt.show()





if __name__ == '__main__':
	main()






























