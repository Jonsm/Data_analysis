from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


#File path
directory = 'D:\Data\Fluxonium #10_python code by Jon'
measurement = 't1_pulse_3.693e9_659'
flux = 38.69
qubitfreq = 3.693e9
path = directory + '\\' + measurement

T1fits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fluxes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
qubitf = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 10):
    #Read data
    time = np.genfromtxt(path + '_time' + str(i) + '.csv')
    time = time[1::]

    data = np.genfromtxt(path + '_phase' + str(i) + '.csv')
    phase = data[1::] #phase is recorded in rad
    phase = np.unwrap(phase)*180/np.pi
    phase = phase - np.mean(phase)
    ###########################################################
    # Curve fitting
    ###########################################################
    def func(x, a, b, c, d):
        return a * (1 - np.exp(-(x-c)/b)) + d

    guessA= max(phase)-min(phase)
    guess = [guessA, 1e-3, 0, 0]

    popt, pcov = curve_fit(func, time*1e-9, phase, guess)

    A = popt[0]
    t_decay = popt[1]
    t_delay = popt[2]
    offset = popt[3]


    print(popt)
    print('T1=' + str(t_decay))
    T1fits[i]=t_decay
    fluxes[i]=flux
    qubitf[i]=qubitfreq

    fitphase = - (A * (1 - np.exp(-(time*1e-9-t_delay)/t_decay)) + offset)

    phase = - phase

    plt.plot(time, phase, 'o', time, fitphase)
    plt.xlabel('Time(ns)')
    plt.ylabel('Phase')
    plt.show()

AvgT1 = np.average(T1fits)
# T1fits = np.transpose(T1fits)
# fluxes = np.transpose(fluxes)
# qubitf = np.transpose(qubitf)
print(T1fits)
print(AvgT1)
np.savetxt(path + "fit.csv", np.transpose([T1fits, fluxes, qubitf]), delimiter=",", header="T1(s), YOKO(mA), Qubit f(Hz)", comments="" )