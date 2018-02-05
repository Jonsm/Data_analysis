from matplotlib import pyplot as plt
import numpy as np

#File path
directory = 'D:\Data\Calibration'
measurement = 'restest.csv'
path = directory + '\\' + measurement
data = np.genfromtxt(path, skip_header=1)

traceA = data[:,0]
traceB = data[:,2]

plt.plot(traceA, traceB)


plt.show()