
from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit
import warnings
from scipy.optimize import OptimizeWarning
warnings.simplefilter("error", OptimizeWarning)

def func(x, a, b, c, d):
    return a*np.exp(-(x-c)/b) + d

#File path
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'T1_auto_35to36p1mA_1.h5'
path = directory + '\\' + measurement
# time_fname = 'T1_delays_35to36p1mA.txt'
# path_t = directory + '\\' + time_fname

#Read data and fit
time = np.linspace(0, 20*3, 20)
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    print count
    phase_raw = hf.get('demod_Phase0')
    freq_raw = np.array(hf.get('freq'))
    flux_raw = np.array(hf.get('flux'))
    total_count = len(flux_raw)
    T1 = []
    freq = []
    flux = []
    for idx in range(total_count):
        phase = -phase_raw[idx, 0]
        phase = np.unwrap(phase)
        phase = phase - np.mean(phase)
        phase = phase*180/np.pi
        guessA= phase[0]-phase[-1]
        if guessA < 1.0:
            continue
        guess = [guessA, 5e-6, 0, 0]
        try:
            popt, pcov = curve_fit(func, time*1e-6, phase, guess)
        except RuntimeError:
            print "Cannot fit entry " + str(idx)
            continue
        except OptimizeWarning:
            print "Doesn't fit well entry " + str(idx)
            continue
        a,b,c,d = popt #b is T1
        phase_fit = func(time*1e-6, a, b, c, d)
        T1=np.append(T1, b*1e6) #T1 in us
        flux = np.append(flux, flux_raw[idx])
        freq = np.append(freq, freq_raw[idx])
        # plt.plot(time, phase, time, phase_fit)


directory = 'G:\Projects\Fluxonium\Data\Summary of T1_T2_vs flux_Fluxonium#10\Automation code'
fname = 'T1_auto_35to36p1mA.csv'
path = directory + '\\' + fname
file = np.zeros((len(T1),3))
file[:,0] = flux
file[:,1] = freq
file[:,2] = T1
print len(T1)
#Check
np.savetxt(path, file)
data = np.genfromtxt(path)
plt.plot(data[:,0], data[:,2], 'ro')
plt.show()