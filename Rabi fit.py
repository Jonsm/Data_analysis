from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

from matplotlib import rc
plt.rc('font', family='serif')
# plt.figure(figsize = [10,7])
def func(x,a,b,c,d):
    return a*np.cos(2*np.pi*b*(x-c)) + d
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Rabi'
# directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Raman'
fname = '062517_Rabi_YOKO_24.49mA_Cav7.3644GHz_-7dBm_Qubit4.137GHz_25dBm_Count20_TimeStep50_Avg10000.h5'
path = directory + '\\' + fname
pts_num = 20
time_step = 50
time = np.linspace(0, pts_num*time_step, pts_num)

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    phase = phase_raw[0, 0]
    phase = np.unwrap(phase)*180/np.pi
    phase = phase - np.min(phase)
plt.plot(time, phase, '-o', color = 'r')

################################################################################################################
# guess = ([np.max(phase)-np.min(phase), 0.5/abs(time[np.argmax(phase)] - time[np.argmin(phase)]), 0, 0])
# opt,cov = curve_fit(func, time, phase, guess)
# time_nice = np.linspace(0, pts_num*time_step, pts_num*100)
# plt.plot(time_nice, func(time_nice, *opt))
# print ("Pi_pulse=" + str(abs(time_nice[np.argmin(func(time_nice, *opt))])))
# print ("Pi/2_pulse=" + str(abs(time_nice[np.argmin(func(time_nice, *opt))]/2.0)))
plt.show()