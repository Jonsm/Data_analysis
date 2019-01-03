from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit
from scipy.optimize import OptimizeWarning
import warnings
warnings.simplefilter("error", OptimizeWarning)
warnings.simplefilter("error", RuntimeWarning)
plt.rc('font', family='serif')

def func(x, a, b, c, d):
    return a*np.exp(-(x-c)/b) + d

def funcRamsey(x, a, b, c, d, g):
    return a*np.exp(-x/b)*np.cos(2*np.pi*c*((x-g))) + d
#################################################################################################################
#Parameters
directory = 'D:\Data\Julius II\T2E'
fname = '102318_T1T2ET2R_loop_YOKO_30.995mA_Cav7.5067GHz_-20dBm_Qubit0.3212GHz_-6dBm__PiPulse414ns_Count20_TimeStepT136000_TimeStepT2E36000_TimeStepT2R4000_loop50.h5'
path = directory + '\\' + fname
pts_num = 20
time_step_T2e = 36000
time_step_T1 = 36000
time_step_T2r = 4000
T1_guess = 100e-6
T2e_guess = 100e-6
T2r_guess = 20e-6
f_Ramsey_guess = .03e6
loop_num = 28

#################################################################################################################
time_t2e = np.linspace(0, pts_num*time_step_T2e, pts_num)
time_t1 = np.linspace(0, pts_num*time_step_T1, pts_num)
time_t2r = np.linspace(0, pts_num*time_step_T2r, pts_num)
T1_array = []
T1_err_array = []
T2e_array = []
T2e_err_array = []
T2r_array = []
T2r_err_array = []
f_R_array = []
f_R_err_array = []
Tp_array = []
loop_index = []
phase_avg_t2e = np.zeros(pts_num)
phase_avg_t2r = np.zeros(pts_num)
phase_avg_t1 = np.zeros(pts_num)
#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    # print phase_raw

    for idx in range(loop_num):
        phase = phase_raw[idx, 0]
        phase_t1 = phase[::3]
        phase_t2e = phase[1::3]
        phase_t2r = phase[2::3]
        phase_t1 = np.unwrap(phase_t1)*180/np.pi
        phase_t1 = phase_t1 - np.min(phase_t1)
        phase_t1 = abs(phase_t1)
        phase_t2e = np.unwrap(phase_t2e)*180/np.pi
        phase_t2e = phase_t2e - np.min(phase_t2e)
        phase_t2e = abs(phase_t2e)
        phase_t2r = np.unwrap(phase_t2r)*180/np.pi
        phase_t2r = phase_t2r - np.min(phase_t2r)
        phase_t2r = abs(phase_t2r)
