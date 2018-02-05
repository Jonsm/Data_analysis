import numpy as np
from matplotlib import pyplot as plt
import time

c = 1
contrast_max = 0.5
contrast_min = -0.5
# File path
directory = 'D:\Data\Fluxonium #22\Two_tone'

measurement = ''
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1:]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1:,0] #phase is recorded in rad
mag = data[1:,1]
Z = np.zeros((len(current),len(freq)))
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)
plt.figure(1)
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)


# plt.xlim([0.5, 0.59])
# plt.ylim([0.1, 0.6])
plt.colorbar()
plt.tick_params(labelsize = 18.0)
plt.show()
