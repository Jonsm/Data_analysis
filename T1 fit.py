from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

def func(x, a, b, c, d):
    return a*np.exp(-(x-c)/b) + d

directory = 'D:\Data\Fluxonium #10_7.5GHzCav\T1'
fname = '062517_T1_YOKO_24.49mA_Cav7.3644GHz_-7dBm_Qubit4.1372GHz_25dBm_PiPulse580ns_Count20_TimeStep100000.h5'
path = directory + '\\' + fname
pts_num = 20
time_step = 100000
time = np.linspace(0, pts_num*time_step, pts_num)

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    # print phase_raw
    phase = phase_raw[0, 0]
    phase = np.unwrap(phase)*180/np.pi
    phase = phase - np.min(phase)
    phase = abs(phase)
plt.plot(time, phase, 'rd')

guess = [phase[0]-phase[-1], 2e-4, 0, phase[-1]]

popt, pcov = curve_fit(func, time*1e-9, phase, guess)

a,b,c,d = popt #b is T1
time_nice = np.linspace(0, pts_num*time_step, pts_num*100)
phase_fit = func(time_nice*1e-9, a, b, c, d)
perr = np.sqrt(abs(np.diag(pcov)))


plt.plot(time_nice, phase_fit)
plt.title(str( b*1e6)+ r'$\pm$' +str(perr[1]*1e6))
plt.show()