#         plt.plot(phase_t2r)
# plt.show()

        ###########################################################################
        guess = [phase_t1[0]-phase_t1[-1], T1_guess, 0, phase_t1[-1]]
        try:
            popt, pcov = curve_fit(func, time_t1*1e-9, phase_t1, guess)
        except RuntimeError:
            print ("Doesn't fit well entry " + str(idx))
            continue
        except RuntimeWarning:
            print ("Doesn't fit well entry " + str(idx))
            continue
        except OptimizeWarning:
            print ("Doesn't fit well entry " + str(idx))
            continue
        a,b,c,d = popt #b is T1
        time_nice  = np.linspace(0, pts_num*time_step_T1, pts_num*100)
        phase_fit = func(time_nice*1e-9, a, b, c, d)
        perr = np.sqrt(abs(np.diag(pcov)))
        T1 = b*1e6
        T1_err = perr[1]*1e6
        if T1_err > T1/2:
          print("Doesn't fit well entry " + str(idx))
          continue
        plt.figure(1)
        plt.title('T1')
        plt.plot(time_t1*1e-3, phase_t1, 'k-o', alpha = 0.2)
        plt.plot(time_nice*1e-3, phase_fit)
        plt.xlabel('microseconds',size=12.0)
        plt.ylabel('phase (deg)',size=12.0)
        plt.tick_params(labelsize = 14.0)

        ############################################################################
        guess = [phase_t2e[0]-phase_t2e[-1], T2e_guess, 0, phase_t2e[-1]]
        try:
            popt, pcov = curve_fit(func, time_t2e*1e-9, phase_t2e, guess)
        except RuntimeError:
            print ("Doesn't fit well entry " + str(idx))
            continue
        except RuntimeWarning:
            print ("Doesn't fit well entry " + str(idx))
            continue
        except OptimizeWarning:
            print ("Doesn't fit well entry " + str(idx))
            continue
        a,b,c,d = popt #b is T1
        time_nice  = np.linspace(0, pts_num*time_step_T2e, pts_num*100)
        phase_fit = func(time_nice*1e-9, a, b, c, d)
        perr = np.sqrt(abs(np.diag(pcov)))
        T2e = b*1e6
        T2e_err = perr[1]*1e6
        if T2e_err > T2e/2:
          print("Doesn't fit well entry " + str(idx))
          continue
        plt.figure(2)
        plt.title('T2 echo')
        plt.plot(time_t2e*1e-3, phase_t2e, 'k-o', alpha = 0.2)
        plt.plot(time_nice*1e-3, phase_fit)
        plt.xlabel('microseconds',size=12.0)
        plt.ylabel('phase (deg)',size=12.0)
        plt.tick_params(labelsize = 14.0)

        ############################################################################

        guess = [-(np.max(phase_t2r) - np.min(phase_t2r)), T2r_guess, f_Ramsey_guess, 0, 0]
        try:
            popt, pcov = curve_fit(funcRamsey, time_t2r*1e-9, phase_t2r, guess)
        except RuntimeError:
            print ("Doesn't fit well entry " + str(idx))
            continue
        except RuntimeWarning:
            print ("Doesn't fit well entry " + str(idx))
            continue
        except OptimizeWarning:
            print ("Doesn't fit well entry " + str(idx))
            continue
        a,b,c,d,g = popt
        time_nice  = np.linspace(0, pts_num*time_step_T2r, pts_num*100) #ns
        phase_fit = funcRamsey(time_nice*1e-9, a, b, c, d, g)
        perr = np.sqrt(abs(np.diag(pcov)))
        T2r = b*1e6
        T2r_err = perr[1]*1e6
        f_R = c/1e6 #MHz
        f_R_err = perr[2]/1e6
        if T2r_err > T2r/1.5 or T2r_err > T2e:
          print("Doesn't fit well entry " + str(idx))
          continue
        plt.figure(3)
        plt.title("T2 Ramsey")
        plt.plot(time_t2r*1e-3, phase_t2r, 'k-o', alpha = 0.2)
        plt.plot(time_nice*1e-3, phase_fit)
        plt.xlabel('microseconds',size=12.0)
        plt.ylabel('phase (deg)',size=12.0)
        plt.tick_params(labelsize = 14.0)

        loop_index = np.append(loop_index, idx)
        T1_array = np.append(T1_array, T1)
        T1_err_array = np.append(T1_err_array, T1_err)
        T2e_array = np.append(T2e_array, T2e)
        T2e_err_array = np.append(T2e_err_array, T2e_err)
        T2r_array = np.append(T2r_array, T2r)
        T2r_err_array = np.append(T2r_err_array, T2r_err)
        f_R_array = np.append(f_R_array, f_R)
        f_R_err_array = np.append(f_R_err_array, f_R_err)
        Tp = (T2e**-1 - (2*T1)**-1)**-1
        Tp_array = np.append(Tp_array, Tp)

plt.figure(4)
plt.errorbar(loop_index, T1_array, yerr=T1_err_array, fmt = 's', mfc = 'none', mew = 2.0, mec = 'b', ecolor = 'b', label='T1')
plt.errorbar(loop_index, T2e_array, yerr=T2e_err_array, fmt = 'h', mfc = 'none', mew = 2.0, mec = 'g', ecolor = 'g', label='T2E')
plt.errorbar(loop_index, T2r_array, yerr=T2r_err_array, fmt = 'D', mfc = 'none', mew = 2.0, mec = 'y', ecolor = 'y', label='T2R')
# plt.errorbar(loop_index, Tp_array, fmt = 'd', mfc = 'none', mew = 2.0, mec = 'r', ecolor = 'r')
plt.legend()
plt.grid()
plt.xlabel('Index',size=12.0)
plt.ylabel('microseconds',size=12.0)
plt.ylim([0,300])
plt.tick_params(labelsize = 18.0)

