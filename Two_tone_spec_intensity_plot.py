import numpy as np
from matplotlib import pyplot as plt
import time

c = .2
contrast_max = 2
contrast_min = -2
# File path
directory = 'D:\Data\Fluxonium waveguide 1\Two_tone'

measurement = '122618_Two_tone_spec_DC_YOKO_1.37to1.33mA_Cav_7.0808GHz&-30dBm_QuBit3.75to3.9GHz&0dBm'
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
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)

plt.show()

