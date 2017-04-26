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
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\T1'
measurement = '042117_T1_auto_28.45to28.6mA_Cavity_7.3649GHz_-15dBm_Qubit5dBm_Count30_TimeStep20000_Average10000.h5'
path = directory + '\\' + measurement
pts_num = 30
time_step = 20000
T1_guess = 100e-6
time = np.linspace(0, pts_num*time_step, pts_num)
time_nice = np.linspace(0, pts_num*time_step, pts_num*100)

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
    print 'Total points taken ' + str(total_count)
    for idx in range(total_count):
        phase = -phase_raw[idx, 0]
        phase = np.unwrap(phase)
        phase = phase - np.min(phase)
        phase = phase*180/np.pi
        guessA= phase[0]-phase[-1]
        # plt.plot (time, phase)
        if guessA < 0.01:
            print "Cannot fit entry " + str(idx)
            continue
        guess = [guessA, T1_guess, 0, 0]
        try:
            popt, pcov = curve_fit(func, time*1e-9, phase, guess)
        except RuntimeError:
            print "Cannot fit entry " + str(idx)
            continue
        except OptimizeWarning:
            print "Doesn't fit well entry " + str(idx)
            continue
        except RuntimeWarning:
            print "Doesn't fit well entry " + str(idx)
            continue
        a,b,c,d = popt #b is T1
        phase_fit = func(time_nice*1e-9, a, b, c, d)
        perr = np.sqrt(abs(np.diag(pcov)))
        T1 = b*1e6
        T1_error = perr[1]*1e6
        if T1 < time_step/1e3 or T1 > time_step/1e3*pts_num or a < 0.01:
            continue
        T1_array = np.append(T1_array, T1)
        T1_error_array = np.append(T1_error_array, T1_error)
        # plt.plot(time, phase)
        plt.plot(time_nice, phase_fit)

    #     flux = np.append(flux, flux_raw[idx])
    #     freq = np.append(freq, freq_raw[idx])
    #     RabiA = np.append(RabiA, a)
    #     print b*1e6, perr[1]*1e6
    #     if b*1e6 > 20:
    #         plt.plot(time, phase, time, phase_fit)
    #         plt.title(str(b*1e6))
    #         plt.show()

# plt.plot(T1, 'r.')
# directory = 'G:\Projects\Fluxonium\Data\Summary of T1_T2_vs flux_Fluxonium#10\Automation code'
# fname = 'T1_rabi_38p5to38p6mA.csv'
# # fname ='dummy.csv'
# path = directory + '\\' + fname
# file = np.zeros((len(flux),4))
# file[:,0] = flux
# file[:,1] = freq
# file[:,2] = T1
# file[:,3] = RabiA
# print 'pts fitted well ' + str(len(T1))
# #Check
# np.savetxt(path_s, file)
# data = np.genfromtxt(path_s)
# plt.show()
# plt.plot(data[:,0], data[:,2], 'ro')
plt.show()