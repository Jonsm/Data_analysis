import numpy as np
from matplotlib import pyplot as plt
import scipy.optimize
from textwrap import wrap
def lorentzian (x,gamma,x0,h,offset):
    return offset+(h*(gamma/2)**2)/(np.power(x-x0, 2)+(gamma/2)**2)

#File path
directory = 'D:\Data\Fluxonium waveguide 1\Two_tone'
measurement = '122618_Two_tone_spec_DC_YOKO_0to0mA_Cav_7.0808GHz&-20dBm_QuBit3.5to4GHz&0dBm'
path = directory + '\\' + measurement

freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1:-1]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1:len(freq)+1,0] #phase is recorded in rad
#phase = np.unwrap(phase)*180/np.pi
phase = phase*180/np.pi
phase = phase - np.mean(phase)
mag = data[1:len(freq)+1,1]
plt.figure(1)
plt.plot(freq, phase,'-')
#
#
# guess = ([0.001, freq[np.argmin(phase)], np.max(phase) - np.min(phase), np.min(phase)])
guess = ([0.01, freq[np.argmax(phase)], np.max(phase) - np.min(phase), np.min(phase)])
popt, pcov = scipy.optimize.curve_fit(lorentzian, freq, phase, p0=guess)
plt.plot(freq, lorentzian(freq,*popt))
plt.title('\n'.join(wrap(measurement)) + '\n' + str(popt[1]))
plt.tight_layout()

plt.xlabel('Frequency (GHz)',size=10.0)
plt.ylabel('Phase (deg)',size=10.0)
plt.tick_params(labelsize = 14.0)

plt.show()