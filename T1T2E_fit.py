from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

def func(x, a, b, c, d):
    return a*np.exp(-(x-c)/b) + d

#################################################################################################################
#Parameters
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\T2E'
fname = 'T1T2E_YOKO_28.583mA_Cav7.3649GHz_-15dBm_Qubit0.5043GHz_25dBm_PiPulse950ns_Count20_TimeStep20000.h5'
path = directory + '\\' + fname
pts_num = 20
time_step = 20000
T1_guess = 200e-6
T2_guess = 100e-6
#################################################################################################################
time_t2 = np.linspace(0, pts_num*time_step, pts_num)
time_t1 = np.linspace(0, pts_num*time_step*1.75, pts_num)

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    # print phase_raw
    phase = phase_raw[0, 0]
    phase_t1 = phase[::2]
    phase_t2 = phase[1::2]
    phase_t1 = np.unwrap(phase_t1)*180/np.pi
    phase_t1 = phase_t1 - np.min(phase_t1)
    phase_t1 = abs(phase_t1)
    phase_t2 = np.unwrap(phase_t2)*180/np.pi
    phase_t2 = phase_t2 - np.min(phase_t2)
    phase_t2 = abs(phase_t2)

plt.figure(1)
plt.plot(time_t1, phase_t1, 'r-o')
guess = [phase_t1[0]-phase_t1[-1], T1_guess, 0, phase_t1[-1]]
popt, pcov = curve_fit(func, time_t1*1e-9, phase_t1, guess)
a,b,c,d = popt #b is T1
time_nice  = np.linspace(0, pts_num*time_step*1.75, pts_num*100)
phase_fit = func(time_nice*1e-9, a, b, c, d)
perr = np.sqrt(abs(np.diag(pcov)))
plt.plot(time_nice, phase_fit)
plt.title(str(b*1e6)+ r'$\pm$' +str(perr[1]*1e6))



plt.figure(2)
plt.plot(time_t2, phase_t2, 'r-o')
guess = [phase_t2[0]-phase_t2[-1], T2_guess, 0, phase_t2[-1]]
popt, pcov = curve_fit(func, time_t2*1e-9, phase_t2, guess)
a,b,c,d = popt #b is T1
time_nice  = np.linspace(0, pts_num*time_step, pts_num*100)
phase_fit = func(time_nice*1e-9, a, b, c, d)
perr = np.sqrt(abs(np.diag(pcov)))
plt.plot(time_nice, phase_fit)
plt.title(str(b*1e6)+ r'$\pm$' +str(perr[1]*1e6))

plt.show()