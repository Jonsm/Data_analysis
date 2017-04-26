import numpy as np
from matplotlib import pyplot as plt

#File path
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\One_tone_spec'
fname = 'One_tone_spec_22.763to22.763mA_7.35to7.38GHz_-15dBm'
path = directory + '\\' + fname

phase = np.genfromtxt(path+"_PHASEMAG.csv")[1:,0]
mag = np.genfromtxt(path+"_PHASEMAG.csv")[1:,1]
freq = np.genfromtxt(path+"_FREQ.csv")[1::]
phase = np.unwrap(phase)*180/np.pi
offset = (phase[-1] - phase[0])/(freq[-1] - freq[0])*freq
phase = phase - offset
phase = phase - np.mean(phase)
I = mag*np.cos(phase*np.pi/180)
Q = mag*np.sin(phase*np.pi/180)

plt.figure(1)
plt.plot(freq, phase)
plt.figure(2)
plt.plot(freq, mag)
plt.figure(3)
plt.plot(I,Q)

plt.show()