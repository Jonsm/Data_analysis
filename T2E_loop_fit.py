from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit
from scipy.optimize import OptimizeWarning
import warnings
warnings.simplefilter("error", OptimizeWarning)
warnings.simplefilter("error", RuntimeWarning)

def func(x, a, b, c, d):
    return a*np.exp(-(x-c)/b) + d

directory = 'D:\Data\Fluxonium #23\T2E'
fname = '061918_T2ELoop_YOKO_119.083mA_Cav7.5612GHz_0dBm_Qubit0.6276GHz_25dBm_PiPulse460ns_Count20_TimeStep18000_loop_20.h5'
path = directory + '\\' + fname
T2_array = []
T2_err_array = []
pts_num = 20
time_step = 18000
t2_guess = 90e-6
time = np.linspace(0, pts_num*time_step, pts_num)
time_nice = np.linspace(0, pts_num*time_step, pts_num*100)
loop_count = 10
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
        guess = [phase[0]-phase[-1], t2_guess, 0, phase[-1]]
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

        a,b,c,d = popt #b is T1

        phase_fit = func(time_nice*1e-9, a, b, c, d)
        perr = np.sqrt(abs(np.diag(pcov)))
        T2 = b*1e6
        T2_err = perr[1]*1e6
        # if T2 < time_step*1e-3 or T2 > 10e5:
        #     continue

        T2_array = np.append(T2_array, T2)
        T2_err_array = np.append(T2_err_array, T2_err)
        plt.figure(1)
        plt.tick_params(labelsize = 18.0)
        plt.plot(time*1e-3, phase, 'g-o', alpha = 0.25)
        plt.plot(time_nice*1e-3, phase_fit, 'k-')
        # print T2
        # print T2_err

count = np.linspace(0, len(T2_array), len(T2_array))
plt.figure(2)
plt.ylim([0,150])
plt.errorbar(count, T2_array, yerr=T2_err_array, fmt = 'h', mfc = 'none', mew = 2.0, mec = 'g', ecolor = 'g')
plt.tick_params(labelsize = 18.0)

T2_avg = np.average(T2_array)

print('Mean T2e=' + str(T2_avg) + '+-' + str(np.average(T2_err_array)))


plt.show()