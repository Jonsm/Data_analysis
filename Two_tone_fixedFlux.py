import numpy as np
from matplotlib import pyplot as plt
import scipy.optimize

def lorentzian (x,gamma,x0,h,offset):
    return offset+(h*(gamma/2)**2)/(np.power(x-x0, 2)+(gamma/2)**2)

#File path
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
# directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Three_tone_spec'
# directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Raman'
measurement = '062317_Two_tone_spec_YOKO_24.49to24.49mA_Cav_7.3644GHz&-7dBm_QuBit4.1to4.2GHz&25dBm'
path = directory + '\\' + measurement

freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1:-1]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1:len(freq)+1,0] #phase is recorded in rad
phase = np.unwrap(phase)*180/np.pi
mag = data[1:len(freq)+1,1]
plt.figure(1)
plt.plot(freq, phase)

guess = ([0.005, freq[np.argmin(phase)], np.max(phase) - np.min(phase), np.min(phase)])
popt, pcov = scipy.optimize.curve_fit(lorentzian, freq, phase, p0=guess)
plt.plot(freq, lorentzian(freq,*popt))
plt.title(str(popt[1]))
plt.show()