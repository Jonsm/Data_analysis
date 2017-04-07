from matplotlib import pyplot as plt
import numpy as np

directory = 'D:\Data\Fluxonium #10_7.5GHzCav\One_tone_spec'
fname = 'One_tone_spec_fixedFreq_0to60_mA_7.363GHz_-15dBm'
path = directory + '\\' + fname

current = np.genfromtxt(path+'_PHASEMAG.csv')[1::,0]
# current = np.linspace(25,35,1001)
phase = np.genfromtxt(path+'_PHASEMAG.csv')[1::,1]
phase = np.unwrap(phase)
phase = phase*180/np.pi
mag = np.genfromtxt(path+'_PHASEMAG.csv')[1::,2]

plt.figure(1)
plt.plot(current, phase)
plt.figure(2)
plt.plot(current, mag)

plt.show()