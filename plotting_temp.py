import numpy as np
from matplotlib import pyplot as plt


#File path
directory = "D:\Data\Fluxonium #10"
fname = "One tune spectroscopy_YOKO 0mAto50mA_ qubit tone off_Cav_10p30GHz to 10p32GHz_1dBm_pulse_4000_2800_after 2nd thermal cycle"
path = directory + '\\' + fname

#Read data
current = np.genfromtxt(path + '_Current.csv', delimiter = ',')
current = current[0::]
freq = np.genfromtxt(path + '_Freq.csv', delimiter = ',')
freq = freq[0::]
mag = np.genfromtxt(path + '_Phase d.csv', delimiter = ',')

X,Y = np.meshgrid(current, freq)

Z = mag.transpose()
plt.pcolormesh(X,Y,Z)
plt.show()