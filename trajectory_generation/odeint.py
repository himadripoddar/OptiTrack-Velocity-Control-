import numpy as np
#import scipy.integrate as spi
import matplotlib.pyplot as plt



#initial conditions

y0 = [0,0]
t = np.linspace(0,5,101)
#u = [1,1,1,1,1]


def y_dash (y,t):
	pos,vel = y
	u =5
	dydt = [[0, 1],[0, 0]]*y + [0,1]*u
	#dydt = [vel,u]
	return dydt

from scipy.integrate import odeint

sol = odeint(y_dash, y0, t)

#plotting
plt.plot(t, sol[:, 0], 'b', label='position')
plt.plot(t, sol[:, 1], 'g', label='velocity')
plt.xlabel('t')
plt.grid()
plt.show()
