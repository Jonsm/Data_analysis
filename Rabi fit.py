from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


#File path
directory = 'D:\\Data\\Fluxonium #10_python code by Jon'
measurement = 'rabi_pulse_5.7137e9_833'
path = directory + '\\' + measurement

#Read data
time = np.genfromtxt(path + '_time.csv')
time = time[1::]

data = np.genfromtxt(path + '_phase.csv')
phase = data[1::] #phase is recorded in rad
phase = np.unwrap(phase)*180/np.pi
#phase = phase - np.mean(phase)


###########################################################
# Curve fitting
###########################################################
def func(x, a, b, c, d, g):
    return a *np.exp(-b*x)* np.cos(2*np.pi*c*((x-g))) + d

guessA= max(phase)-min(phase)

guess = [guessA, 0, 1e6, 0, 0]

popt, pcov = curve_fit(func, time*1e-9, phase, guess)

A = popt[0]
t_decay = popt[1]
Rabi_f = popt[2]
offset = popt[3]
t_delay = popt[4]

pi_pulse = (1/Rabi_f)/2

print(popt)
print('Rabi A = ' + str(A))
print('Rabi f = ' + str(Rabi_f))
print('Pi pulse = ' + str(pi_pulse*1e9) + 'ns')

fitphase = A *np.exp(-t_decay*time*1e-9)* np.cos(2*np.pi*Rabi_f*(time*1e-9-t_delay)) + offset

plt.plot(time, phase, 'o', time, fitphase)
#plt.plot(time, phase, 'o')
plt.xlabel('Time(ns)')
plt.ylabel('Phase')
plt.show()