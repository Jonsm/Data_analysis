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
fname = '042017_Rabi3ToneA_YOKO_28.53mA_Cav7.3649GHz_-15dBm_Qubit0.50425GHz_25dBm_Qubit125.49GHz_25dBm_Count20_TimeStep20_Avg100000.h5'
path = directory + '\\' + fname
pts_num = 20
time_step = 20
time = np.linspace(0, pts_num*time_step, pts_num)

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    phase = phase_raw[0, 0]
    phase = np.unwrap(phase)*180/np.pi
    phase = phase - np.mean(phase)
plt.plot(time, phase, '-o', color = 'r')
#

fname = '042017_Rabi3ToneB_YOKO_28.53mA_Cav7.3649GHz_-15dBm_Qubit0.50425GHz_25dBm_Qubit125.49GHz_25dBm_Count20_TimeStep20_Avg100000.h5'
path = directory + '\\' + fname
pts_num = 20
time_step = 20
time = np.linspace(0, pts_num*time_step, pts_num)

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    phase = phase_raw[0, 0]
    phase = np.unwrap(phase)*180/np.pi
    phase = phase - np.mean(phase)
plt.plot(time, phase, '-o', color = 'b')
# guess = [np.max(phase) - np.min(phase), 5e6, 0, np.mean(phase)]
# popt, pcov = curve_fit(func, time*1e-9, phase, guess)
# a,b,c,d = popt #b is T1
# time_nice = np.linspace(0, pts_num*time_step, pts_num*100)
# phase_fit = func(time_nice*1e-9, a, b, c, d)
# perr = np.sqrt(abs(np.diag(pcov)))
# plt.plot(time_nice, phase_fit)
# plt.title(str(b/1e6))

# plt.grid()
plt.tick_params(labelsize = 18.0)
plt.xticks(np.linspace(0,400,5))
plt.ylim([-0.3,0.3])
plt.show()