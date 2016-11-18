from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


#File path
directory = 'D:\Data\Fluxonium #10_python code by Jon'
measurement = 't1_pulse_7.9597e9_815'

path = directory + '\\' + measurement

for i in range(1, 10):
    #Read data
    time = np.genfromtxt(path + '_time' + str(i) + '.csv')
    time = time[0::]

    data = np.genfromtxt(path + '_phase' + str(i) + '.csv')
    phase = data[0::] #phase is recorded in rad
    phase = np.unwrap(phase)*180/np.pi
    # phase = -phase
    # phase = phase - np.min(phase)
    if i ==4:
        continue
    if i == 1:
        phaseall = phase
    else:
        phaseall= phaseall + phase

###########################################################
#   average phase
###########################################################
phaseall = -phaseall
phaseall = phaseall-np.min(phaseall)
phaseall = phaseall/9

print(phaseall)
###########################################################
# Curve fitting
###########################################################
def func(x, a, b, c, d):
    return a*np.exp(-(x-c)/b) + d

guessA= max(phaseall)-min(phaseall)

guess = [guessA, 2e-4, 0, 0]

popt, pcov = curve_fit(func, time*1e-9, phaseall, guess)

A = popt[0]
t_decay = popt[1]
t_delay = popt[2]
offset = popt[3]

perr = np.diag(pcov)


print(popt)
#print(np.diag(pcov))
print('T1=' + str(t_decay*1e6) + 'us')
print('T1 error=' + str(np.sqrt(perr[1])*1e6)+ 'us')

fitphase = A*np.exp(-(time*1e-9-t_delay)/t_decay) + offset
fig1 = plt.figure(1)
plt.plot(time/1e6, phaseall, 'o', time/1e6, fitphase)
plt.xlabel('Time(ms)')
plt.ylabel('Phase')
fig2 = plt.figure(2)
plt.semilogy(time/1e6, phaseall, 'o', time/1e6, fitphase)
plt.xlabel('Time(ms)')
plt.ylabel('Phase')
plt.show()

