from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


#File path
directory = 'D:\Data\Fluxonium #10_python code by Jon'
measurement = 't2_echo_pulse_5.7208e9_770'
path = directory + '\\' + measurement

#Read data
time = np.genfromtxt(path + '_time.csv')
time = time[0::]

data = np.genfromtxt(path + '_phase.csv')
phase = data[0::] #phase is recorded in rad
phase = np.unwrap(phase)*180/np.pi
phase = phase - np.mean(phase)


###########################################################
# Curve fitting
###########################################################
def func(x, a, b, c, d):
    return a * (1 - np.exp(-(x-c)/b)) + d

guessA= max(phase)-min(phase)

guess = [guessA,1e-4, 0, 0]

popt, pcov = curve_fit(func, time*1e-9, phase, guess)

A = popt[0]
t_decay = popt[1]
t_delay = popt[2]
offset = popt[3]


print(popt)
print('T2_echo=' + str(t_decay))

fitphase = (A * (1 - np.exp(-(time*1e-9-t_delay)/t_decay)) + offset)

phase = phase

plt.plot(time, phase, 'o', time, fitphase)
plt.xlabel('Time(ns)')
plt.ylabel('Phase')
plt.show()