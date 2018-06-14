import numpy as np
from matplotlib import pyplot as plt
import scipy.optimize
from textwrap import wrap
def lorentzian (x,gamma,x0,h,offset):
    return offset+(h*(gamma/2)**2)/(np.power(x-x0, 2)+(gamma/2)**2)

#File path
directory = 'D:\Data\Fluxonium #23\Two_tone'
measurement = '061418_Two_tone_spec_YOKO_91.26to91.26mA_Cav_7.5612GHz&-5dBm_QuBit0.61to0.65GHz&25dBm'
path = directory + '\\' + measurement

freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1:-1]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1:len(freq)+1,0] #phase is recorded in rad
phase = np.unwrap(phase)*180/np.pi
mag = data[1:len(freq)+1,1]
plt.figure(1)
plt.plot(freq, phase)#-np.mean(phase),'-')
# plt.plot(freq, mag)

#guess = ([0.001, freq[np.argmax(phase)], np.max(phase) - np.min(phase), np.min(phase)])
guess = ([0.0001, 0.63, np.max(phase) - np.min(phase), np.min(phase)])
popt, pcov = scipy.optimize.curve_fit(lorentzian, freq, phase, p0=guess)
plt.plot(freq, lorentzian(freq,*popt))
plt.title('\n'.join(wrap(measurement)) + '\n' + str(popt[1]))
plt.tight_layout()

plt.xlabel('Frequency (GHz)',size=10.0)
plt.ylabel('Phase (deg)',size=10.0)

# plt.tick_params(labelsize = 18.0)
plt.show()