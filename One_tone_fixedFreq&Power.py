from matplotlib import pyplot as plt
import numpy as np

directory = 'D:\Data\Fluxonium waveguide 1\One_tone'
fname = '122018_One_tone_spec_fixedFreq_-0.2to4mA_7.0808GHz_-30dBm'
path = directory + '\\' + fname

current = np.genfromtxt(path+'_CURRENT.csv')[1:]
# current = np.linspace(25,35,1001)
phase = np.genfromtxt(path+'_PHASEMAG.csv')[1:,0]
phase = np.unwrap(phase)
phase = phase*180/np.pi
mag = np.genfromtxt(path+'_PHASEMAG.csv')[1:,1]

plt.figure(1)
plt.plot(current, phase)
# plt.figure(2)
# plt.plot(current, mag)

plt.xlabel('Current (mA')
plt.ylabel('Phase (deg)')
plt.show()