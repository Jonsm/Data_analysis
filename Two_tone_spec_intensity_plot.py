import numpy as np
from matplotlib import pyplot as plt


#File path
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_22.75to23.3mA_Cav_7.3654GHz&-15dBm_QuBit0.5to5.5GHz&25dBm'
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

for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.max(temp)
plt.figure(1)
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = -15, vmax = 1)


#############################################################################################

# for idx in range(len(current)):
#     temp = mag[idx*len(freq):(idx+1)*len(freq)]
#     Z[idx,:] = temp - np.average(temp)
#
# plt.figure(2)
# plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu')#,vmin = 0)
# plt.colorbar()
# plt.xlabel('current (mA)')
# plt.ylabel('Frequency (GHz)')
plt.colorbar()
plt.show()