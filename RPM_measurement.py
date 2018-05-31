from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

from matplotlib import rc
plt.rc('font', family='serif')
# plt.figure(figsize = [10,7])
# def func(x,a,b,c,d,tau):
#     return a*np.cos(2*np.pi*b*(x-c))*np.exp(-x/tau) + d
# directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Rabi'
# directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Raman'
# fname = '050617_Rabi3Tone014A_YOKO_28.551mA_Cav7.36485GHz_-15dBm_Qubit0.504GHz_25dBm_Qubit125.52879GHz_10dBm_Count20_TimeStep30_Avg100000.h5'
# path = directory + '\\' + fname
# pts_num = 20
# time_step = 30
# time = np.linspace(0, pts_num*time_step, pts_num)
# tau = 1e-7*1e9
# #Read data and fit
# with h5py.File(path,'r') as hf:
#     print('List of arrays in this file: \n', hf.keys())
#     count = np.array(hf.get('count'))
#     phase_raw = hf.get('PHASEMAG_Phase0')
#     phase = phase_raw[0, 0]
#     phase = np.unwrap(phase)*180/np.pi
#     phase = phase - np.mean(phase)
# plt.figure(1)
# plt.plot(time, phase, '-o', color = 'r')
# guess = ([np.max(phase)-np.min(phase), 0.5/abs(time[np.argmax(phase)] - time[np.argmin(phase)]), 0, 0, tau])
# opt,cov = curve_fit(func, time, phase, guess)
# time_nice = np.linspace(0, pts_num*time_step, pts_num*100)
# plt.plot(time_nice, func(time_nice, *opt))
# Aa = guess[0]
#
# fname = '050617_Rabi3Tone014B_YOKO_28.551mA_Cav7.36485GHz_-15dBm_Qubit0.504GHz_25dBm_Qubit125.52879GHz_10dBm_Count20_TimeStep30_Avg100000.h5'
# path = directory + '\\' + fname
# #Read data and fit
# with h5py.File(path,'r') as hf:
#     print('List of arrays in this file: \n', hf.keys())
#     count = np.array(hf.get('count'))
#     phase_raw = hf.get('PHASEMAG_Phase0')
#     phase = phase_raw[0, 0]
#     phase = np.unwrap(phase)*180/np.pi
#     phase = phase - np.mean(phase)
# plt.plot(time, phase, '-o', color = 'b')
# guess = ([np.max(phase)-np.min(phase), 0.5/abs(time[np.argmax(phase)] - time[np.argmin(phase)]), 0, 0, tau])
# opt,cov = curve_fit(func, time, phase, guess)
# time_nice = np.linspace(0, pts_num*time_step, pts_num*100)
# plt.plot(time_nice, func(time_nice, *opt))
# Ab = guess[0]


###############################################################################################################
h = 6.62606876e-34
kB = 1.3806503e-23
f = .6343e9
# f02 = 5.549e9
Aa = .0996
Ab = .238
ratio = Aa/Ab
T_eff = -h*f/(kB*np.log(ratio))
print ('ratio=' + str(ratio))
print ('T_eff=' + str(T_eff*1e3))
###############################################################################################################
# f = 3.43e9
# print (np.exp(-h*f/(kB*T_eff)))
###############################################################################################################
# T=np.linspace(1,100,1000)*1e-3
# y1 = ratio*(1-np.exp(-h*f02/(kB*T)))
# y2 = np.exp(-h*f01/(kB*T)) - np.exp(-h*f02/(kB*T))
# plt.figure(2)
# plt.plot(T*1e3,y1, T*1e3, y2)
plt.show()