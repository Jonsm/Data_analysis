from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

def func(x,a,b,c,d):
    return a*np.cos(2*np.pi*b*(x-c)) + d
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Rabi'
# directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Raman'
fname = 'Rabi_YOKO_28.583mA_Cav7.3649GHz_-15dBm_Qubit0.5043GHz_25dBm_Count40_TimeStep100_Avg10001.h5'
path = directory + '\\' + fname
pts_num = 40
time_step = 100
time = np.linspace(0, pts_num*time_step, pts_num)

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    phase = phase_raw[0, 0]
    phase = np.unwrap(phase)*180/np.pi
    phase = phase - np.min(phase)
plt.plot(time, phase, '-o')

# guess = [np.max(phase) - np.min(phase), 0.5e6, 0, np.mean(phase)]
# popt, pcov = curve_fit(func, time*1e-9, phase, guess)
# a,b,c,d = popt #b is T1
# time_nice = np.linspace(0, pts_num*time_step, pts_num*100)
# phase_fit = func(time_nice*1e-9, a, b, c, d)
# perr = np.sqrt(abs(np.diag(pcov)))
# plt.plot(time_nice, phase_fit)


plt.grid()
plt.show()