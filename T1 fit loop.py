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

directory = 'D:\Data\Fluxonium #10_7.5GHzCav\T1'
fname = 'T1_YOKO_28.575mA_Cav7.3649GHz_-15dBm_Qubit0.5046GHz_16dBm_PiPulse1320ns_Count20_TimeStep35000_loop_1000.h5'
path = directory + '\\' + fname
T1_array = []
T1_err_array = []
time = np.linspace(0,20*35000,20)

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    print phase_raw
    for idx in range(937):
        phase = phase_raw[idx, 0]
        phase = np.unwrap(phase)*180/np.pi
        phase = phase - np.min(phase)
        phase = abs(phase)

        guess = [phase[0]-phase[-1], 2e-4, 0, phase[-1]]
        try:
            popt, pcov = curve_fit(func, time*1e-9, phase, guess)
        except RuntimeError:
            print "Doesn't fit well entry " + str(idx)
            continue
        except RuntimeWarning:
            print "Doesn't fit well entry " + str(idx)
            continue
        except OptimizeWarning:
            print "Doesn't fit well entry " + str(idx)
            continue

        a,b,c,d = popt #b is T1
        time_nice = np.linspace(0,20*35000, 1000)
        phase_fit = func(time_nice*1e-9, a, b, c, d)
        perr = np.sqrt(abs(np.diag(pcov)))
        T1 = b*1e6
        T1_err = perr[1]*1e6
        T1_array = np.append(T1_array, T1)
        T1_err_array = np.append(T1_err_array, T1_err)
        # print T1
        # print T1_err

count = np.linspace(0, len(T1_array), len(T1_array))
plt.errorbar(count, T1_array, yerr=T1_err_array)
plt.show()