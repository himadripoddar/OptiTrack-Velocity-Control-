import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

 

timestamp = (0,10,20,30,40,50,60,70,80,90)
distance = (10,10,40,40,20,20,50,50,10,10)


# plt.plot(timestamp, distance, 'o')
# plt.show()

 

data = np.array((timestamp,distance))

 

tck,u = interpolate.splprep(data, s=0)
unew = np.arange(0, 1.001, 0.001)
out = interpolate.splev(unew, tck)

print(len(out[1]))



plt.plot(out[0], out[1], color='orange')
plt.plot(data[0,:], data[1,:], 'ob')
plt.show()