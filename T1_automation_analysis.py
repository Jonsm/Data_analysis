
from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

def func(x, a, b, c, d):
    return a*np.exp(-(x-c)/b) + d

#File path
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'T1_auto3.h5'
path = directory + '\\' + measurement
# time_fname = 'T1_delays_35to36p1mA.txt'
# path_t = directory + '\\' + time_fname

#Read data and fit
time = np.linspace(0, 20*10, 20)
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    print count
    phase_raw = hf.get('demod_Phase0')
    freq = np.array(hf.get('freq'))
    flux = np.array(hf.get('flux'))
    total_count = len(flux)
    T1 = np.zeros(total_count)
    for idx in range(total_count):
        phase = -phase_raw[idx,0]
        phase = np.unwrap(phase)
        phase = phase - np.mean(phase)
        phase = phase*180/np.pi
        guessA= max(phase)-min(phase)
        guess = [guessA, 2e-6, 0, 0]
        popt, pcov = curve_fit(func, time*1e-6, phase, guess)
        a,b,c,d = popt #b is T1
        phase_fit = func(time*1e-6, a, b, c, d)
        T1[idx]=b*1e6 #T1 in us

directory = 'D:\Data\Summary'
fname = 'T1_auto_44to45mA.csv'
path = directory + '\\' + fname
file = np.zeros((total_count,3))
file[:,0] = flux
file[:,1] = freq
file[:,2] = T1

#Check
np.savetxt(path, file)
data = np.genfromtxt(path)
plt.plot(data[:,0], data[:,2], 'ro')
plt.show()
