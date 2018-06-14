import numpy as np
from matplotlib import pyplot as plt
import time

c = 1
contrast_max = 0.5
contrast_min = -.5
# File path
directory = 'D:\Data\Fluxonium #23\Two_tone'

measurement = '061418_Two_tone_spec_YOKO_91.22to91.3mA_Cav_7.5612GHz&0dBm_QuBit2.66to2.68GHz&15dBm'
path = directory + '\\' + measurement
#
# #Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3  b
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
#
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu_r', vmin = contrast_min, vmax = contrast_max)

plt.colorbar()
plt.tick_params(labelsize = 18.0)
plt.show()


