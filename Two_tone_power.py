
import numpy as np
from matplotlib import pyplot as plt

cmin = -2
cmax = 2
#File path
directory = 'D:\Data\Fluxonium #28\Two_tone'
measurement = '050818_Two_tone_power_YOKO_-30to5dBm_Cav_7.3367GHz&59.719mA_QuBit0.2to0.35GHz&25dBm'
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
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)

plt.figure(1)
X,Y = np.meshgrid(power, freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu')#, vmin = cmin, vmax = cmax)
plt.ylim([freq[0],freq[-1]])

# plt.figure(2)
# X,Y = np.meshgrid(np.power(10,power/10.0), freq)
# plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = cmin, vmax = cmax)

plt.ylim([freq[0],freq[-1]])
plt.colorbar()
plt.show()