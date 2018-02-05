from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


#File path
directory = 'D:\Data\Fluxonium #10\T1_YOKO 44p5mA_qubit 3p2139GHz 16dBm_Cav 10p304GHz_8dBm_Avg2M_T1 pulse id 80'
measurement = '1.000000_Phase.csv'
path = directory + '\\' + measurement
phase = np.genfromtxt(path , delimiter = ',')
phase = phase - np.min(phase)
measurement = '1.000000_Time.csv'
path = directory + '\\' + measurement
time = np.genfromtxt(path , delimiter = ',') #in us
plt.plot(time, phase,'s-')
def func(x, a, b, c, d):
    return a*np.exp(-(x-c)/b) + d

guess = [phase[0]-phase[-1], 20e-6, 0, phase[-1]]
popt, pcov = curve_fit(func, time*1e-6, phase, guess)
a,b,c,d = popt #b is T1
time_nice = np.linspace(time[0], time[-1], len(time)*100)
phase_fit = func(time_nice*1e-6, a, b, c, d)
perr = np.sqrt(abs(np.diag(pcov)))
plt.plot(time_nice, phase_fit)
plt.tick_params(labelsize = 18.0)
print (b)
plt.show()