import numpy as np
from matplotlib import pyplot as plt


#File path
directory = "D:\Data\Fluxonium #20\One_tone"
fname = "010918_One_tone_spec_0to0mA_7.3to7.6GHz_-10dBm"
path = directory + '\\' + fname

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')
current = current[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1::]
phasemag = np.genfromtxt(path + '_PHASEMAG.csv')
phase = phasemag[1::,0] #phase is recorded in rad
phase = np.unwrap(phase)*180/(np.pi)
mag = phasemag[1::,1]
magdB = 10*np.log10(mag)
Z_mag = np.zeros((len(current), len(freq)))
Z_phase = np.zeros((len(current), len(freq)-1))
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    delay = (temp[-1]-temp[0]) / (freq[-1]-freq[0])
    temp = temp - freq*delay
    # Z_phase[idx,:] = temp - np.min(temp)
    Z_phase[idx,:] = np.diff(temp - np.min(temp))
    temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z_mag[idx,:] = temp - np.min(temp)


X,Y = np.meshgrid(current, freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z_mag.transpose(), cmap= 'GnBu')#, vmax=0.003)
plt.colorbar()
plt.xlim([current[0], current[-1]])
plt.ylim([freq[0],freq[-1]])

plt.figure(2)
X,Y = np.meshgrid(current, freq[0:-1])
plt.pcolormesh(X,Y,Z_phase.transpose(), cmap= 'GnBu_r')#, vmin = , vmax=-20)
plt.colorbar()
plt.xlim([current[0], current[-1]])
plt.ylim([freq[0],freq[-1]])
plt.show()