import numpy as np
from matplotlib import pyplot as plt


#File path
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_28.3to28.8mA_Cav_7.365GHz&-15dBm_QuBit0.45to2.5GHz&10dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1::]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1::,0] #phase is recorded in rad
mag = data[1::,1]
Z = np.zeros((len(current),len(freq)))
# print (phase)
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.max(temp)


X,Y = np.meshgrid(current,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = -1.5, vmax = 0.5)
#plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu_r')#, vmax=-0.0001)
plt.colorbar()
plt.xlim([current[0], current[-1]])
plt.ylim([freq[0],freq[-1]])
plt.xlabel('current (mA)')
plt.ylabel('Qubit freq (GHz)')
plt.grid()
#############################################################################################

# for idx in range(len(current)):
#     temp = mag[idx*len(freq):(idx+1)*len(freq)]
#     Z[idx,:] = temp - np.average(temp)
#
# plt.figure(2)
# plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu_r')#,vmin = 0)
# plt.colorbar()
# plt.xlabel('current (mA)')
# plt.ylabel('Frequency (GHz)')
# plt.grid()
# plt.yticks(np.linspace(freq[0],freq[-1],4))
plt.show()
# plt.ion()
# print phase
