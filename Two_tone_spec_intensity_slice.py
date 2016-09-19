import numpy as np
from matplotlib import pyplot as plt


#File path
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'Two tone spec_YOKO41mA_46mA_Qubit2 to 4GHz 5dBm_Cav 10p304GHz 5dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURR.dat')
current = current[1::]
freq = np.genfromtxt(path + '_FREQ.dat')
freq = freq[1::]
data = np.genfromtxt(path + '_PHASEMAG.dat')
phase = data[1::,0] #phase is recorded in rad
phase = phase#*180/(np.pi)
mag = data[1::,0]
plt.figure(1)
Z = np.zeros((len(current),len(freq)))
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    Z[idx,:] = temp - np.average(temp)

# Z = Z.transpose()

plt.plot(freq, Z[15])

plt.figure(2)
for idx in range(len(current)):
    Z[idx,:] = mag[idx*len(freq):(idx+1)*len(freq)]

plt.plot(freq, Z[15])

plt.show()