import numpy as np
from matplotlib import pyplot as plt


#File path
directory = 'D:\Data\Fluxonium waveguide 1\One_tone'
measurement = '122618_One_tone_power_QubitOn_1msDuration10usRead1.349mA_7.05to7.1GHz_-25to20dBm'
path = directory + '\\' + measurement

#Read data
power = np.genfromtxt(path + '_POWER.csv')
power = power[1:]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1:]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1:,0] #phase is recorded in rad
mag = data[1:,1]
magdB = np.log10(mag)
Z1 = np.zeros((len(power), len(freq)))
# print (phase)
for idx in range(len(power)):
    # temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = magdB[idx*len(freq):(idx+1)*len(freq)]
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z1[idx,:] = temp - np.max(temp)

# Z = Z*180/(np.pi)

X,Y = np.meshgrid(power, freq+0.1)
plt.pcolormesh(X,Y,Z1.transpose(), cmap= 'GnBu')#, vmin = -5, vmax=-1.5)

measurement = '122618_One_tone_power_1msDuration10usRead1.349mA_7.05to7.1GHz_-25to20dBm'
path = directory + '\\' + measurement

#Read data
power = np.genfromtxt(path + '_POWER.csv')
power = power[1:]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1:]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1:,0] #phase is recorded in rad
mag = data[1:,1]
magdB = np.log10(mag)
Z = np.zeros((len(power), len(freq)))
# print (phase)
for idx in range(len(power)):
    # temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = magdB[idx*len(freq):(idx+1)*len(freq)]
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    # Z[idx,:] = temp - np.max(temp)

toplot= (abs(Z1)-abs(Z)) / (abs(Z1)+abs(Z))
# plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu')#, vmin = -5, vmax=-1.5)
# plt.pcolormesh(X,Y,toplot.transpose(), cmap= 'GnBu', vmin = -0.05, vmax=0.05)
# plt.ylim([freq[0],freq[-1]])
plt.colorbar()
plt.ylabel('Cavity freq (GHz)')
plt.xlabel('dBm')
plt.show()