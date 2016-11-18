from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


#File path
directory = 'D:\\Data\\Fluxonium #10_python code by Jon'
measurement = 't2_pulse_2.0675e9_123'
path = directory + '\\' + measurement

#Read data
time = np.genfromtxt(path + '_time.csv')
time = time[1::]

data = np.genfromtxt(path + '_phase.csv')
phase = data[1::] #phase is recorded in rad
phase = np.unwrap(phase)*180/np.pi
phase = phase - np.mean(phase)


###########################################################
# Curve fitting
###########################################################
def func(x, a, b, c, d, g):
    return a *np.exp(-b*x)* np.cos(2*np.pi*c*((x-g))) + d

guess = [7.5, 0, 2e6, 0, 0]

popt, pcov = curve_fit(func, time*1e-9, phase, guess)

A = popt[0]
t_decay = popt[1]
Ramsey_f = popt[2]
offset = popt[3]
t_delay = popt[4]



print(popt)
print('Ramsey f = ' + str(Ramsey_f))
print('T2 ramsey = ' + str(1/t_decay) + 'sec')

fitphase = A *np.exp(-(t_decay)*time*1e-9)* np.cos(2*np.pi*Ramsey_f*(time*1e-9-t_delay)) + offset

plt.plot(time, phase, 'o', time, fitphase)
plt.xlabel('Time(ns)')
plt.ylabel('Phase')
plt.show()