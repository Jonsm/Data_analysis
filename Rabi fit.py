from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

from matplotlib import rc
plt.rc('font', family='serif')
# plt.figure(figsize = [10,7])
def func(x,a,b,c,d,t2):
    return a*np.cos(2*np.pi*b*(x-c))*np.exp(-x/t2) + d
directory = 'D:\Data\Fluxonium #22\Rabi'
fname = '020418_Rabi_YOKO_90.604mA_Cav7.3262GHz_-15dBm_Qubit0.17286GHz_25dBm_Count20_TimeStep300_Avg20000.h5'
path = directory + '\\' + fname
pts_num = 20
time_step = 300
time = np.linspace(0, pts_num*time_step, pts_num)

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    phase = phase_raw[0, 0]
    phase = np.unwrap(phase)*180/np.pi
    phase = phase - np.min(phase)
plt.plot(time, phase, '-d')

################################################################################################################
guess = ([np.max(phase)-np.min(phase), 0.5/abs(time[np.argmax(phase)] - time[np.argmin(phase)]), 0, 0, 1.6e3])
opt,cov = curve_fit(func, time, phase, guess)
time_nice = np.linspace(0, pts_num*time_step, pts_num*100)
plt.plot(time_nice, func(time_nice, *opt), linewidth = 2.0)
pi_p = abs(time_nice[np.argmax(func(time_nice, *opt))])
rabi_amp = abs(opt[0])
print ("Pi_pulse=" + str(pi_p))
print ("Pi/2_pulse=" + str(pi_p/2.0))

plt.title("Pi_pulse=" + str(pi_p) + '\n' +
          # "Pi/2_pulse=" + str(pi_p/2.0) + '\n'+
          "Rabi_amplitude=" + str(rabi_amp))

plt.tick_params(labelsize = 18.0)


plt.tick_params(labelsize = 18.0)
plt.show()