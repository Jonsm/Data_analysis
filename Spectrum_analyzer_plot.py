import numpy as np
from matplotlib import pyplot as plt

directory = 'D:\Data\Calibration\\2018-12-05-Spectrum'
fname = 'Qubit_leak.csv'
path = directory + '\\' + fname
data = np.genfromtxt(path, delimiter = ',')
plt.plot(data[0]/1e9, data[1])
plt.xlabel('GHz')
plt.ylabel('dB')
plt.grid()
plt.title(fname)
plt.show()