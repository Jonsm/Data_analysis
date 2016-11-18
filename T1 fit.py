from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


#File path
directory = 'D:\Data\Fluxonium #10_python code by Jon'
measurement = 't1_pulse_8.0647e9_823'
path = directory + '\\' + measurement

#Read data
time = np.genfromtxt(path + '_time.csv')
time = time[0::]

data = np.genfromtxt(path + '_phase.csv')
phase = data[0::] #phase is recorded in rad
phase = np.unwrap(phase)*180/np.pi
phase = -phase
phase = phase - min(phase)

###########################################################
# Curve fitting
###########################################################
def func(x, a, b, c, d):
    return a * np.exp(-(x-c)/b) + d

guessA= max(phase)-min(phase)

guess = [guessA, 1e-5, 0, 0]

popt, pcov = curve_fit(func, time*1e-9, phase, guess)

A = popt[0]
t_decay = popt[1]
t_delay = popt[2]
offset = popt[3]


print(popt)
print('T1=' + str(t_decay*1e6) + 'us')

fitphase =  A * np.exp(-(time*1e-9-t_delay)/t_decay) + offset

fig1=plt.figure(1)
plt.plot(time/1e6,phase, 'o')
plt.plot(time/1e6,fitphase)
plt.xlabel('Time(ms)')
plt.ylabel('Phase')
fig2 = plt.figure(2)
plt.plot(time/1e6,np.log(phase), 'o')
plt.plot(time/1e6, np.log(fitphase))
plt.xlabel('Time(ms)')
plt.ylabel('Phase')
plt.show()
