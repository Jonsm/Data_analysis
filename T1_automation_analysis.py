from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit
import warnings
from scipy.optimize import OptimizeWarning
warnings.simplefilter("error", OptimizeWarning)
warnings.simplefilter("error", RuntimeWarning)

def func(x, a, b, c, d):
    return a*np.exp(-(x-c)/b) + d

#File path
directory = 'D:\Data\Fluxonium #13\T1'
measurement = '083017_T1_auto_input_31.07to31.41mA_Cavity_7.36923GHz_-30dBm_Qubit15dBm_Count50_TimeStep5000_Average10000.h5'
path = directory + '\\' + measurement
pts_num = 50
time_step = 5000
T1_guess = 50e-6
time = np.linspace(0, pts_num*time_step, pts_num)
time_nice = np.linspace(0, pts_num*time_step, pts_num*100)
plt.figure(1)
#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    # print count
    phase_raw = hf.get('PHASEMAG_Phase0')
    freq_raw = np.array(hf.get('FREQ'))
    current_raw = np.array(hf.get('CURRENT'))
    plt.plot(current_raw, freq_raw)
    total_count = len(current_raw)
    T1_array = []
    T1_error_array = []
    freq_array = []
    current_array = []
    print ('Total points taken ' + str(total_count))
    for idx in range(total_count):
        phase = phase_raw[idx, 0]
        phase = np.unwrap(phase)
        phase = phase - np.min(phase)
        phase = phase*180/np.pi
        guessA = np.max(phase) - np.min(phase)
        # plt.plot (time, phase)
        if guessA < 1:
            print ("Cannot fit entry " + str(idx))
            continue
        guess = [guessA, T1_guess, 0, 0]
        try:
            popt, pcov = curve_fit(func, time*1e-9, phase, guess)
        except RuntimeError:
            print ("Cannot fit entry " + str(idx))
            continue
        except OptimizeWarning:
            print ("Doesn't fit well entry " + str(idx))
            continue
        except RuntimeWarning:
            print ("Doesn't fit well entry " + str(idx))
            continue
        a,b,c,d = popt #b is T1
        phase_fit = func(time_nice*1e-9, a, b, c, d)
        perr = np.sqrt(abs(np.diag(pcov)))
        T1 = b*1e6
        T1_error = perr[1]*1e6
        if T1 < time_step/1e3 or T1 > time_step/1e3*pts_num:
            continue
        if T1_error > time_step/1e3*3:
            continue
        T1_array = np.append(T1_array, T1)
        T1_error_array = np.append(T1_error_array, T1_error)
        plt.plot(time, phase, 'k-.', alpha = 0.2)
        plt.plot(time_nice, phase_fit)

        current_array = np.append(current_array, current_raw[idx])
        freq_array = np.append(freq_array, freq_raw[idx])
        # RabiA = np.append(RabiA, a)
        # print b*1e6, perr[1]*1e6
        # if b*1e6 > 20:
        #     plt.plot(time, phase, time, phase_fit)
        #     plt.title(str(b*1e6))
        #     plt.show()

plt.figure(2)
plt.errorbar(current_array, T1_array, yerr=T1_error_array, fmt = 's', mfc = 'none', mew = 2.0, mec = 'b', ecolor = 'b')

fname = 'T1_auto_31.07to31.41mA.csv'
path = directory + '\\' + fname
file = np.zeros((len(current_array),4))
file[:,0] = current_array
file[:,1] = freq_array
file[:,2] = T1_array
file[:,3] = T1_error_array
print ('pts fitted well ' + str(len(T1_array)))
np.savetxt(path, file)
plt.show()