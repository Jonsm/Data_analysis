from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

from matplotlib import rc
plt.rc('font', family='serif')
# plt.figure(figsize = [10,7])
def func(x,a,b,c,d,t2):
    return a*np.cos(2*np.pi*b*(x-c))*np.exp(-x/t2) + d
directory = 'D:\Data\Fluxonium #23\Rabi'
fname = '061418_Rabi_YOKO_91.259mA_Cav7.5612GHz_0dBm_Qubit0.63027GHz_25dBm_Count20_TimeStep70_Avg20000.h5'
path = directory + '\\' + fname
pts_num = 20
time_step = 70
time = np.linspace(0, pts_num*time_step, pts_num)

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    phase = phase_raw[0, 0]
    phase = phase*180/np.pi
    # phase = np.unwrap(phase)*180/np.pi
    phase = phase - np.min(phase)
plt.plot(time, phase, '-d')
# '''
#######################################################################################################
guess = ([np.max(phase)-np.min(phase), 0.5/abs(time[np.argmax(phase)] - time[np.argmin(phase)]), 0, phase[1], 1e3])
opt,cov = curve_fit(func, time, phase, guess)
err = np.sqrt(abs(np.diag(cov)))
time_nice = np.linspace(0, pts_num*time_step, pts_num*100)
plt.plot(time_nice, func(time_nice, *opt), linewidth = 2.0)
pi_p = 1.0/opt[1]/2
rabi_amp = abs(opt[0])
print ("Pi_pulse=" + str(pi_p))
print ("Pi/2_pulse=" + str(pi_p/2.0))
#
plt.title("Pi_pulse=" + str(pi_p) + '\n' +
          # "Pi/2_pulse=" + str(pi_p/2.0) + '\n'+
          "Rabi_amplitude=" + str(rabi_amp) +" +/- "+str(err[0]))
# '''


plt.tick_params(labelsize = 12.0)
plt.ylabel('Phase',size = 12)
plt.xlabel('ns',size = 12)
plt.show()