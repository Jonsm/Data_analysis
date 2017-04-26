from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

def func(x, a, b, c, d):
    return a*np.exp(-(x-c)/b) + d

#################################################################################################################
#Parameters
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\T2E'
fname = '042117_T1T2ET2R_loop_YOKO_28.53mA_Cav7.3649GHz_-15dBm_Qubit0.50425GHz_25dBm__PiPulse930ns_Count20_TimeStep20000.h5'
path = directory + '\\' + fname
pts_num = 20
time_step = 20000
T1_guess = 200e-6
T2e_guess = 100e-6
#################################################################################################################
time_t2e = np.linspace(0, pts_num*time_step, pts_num)
time_t1 = np.linspace(0, pts_num*time_step*1.75, pts_num)
time_t2r = np.linspace(0, pts_num*time_step*0.08, pts_num)

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    # print phase_raw
    phase = phase_raw[0, 0]
    phase_t1 = phase[0::3]
    phase_t2e = phase[1::3]
    phase_t2r = phase[2::3]
    phase_t1 = np.unwrap(phase_t1)*180/np.pi
    phase_t1 = phase_t1 - np.min(phase_t1)
    phase_t1 = abs(phase_t1)

    phase_t2r = np.unwrap(phase_t2r)*180/np.pi
    phase_t2r = phase_t2r - np.min(phase_t2r)
    phase_t2r = abs(phase_t2r)

    phase_t2e = np.unwrap(phase_t2e)*180/np.pi
    phase_t2e = phase_t2e - np.min(phase_t2e)
    phase_t2e = abs(phase_t2e)

plt.figure(1)
plt.plot(time_t1, phase_t1, 'b-o')
guess = [phase_t1[0]-phase_t1[-1], T1_guess, 0, phase_t1[-1]]
popt, pcov = curve_fit(func, time_t1*1e-9, phase_t1, guess)
a,b,c,d = popt #b is T1
time_nice  = np.linspace(0, pts_num*time_step*1.75, pts_num*100)
phase_fit = func(time_nice*1e-9, a, b, c, d)
perr = np.sqrt(abs(np.diag(pcov)))
plt.plot(time_nice, phase_fit)
plt.title(str(b*1e6)+ r'$\pm$' +str(perr[1]*1e6))



plt.figure(2)
plt.plot(time_t2e, phase_t2e, 'g-o')
guess = [phase_t2e[0]-phase_t2e[-1], T2e_guess, 0, phase_t2e[-1]]
popt, pcov = curve_fit(func, time_t2e*1e-9, phase_t2e, guess)
a,b,c,d = popt #b is T1
time_nice  = np.linspace(0, pts_num*time_step, pts_num*100)
phase_fit = func(time_nice*1e-9, a, b, c, d)
perr = np.sqrt(abs(np.diag(pcov)))
plt.plot(time_nice, phase_fit)
plt.title(str(b*1e6)+ r'$\pm$' +str(perr[1]*1e6))

plt.figure(3)
plt.plot(time_t2r, phase_t2r, 'r-o')

plt.show()