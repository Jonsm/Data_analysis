
import numpy as np
from matplotlib import pyplot as plt

cmin = -1
cmax = 3
#File path
directory = 'D:\Data\Fluxonium waveguide 1\Two_tone'
measurement = '122718_Two_tone_ACStark_DC_YOKO_0mA_Cav_7.081GHz&-30to20dBm_QuBit3.2to4GHz&-20dBm'
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
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = cmin, vmax = cmax)
plt.ylim([freq[0],freq[-1]])
plt.xlabel('Power (dbm)')
plt.ylabel('Frequency (GHz')

plt.figure(2)
X,Y = np.meshgrid(np.power(10,power/10.0), freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = cmin, vmax = cmax)

# plt.ylim([freq[0],freq[-1]])



plt.show()