import numpy as np
from matplotlib import pyplot as plt


#File path
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\One_tone_spec'
measurement = 'One_tone_spec_0mA_7.35to7.4GHz_10to-50dBm'
path = directory + '\\' + measurement

#Read data
power = np.genfromtxt(path + '_Power.csv')
power = power[1:-1]
freq = np.genfromtxt(path + '_Freq.csv')
freq = freq[1::]
data = np.genfromtxt(path + '_PhaseMag.csv')
phase = data[1::,0] #phase is recorded in rad
mag = data[1::,1]
magdB = 10*np.log10(mag)
Z = np.zeros((len(power), len(freq)))
# print (phase)
for idx in range(len(power)):
    # temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = mag[idx*len(freq):(idx+1)*len(freq)]

    Z[idx,:] = temp# - np.mean(temp)

# Z = Z*180/(np.pi)

X,Y = np.meshgrid(power, freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = 0, vmax=0.005)
plt.ylim([freq[0],freq[-1]])
plt.colorbar()
plt.show()