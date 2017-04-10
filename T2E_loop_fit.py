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

directory = 'D:\Data\Fluxonium #10_7.5GHzCav\T2E'
fname = 'T2ELoop_YOKO_28.583mA_Cav7.3649GHz_-15dBm_Qubit0.5041GHz_25dBm_PiPulse800ns_Count20_TimeStep20000_loop_1000.h5'
path = directory + '\\' + fname
T2_array = []
T2_err_array = []
time = np.linspace(0,20*20000,20)

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    print phase_raw
    for idx in range(41):
        phase = phase_raw[idx, 0]
        phase = np.unwrap(phase)*180/np.pi
        phase = phase - np.min(phase)
        phase = abs(phase)
        # plt.plot(time, phase)

        guess = [phase[0]-phase[-1], 100e-6, 0, phase[-1]]
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
        time_nice = np.linspace(0,20*20000, 1000)
        phase_fit = func(time_nice*1e-9, a, b, c, d)
        perr = np.sqrt(abs(np.diag(pcov)))
        T2 = b*1e6
        T2_err = perr[1]*1e6
        if T2 < 20:
            continue
        T2_array = np.append(T2_array, T2)
        T2_err_array = np.append(T2_err_array, T2_err)
        # print T2
        # print T2_err

count = np.linspace(0, len(T2_array), len(T2_array))
plt.errorbar(count, T2_array, yerr=T2_err_array)
plt.show()