T1avg = np.average(T1_array)
T2Eavg = np.average(T2e_array)
T2Ravg = np.average(T2r_array)
print('Mean T1:' + str(T1avg) + '+-' + str(np.average(T1_err_array)) + ' T2E:' + str(T2Eavg)+ '+-' + str(np.average(T2e_err_array)) + ' T2R: ' + str(T2Ravg)+ '+-' + str(np.average(T2r_err_array)))
print(str(np.std(T1_array)))
plt.figure(5)
plt.errorbar(loop_index, f_R_array, yerr=f_R_err_array, fmt = 's', mfc = 'none', mew = 2.0, mec = 'r', ecolor = 'r')
plt.xlabel('Index', size=12.0)

c = np.corrcoef(T2e_array/T1_array, T1_array)
print(c)
# plt.figure(6)
# plt.errorbar(T1_array, T2e_array, xerr = T1_err_array, yerr=T2e_err_array, fmt='d', mfc = 'none', mew = 1.0, mec = 'm', ecolor = 'm')
# plt.xlabel('T1 (us)')
# plt.ylabel('T2 echo (us)')
#
# plt.figure(7)
# plt.errorbar(T1_array, T2r_array, xerr = T1_err_array, yerr=T2r_err_array, fmt='d', mfc = 'none', mew = 1.0, mec = 'orange', ecolor = 'orange')
# plt.xlabel('T1 (us)')
# plt.ylabel('T2 ramsey (us)')
#
# plt.figure(8)
# plt.errorbar(f_R_array, T2r_array, xerr = f_R_err_array, yerr=T2r_err_array, fmt='d', mfc = 'none', mew = 1.0, mec = 'orange', ecolor = 'orange')
# plt.xlabel('Ramsey freq (MHz)')
# plt.ylabel('T2 ramsey (us)')
#
# plt.figure(9)
# plt.hist(T1_array)
# plt.tick_params(labelsize = 14.0)

#Fit average
plt.figure(10)
phase_avg_t1 = phase_avg_t1 / loop_num
guess = [phase_t1 [0]-phase_t1 [-1], T1_guess, 0, phase_t1 [-1]]
popt, pcov = curve_fit(func, time_t1*1e-9, phase_t1, guess)
a,b,c,d = popt #b is T1
plt.plot(time_t1*1e-3, phase_t1 , 'b-o', alpha = 0.25)
time_nice  = np.linspace(0, pts_num*time_step_T1, pts_num*100)
phase_fit = func(time_nice*1e-9, a, b, c, d)
perr = np.sqrt(abs(np.diag(pcov)))
plt.plot(time_nice*1e-3, phase_fit, 'k-')
plt.tick_params(labelsize = 18.0)
plt.title ("Average T1 is "+str(b*1e6) +" +- " +str(perr[1]*1e6) +" us")


plt.figure(11)
phase_avg_t2e = phase_avg_t2e / loop_num
guess = [phase_t2e [0]-phase_t2e [-1], T2e_guess, 0, phase_t2e [-1]]
popt, pcov = curve_fit(func, time_t2e*1e-9, phase_t2e, guess)
a,b,c,d = popt #b is T2e
plt.plot(time_t2e*1e-3, phase_t2e , 'b-o', alpha = 0.25)
time_nice  = np.linspace(0, pts_num*time_step_T2e, pts_num*100)
phase_fit = func(time_nice*1e-9, a, b, c, d)
perr = np.sqrt(abs(np.diag(pcov)))
plt.plot(time_nice*1e-3, phase_fit, 'k-')
plt.tick_params(labelsize = 18.0)
plt.title ("Average T2e is "+str(b*1e6) +" +- " +str(perr[1]*1e6) +" us")


plt.grid()
plt.show()
