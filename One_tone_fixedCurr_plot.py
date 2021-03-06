import numpy as np
from matplotlib import pyplot as plt
import scipy.optimize
from textwrap import wrap

def lorentzian (x,gamma,x0,h,offset):
    return offset+(h*(gamma/2)**2)/(np.power(x-x0, 2)+(gamma/2)**2)

#File path
directory = 'D:\Data\Fluxonium waveguide 1\One_tone'
fname = '122718_One_tone_spec_0to0mA_7.0to7.2GHz_-30dBm'
path = directory + '\\' + fname

phase = np.genfromtxt(path+"_PHASEMAG.csv")[1:,0]
mag = np.genfromtxt(path+"_PHASEMAG.csv")[1:,1]
freq = np.genfromtxt(path+"_FREQ.csv")[1:-1]
phase = np.unwrap(phase)*180/np.pi
offset = (phase[-1] - phase[0])/(freq[-1] - freq[0])*freq
phase = phase - offset
phase = phase - np.mean(phase)
I = mag*np.cos(phase*np.pi/180)
Q = mag*np.sin(phase*np.pi/180)

# '''
kappa = 0.005
guess = ([kappa, freq[np.argmax(mag)], np.max(mag) - np.min(mag), 0])
popt, pcov = scipy.optimize.curve_fit(lorentzian, freq, mag, p0=guess)

# plt.figure(1)
# plt.plot(freq, phase)
plt.figure(2)
plt.plot(freq, mag)
plt.plot(freq, lorentzian(freq, *popt))
plt.title('\n'.join(wrap(fname)) + '\n' + str(popt[1]) +"GHz"+ '\n' + str(popt[0]*1e3)+'MHz')
# plt.figure(3)
# plt.plot(I,Q)

plt.show()