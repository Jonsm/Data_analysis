from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit
from scipy.optimize import OptimizeWarning
import warnings
warnings.simplefilter("error", OptimizeWarning)
warnings.simplefilter("error", RuntimeWarning)

def func(x, a, b, c, d, g):
    return a*np.exp(-x/b)*np.cos(2*np.pi*c*((x-g))) + d

directory = 'D:\Data\Fluxonium #10_7.5GHzCav\T2R'
fname = '062217_T2R_YOKO_24.49mA_Cav7.3644GHz_-7dBm_Qubit4.1335GHz_25dBm_PiPulse420ns_Count40_TimeStep20.h5'
path = directory + '\\' + fname
T2_array = []
T2_err_array = []
fR_array = []
fR_err_array = []
pts_num = 40
time_step = 20
t2_guess = 1e-6
f2_guess = 2e6
time = np.linspace(0, pts_num*time_step, pts_num)
time_nice = np.linspace(0, pts_num*time_step, pts_num*100)
loop_count = 90
#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
   # print phase_raw
    for idx in range(loop_count):
        phase = phase_raw[idx, 0]
        phase = np.unwrap(phase)*180/np.pi
        phase = phase - np.min(phase)
        phase = abs(phase)
        guess = [np.max(phase) - np.min(phase), t2_guess, f2_guess, 0, 0]
        try:
            popt, pcov = curve_fit(func, time*1e-9, phase, guess)
        except RuntimeError:
            print ("Doesn't fit well entry " + str(idx))
            continue
        except RuntimeWarning:
            print ("Doesn't fit well entry " + str(idx))
            continue
        except OptimizeWarning:
            print ("Doesn't fit well entry " + str(idx))
            continue

        a,b,c,d,g = popt #b is T2, c is fR

        phase_fit = func(time_nice*1e-9, a, b, c, d, g)
        perr = np.sqrt(abs(np.diag(pcov)))
        T2 = b*1e6
        T2_err = perr[1]*1e6
        fR = c*1e-3 #in kHz
        fR_err = perr[2]*1e-3
        if T2 < time_step*1e-3:
            continue
        T2_array = np.append(T2_array, T2)
        T2_err_array = np.append(T2_err_array, T2_err)
        fR_array = np.append(fR_array, fR)
        fR_err_array = np.append(fR_err_array, fR_err)
        plt.figure(1)
        plt.plot(time, phase, 'g-o', alpha = 0.25)
        plt.plot(time_nice, phase_fit, 'k-')
        # print T2
        # print T2_err

count = np.linspace(0, len(T2_array), len(T2_array))
plt.figure(2)
plt.errorbar(count, T2_array, yerr=T2_err_array, fmt = 'h', mfc = 'none', mew = 2.0, mec = 'y', ecolor = 'y')
plt.figure(3)
plt.errorbar(count, fR_array, yerr=fR_err_array, fmt = 'h', mfc = 'none', mew = 2.0, mec = 'k', ecolor = 'k')
plt.show()