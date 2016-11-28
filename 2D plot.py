from matplotlib import pyplot as plt
import numpy as np

#File path
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'Two_tone_spec_YOKO_44.5to44.5mA_Qubit_3to3.5GHz_10dBm_Cav_10.3039GHz_8dBm_IF_0.05GHz_measTime_500ns_avg_50000'
path = directory + '\\' + measurement

#Read data
freq = np.genfromtxt(path + '_FREQ.dat')
freq = freq[1::]

data = np.genfromtxt(path + '_PHASEMAG.dat')
phase = data[1::,0] #phase is recorded in rad
phase = np.unwrap(phase+0.1)*180/np.pi
phase = phase - np.mean(phase)
mag = data[1::,1] - np.mean(data[1::,1])
plt.plot(freq, phase)
plt.xlabel('Freq')
plt.ylabel('Phase')
plt.show()
plt.plot(freq, mag)
plt.show()