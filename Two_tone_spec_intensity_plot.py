import numpy as np
from matplotlib import pyplot as plt


#File path
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'Two_tone_spec_YOKO_38.1to40mA_Qubit_3.5to5GHz_5dBm_Cav_10.3039GHz_8dBm_IF_0.05GHz_measTime_500ns_avg_25000'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURR.dat')#*1e3
current = current[1:-1]
freq = np.genfromtxt(path + '_FREQ.dat')
freq = freq[1::]
data = np.genfromtxt(path + '_PHASEMAG.dat')
phase = data[1::,0] #phase is recorded in rad
mag = data[1::,1]
Z = np.zeros((len(current),len(freq)))
# print (phase)
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    Z[idx,:] = temp - np.average(temp)

Z = Z*180/(np.pi)
X,Y = np.meshgrid(current,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu_r', vmin = -5, vmax=0)
plt.colorbar()
plt.xlim([current[0], current[-1]])
plt.ylim([freq[0],freq[-1]])
plt.xlabel('current (mA)')
plt.ylabel('Qubit freq (GHz)')
plt.grid()
for idx in range(len(current)):
    temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.average(temp)

plt.figure(2)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu_r')#, vmin = -1, vmax=0)
plt.colorbar()
plt.xlabel('current (mA)')
plt.ylabel('Frequency (GHz)')
plt.yticks(np.linspace(freq[0],freq[-1],4))
plt.show()
# plt.ion()
# print phase
