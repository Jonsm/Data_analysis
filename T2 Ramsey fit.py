from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

directory = 'D:\Data\Fluxonium #10_7.5GHzCav\T2R'
fname = '062217_T2R_YOKO_24.49mA_Cav7.3644GHz_-7dBm_Qubit4.1335GHz_25dBm_PiPulse420ns_Count20_TimeStep20.h5'
path = directory + '\\' + fname
pts_num = 20
time_step = 20
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

plt.plot(time, phase, '-o')
###########################################################
# Curve fitting
###########################################################
def func(x, a, b, c, d, g):
    return a*np.exp(-x/b)*np.cos(2*np.pi*c*((x-g))) + d

guess = [np.max(phase) - np.min(phase), 2e-6, 2e6, 0, 0]

popt, pcov = curve_fit(func, time*1e-9, phase, guess)

a,b,c,d,g = popt
time_nice  = np.linspace(0, pts_num*time_step, pts_num*100) #ns
phase_fit = func(time_nice*1e-9, a, b, c, d, g)
perr = np.sqrt(abs(np.diag(pcov)))
T2 = b*1e6 #us
T2_err = perr[1]*1e6 #us
f_R = c/1e6 #MHz
plt.plot(time_nice, phase_fit, linewidth = 2.0)

plt.xlabel('Time(ns)')
plt.ylabel('Phase')
plt.title('T2 Ramsey=' + str(T2) + '+/-' + str(T2_err) + 'us, f_R=' + str(f_R) + 'MHz')
plt.show()