import numpy as np
import matplotlib.pyplot as plt
import scipy
x = np.arange(0,70000)
y = np.loadtxt('pi_tx_line.TXT')
from scipy import signal

#n = 10
#b = [1.0 / n]*n
#a =1
#yy =lfilter(b,a,y)

def smooth(y,box_pts):
	box = np.ones(box_pts)/box_pts
	y_smooth = np.convolve(y,box,'same')
	return y_smooth

plt.xlabel('iterations')
plt.xlim(1,69996)
plt.ylim(4,6)
plt.ylabel('voltage')
plt.plot(x,y,'o',lw=0.1)
plt.plot(x,smooth(y,25), 'r-', lw =0.5)
plt.show()
