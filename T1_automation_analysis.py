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

# directory = 'G:\Projects\Fluxonium\Data\Summary of T1_T2_vs flux_Fluxonium#10\Automation code'
# fname = 'T1_rabi_44to45mA.csv'
# # fname ='dummy.csv'
# path_s = directory + '\\' + fname

#File path
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'T1_auto_38.5to38.6mA_1.h5'
path = directory + '\\' + measurement
# time_fname = 'T1_delays_35to36p1mA.txt'
# path_t = directory + '\\' + time_fname
t_inc = 10

#Read data and fit
time = np.linspace(0, 20*t_inc, 20)
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    # print count
    phase_raw = hf.get('demod_Phase0')
    freq_raw = np.array(hf.get('freq'))
    flux_raw = np.array(hf.get('flux'))
    total_count = len(flux_raw)
    T1 = []
    T1_error = []
    freq = []
    flux = []
    RabiA = []
    print 'Total points taken ' + str(total_count)
    for idx in range(total_count):
        phase = -phase_raw[idx, 0]
        phase = np.unwrap(phase)
        phase = phase - np.min(phase)
        phase = phase*180/np.pi
        guessA= phase[0]-phase[-1]
        # plt.plot(phase)
        # print freq_raw[idx]
        if guessA < 0.5 or guessA > 10:
            continue
        guess = [guessA, 20e-6, 0, 0]
        try:
            popt, pcov = curve_fit(func, time*1e-6, phase, guess)
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
        phase_fit = func(time*1e-6, a, b, c, d)
        perr = np.sqrt(abs(np.diag(pcov)))
        if b*1e6 < t_inc or b*1e6 > t_inc*19 or a < 0.5 or a > 10:# or perr[1]*1e6 > t_inc:
            continue
        T1_error = np.append(T1_error, perr[1]*1e6)
        T1 = np.append(T1, b*1e6) #T1 in us
        flux = np.append(flux, flux_raw[idx])
        freq = np.append(freq, freq_raw[idx])
        RabiA = np.append(RabiA, a)
        print b*1e6, perr[1]*1e6
        if b*1e6 > 20:
            plt.plot(time, phase, time, phase_fit)
            plt.title(str(b*1e6))
            plt.show()

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
# plt.show()