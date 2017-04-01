import numpy as np
from matplotlib import pyplot as plt
import scipy.optimize

def lorentzian (x,gamma,x0,h,offset):
    return offset+(h*(gamma/2)**2)/(np.power(x-x0, 2)+(gamma/2)**2)

#File path
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_28.575to28.575mA_Cav_7.365GHz&-15dBm_QuBit0.5to0.51GHz&12dBm'
path = directory + '\\' + measurement

freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1::]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1::,0] #phase is recorded in rad
phase = np.unwrap(phase)*180/np.pi
mag = data[1::,1]
plt.figure(1)
# plt.plot(freq, phase)
# print(lorentzian(freq,.5,.5))
popt, pcov = scipy.optimize.curve_fit(lorentzian, freq, mag, p0=[.01,.5,.01,.015])
plt.plot(freq,lorentzian(freq,*popt))
#plt.figure(2)
plt.plot(freq, mag)
plt.show()