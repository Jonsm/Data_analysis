import numpy as np
from matplotlib import pyplot as plt
import scipy.optimize
from textwrap import wrap
def lorentzian (x,gamma,x0,h,offset):
    return offset+(h*(gamma/2)**2)/(np.power(x-x0, 2)+(gamma/2)**2)

#File path
directory = 'D:\Data\Fluxonium #22\Two_tone'
measurement = '020418_Two_tone_spec_YOKO_90.604to90.604mA_Cav_7.3262GHz&-15dBm_QuBit0.16to0.18GHz&25dBm'
path = directory + '\\' + measurement

freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1:-1]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1:len(freq)+1,0] #phase is recorded in rad
phase = np.unwrap(phase)*180/np.pi
mag = data[1:len(freq)+1,1]
plt.figure(1)
plt.plot(freq, phase,'-')
#plt.plot(freq, mag)

guess = ([0.002, freq[np.argmax(phase)], np.max(phase) - np.min(phase), np.min(phase)])
popt, pcov = scipy.optimize.curve_fit(lorentzian, freq, phase, p0=guess)
plt.plot(freq, lorentzian(freq,*popt))
plt.title('\n'.join(wrap(measurement)) + '\n' + str(popt[1]))
plt.tight_layout()

plt.show()