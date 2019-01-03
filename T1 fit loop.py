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

directory = 'D:\Data\Julius II\T1'
fname = '101118_T1_YOKO_1.64mA_Cav7.507GHz_-30dBm_Qubit0.3217GHz_0dBm_PiPulse191ns_Count20_TimeStep35000_loop_5.h5'
path = directory + '\\' + fname
T1_array = []
T1_err_array = []
pts_num = 20
time_step = 35000
loop_count = 6
t1_guess = 50e-6
time = np.linspace(0, pts_num*time_step, pts_num)
phase_avg = np.zeros(pts_num)
#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    for idx in range(loop_count):
        phase = phase_raw[idx, 0]
        phase = np.unwrap(phase)*180/np.pi
        phase = phase - np.min(phase)
        # phase = abs(phase)
        # plt. plot(phase)
        guess = [phase[0]-phase[-1], t1_guess, 0, phase[-1]]
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
        plt.figure(1)
        plt.tick_params(labelsize = 18.0)
        a,b,c,d = popt #b is T1
        time_nice = np.linspace(0, pts_num*time_step, pts_num*100)
        phase_fit = func(time_nice*1e-9, a, b, c, d)
        perr = np.sqrt(abs(np.diag(pcov)))
        T1 = b*1e6
        T1_err = perr[1]*1e6
        if T1_err > T1/2:
            continue
        T1_array = np.append(T1_array, T1)
        T1_err_array = np.append(T1_err_array, T1_err)
        plt.plot(time*1e-3,phase, 'b-o', alpha = 0.25)
        phase_avg = phase_avg + phase
        plt.plot(time_nice*1e-3, phase_fit, 'k-')

count = np.linspace(0, len(T1_array), len(T1_array))
plt.figure(2)
plt.errorbar(count, T1_array, yerr=T1_err_array, fmt = 's', mfc = 'none', mew = 2.0, mec = 'b', ecolor = 'b')
plt.ylim([0,300])
plt.tick_params(labelsize = 18.0)
print(T1_array)
##########################################
#Fit average

plt.figure(3)
phase_avg = phase_avg / loop_count
guess = [phase_avg [0]-phase_avg [-1], t1_guess, 0, phase_avg [-1]]
popt, pcov = curve_fit(func, time*1e-9, phase_avg, guess)
a,b,c,d = popt #b is T1
plt.plot(time*1e-3,phase_avg , 'b-o', alpha = 0.25)
phase_fit = func(time_nice*1e-9, a, b, c, d)
perr = np.sqrt(abs(np.diag(pcov)))
plt.plot(time_nice*1e-3, phase_fit, 'k-')
plt.tick_params(labelsize = 18.0)
plt.title ("Average T1 is "+str(b*1e6) +" +- " +str(perr[1]*1e6) +" us")

#########################################
plt.grid()
plt.show()