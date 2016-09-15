import numpy as np
from matplotlib import pyplot as plt


#File path
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'Two tone spec_YOKO41mA_46mA_Qubit2 to 4GHz n5dBm_Cav 10p304GHz 8dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURR.dat')
current = current[1::]
freq = np.genfromtxt(path + '_FREQ.dat')
freq = freq[1::]
data = np.genfromtxt(path + '_PHASEMAG.dat')
phase = data[1::,0] #phase is recorded in rad
phase = phase*180/(np.pi)

Z = np.zeros((len(current),len(freq)))
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    Z[idx,:] = temp - np.average(temp)

X,Y = np.meshgrid(current,freq)

plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu_r', vmin = -5, vmax=1)
plt.colorbar()
plt.xlabel('Current (mA)')
plt.ylabel('Qubit freq (GHz)')
plt.show()
plt.ion()
# print phase
