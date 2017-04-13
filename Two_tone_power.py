
import numpy as np
from matplotlib import pyplot as plt


#File path
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_POWER_-20to0mA_Cav_7.3649GHz&-15dBm_QuBit7.8to7.9GHz'
path = directory + '\\' + measurement

#Read data
power = np.genfromtxt(path + '_POWER.csv')
power = power[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1::]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1::,0] #phase is recorded in rad
mag = data[1::,1]
magdB = 10*np.log10(mag)
Z = np.zeros((len(power), len(freq)))
# print (phase)
for idx in range(len(power)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)

X,Y = np.meshgrid(power, freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu')#, vmin = -1.5, vmax = 0.5)
plt.ylim([freq[0],freq[-1]])
plt.colorbar()
plt.show()