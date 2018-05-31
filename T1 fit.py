from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

def func(x, a, b, c, d):
    return a*np.exp(-(x-c)/b) + d

directory = 'D:\Data\Fluxonium #23\T1'
fname = '053018_T1_YOKO_1.188mA_Cav7.5613GHz_-20dBm_Qubit0.6343GHz_25dBm_PiPulse514ns_Count25_TimeStep20000.h5'
path = directory + '\\' + fname
pts_num = 25
time_step = 20000
t1_guess = 100e-6
time = np.linspace(0, (pts_num)*time_step, pts_num)

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    # print phase_raw
    phase = phase_raw[0, 0][0:]
    phase = np.unwrap(phase)*180/np.pi
    phase = phase - np.min(phase)
    phase = abs(phase[0::])
plt.figure(1)
plt.plot(time*1e-3, phase, 'd-')
#
guess = [phase[0]-phase[-1], t1_guess, 0, phase[-1]]
popt, pcov = curve_fit(func, time*1e-9, phase, guess)
a,b,c,d = popt #b is T1
time_nice = np.linspace(0, pts_num*time_step, (pts_num-1)*100)
phase_fit = func(time_nice*1e-9, a, b, c, d)
perr = np.sqrt(abs(np.diag(pcov)))
plt.plot(time_nice*1e-3, phase_fit)
plt.title(str( b*1e6)+ r'$\pm$' +str(perr[1]*1e6))
plt.tick_params(labelsize = 18.0)

# plt.figure(2)
# plt.semilogy(time*1e-3, phase, 'd-')
# plt.semilogy(time_nice*1e-3, phase_fit)
# plt.title(str( b*1e6)+ r'$\pm$' +str(perr[1]*1e6))
# plt.tick_params(labelsize = 18.0)
plt.show()
