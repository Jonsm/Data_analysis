from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

directory = 'D:\Data\Fluxonium waveguide 1\T2R'
fname = '121618_T2R_YOKO_1.398mA_Cav7.0808GHz_-35dBm_Qubit1.0592GHz_16dBm_PiPulse260ns_Count30_TimeStep500.h5'
path = directory + '\\' + fname
pts_num = 30
time_step = 500
time = np.linspace(0, pts_num*time_step, pts_num)
t2_guess = 10e-6
freq_guess = .2e6
#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    # print phase_raw
    phase = phase_raw[0, 0]
    phase = np.unwrap(phase)*180/np.pi
    phase = phase - np.min(phase)
    phase = abs(phase)

plt.plot(time*1e-3, phase, '-o')
###########################################################
# Curve fitting
###########################################################
def func(x, a, b, c, d, g):
    return a*np.exp(-x/b)*np.cos(2*np.pi*c*((x-g))) + d

guess = [np.max(phase) - np.min(phase), t2_guess, freq_guess, 0, 0]

popt, pcov = curve_fit(func, time*1e-9, phase, guess)

a,b,c,d,g = popt
time_nice  = np.linspace(0, pts_num*time_step, pts_num*100) #ns
phase_fit = func(time_nice*1e-9, a, b, c, d, g)
perr = np.sqrt(abs(np.diag(pcov)))
T2 = b*1e6 #us
T2_err = perr[1]*1e6 #us
f_R = c/1e6 #MHz
plt.plot(time_nice*1e-3, phase_fit, linewidth = 2.0)

plt.xlabel('Time(us)')
plt.ylabel('Phase')
plt.title('T2 Ramsey=' + str(T2) + '+/-' + str(T2_err) + 'us, f_R=' + str(f_R) + 'MHz')
plt.tick_params(labelsize = 18.0)
plt.xlabel('microseconds',size=12.0)
plt.ylabel('phase',size=12.0)
plt.show()