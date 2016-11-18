from matplotlib import pyplot as plt
import numpy as np

#File path
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'Two_tone_spec_YOKO_38.28to38.28mA_Qubit_8to8.2GHz_-15dBm_Cav_10.3045GHz_5dBm_IF_0.05GHz_measTime_500ns_avg_50000'
path = directory + '\\' + measurement

#Read data
freq = np.genfromtxt(path + '_FREQ.dat')
freq = freq[1::]

data = np.genfromtxt(path + '_PHASEMAG.dat')
phase = data[1::,0] #phase is recorded in rad
phase = np.unwrap(phase)*180/np.pi
phase = phase - np.mean(phase)
mag = data[1::,1] - np.mean(data[1::,1])
plt.plot(freq, phase)
plt.xlabel('Freq')
plt.ylabel('Phase')
plt.show()
plt.plot(freq, mag)
plt.show()