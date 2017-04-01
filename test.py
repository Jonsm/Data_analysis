from matplotlib import pyplot as plt
import numpy as np
import scipy.optimize as opt



#File path
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\One_tone_spec'
fname = 'One_tone_spec_28.575to28.575mA_7.55to7.6GHz_-15dBm.csv'
path = directory + '\\' + fname
imported = np.genfromtxt(path)[1:, :]
freq = imported[1::, 0]
phase = imported[1::, 1]
mag = imported[1::, 2]
magdB = 10*np.log10(mag)
phase = np.unwrap(phase) * 180/np.pi
phase_delay = (phase[-1]-phase[0])/(freq[-1]-freq[0])
# phase = phase - freq*phase_delay
phase = phase-np.mean(phase)
plt.figure(1)
plt.plot(freq, mag)
plt.figure(2)
plt.plot(freq, phase)

plt.show()