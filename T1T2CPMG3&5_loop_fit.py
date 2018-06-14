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

#################################################################################################################
#Parameters
directory = 'D:\Data\Fluxonium #23\T2CPMG'
fname = '061118_T1T2ET2R_loop_YOKO_91.258mA_Cav7.5612GHz_0dBm_Qubit0.6304GHz_25dBm__PiPulse485ns_Count25_TimeStepT112000_TimeStepT2E18000_TimeStepT2R2500_loop50.h5'
path = directory + '\\' + fname
pts_num = 25
time_step_T2_cp3 = 18000
time_step_T1 = 12000
time_step_T2_cp5 = 2500
T1_guess = 55e-6
T2_cp3_guess = 75e-6
T2_cp5_guess = 30e-6
loop_num = 46

#################################################################################################################
time_t2_cp3 = np.linspace(0, pts_num*time_step_T2e, pts_num)
time_t1 = np.linspace(0, pts_num*time_step_T1, pts_num)
time_t2_cp5 = np.linspace(0, pts_num*time_step_T2r, pts_num)
T1_array = []
T1_err_array = []
T2_cp3_array = []
T2_cp3_err_array = []
T2_cp5_array = []
T2_cp5_err_array = []
Tp_array = []
loop_index = []

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    # print phase_raw

    for idx in range(loop_num):
        phase = phase_raw[idx, 0]
        phase_t1 = phase[::3]
        phase_t2_cp3 = phase[1::3]
        phase_t2_cp5 = phase[2::3]
        phase_t1 = np.unwrap(phase_t1)*180/np.pi
        phase_t1 = phase_t1 - np.min(phase_t1)
        phase_t1 = abs(phase_t1)
        phase_t2_cp3 = np.unwrap(phase_t2e)*180/np.pi
        phase_t2_cp3 = phase_t2e - np.min(phase_t2e)
        phase_t2_cp3 = abs(phase_t2e)
        phase_t2_cp5 = np.unwrap(phase_t2r)*180/np.pi
        phase_t2_cp5= phase_t2r - np.min(phase_t2r)
        phase_t2_cp5 = abs(phase_t2r)

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
        plt.figure(1)
        plt.plot(time_t1*1e-3, phase_t1, 'k-o', alpha = 0.2)
        plt.plot(time_nice*1e-3, phase_fit)
        plt.xlabel('microseconds',size=12.0)
        plt.ylabel('phase (deg)',size=12.0)
        plt.tick_params(labelsize = 14.0)

        ############################################################################
        guess = [phase_t2_cp3[0]-phase_t2_cp3[-1], T2_cp3_guess, 0, phase_t2_cp3[-1]]
        try:
            popt, pcov = curve_fit(func, time_t2_cp3*1e-9, phase_t2_cp3, guess)
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
        time_nice  = np.linspace(0, pts_num*time_step_T2_cp3, pts_num*100)
        phase_fit = func(time_nice*1e-9, a, b, c, d)
        perr = np.sqrt(abs(np.diag(pcov)))
        T2_cp3 = b*1e6
        T2_cp3_err = perr[1]*1e6
        if T2_cp3_err > T2_cp3/3.0:
          print("Doesn't fit well entry " + str(idx))
          continue
        plt.figure(2)
        plt.plot(time_t2_cp3*1e-3, phase_t2_cp3, 'k-o', alpha = 0.2)
        plt.plot(time_nice*1e-3, phase_fit)
        plt.xlabel('microseconds',size=12.0)
        plt.ylabel('phase (deg)',size=12.0)
        plt.tick_params(labelsize = 14.0)

        ############################################################################
        guess = [phase_t2_cp5[0]-phase_t2_cp5[-1], T2_cp5_guess, 0, phase_t2_cp5[-1]]
        try:
            popt, pcov = curve_fit(func, time_t2_cp5*1e-9, phase_t2_cp5, guess)
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
        time_nice  = np.linspace(0, pts_num*time_step_T2_cp5, pts_num*100)
        phase_fit = func(time_nice*1e-9, a, b, c, d)
        perr = np.sqrt(abs(np.diag(pcov)))
        T2_cp5 = b*1e6
        T2_cp5_err = perr[1]*1e6
        if T2_cp5_err > T2_cp5/3.0:
          print("Doesn't fit well entry " + str(idx))
          continue
        plt.figure(2)
        plt.plot(time_t2_cp5*1e-3, phase_t2_cp5, 'k-o', alpha = 0.2)
        plt.plot(time_nice*1e-3, phase_fit)
        plt.xlabel('microseconds',size=12.0)
        plt.ylabel('phase (deg)',size=12.0)
        plt.tick_params(labelsize = 14.0)

        loop_index = np.append(loop_index, idx)
        T1_array = np.append(T1_array, T1)
        T1_err_array = np.append(T1_err_array, T1_err)
        T2_cp3_array = np.append(T2_cp3_array, T2_cp3)
        T2_cp3_err_array = np.append(T2_cp3_err_array, T2_cp3_err)
        T2_cp5_array = np.append(T2_cp5_array, T2_cp5)
        T2_cp5_err_array = np.append(T2_cp5_err_array, T2_cp5_err)

plt.figure(4)
plt.errorbar(loop_index, T1_array, yerr=T1_err_array, fmt = 's', mfc = 'none', mew = 2.0, mec = 'b', ecolor = 'b', label='T1')
plt.errorbar(loop_index, T2_cp3_array, yerr=T2_cp3_err_array, fmt = 'h', mfc = 'none', mew = 2.0, mec = 'g', ecolor = 'g', label='T2CP3')
plt.errorbar(loop_index, T2_cp5_array, yerr=T2_cp5_err_array, fmt = 'D', mfc = 'none', mew = 2.0, mec = 'y', ecolor = 'y', label='T2CP5')
plt.legend()
plt.xlabel('Index',size=12.0)
plt.ylabel('microseconds',size=12.0)
plt.ylim([0,120])
plt.tick_params(labelsize = 18.0)

T1_avg = np.average(T1_array)
T2_cp5_avg = np.average(T2_cp5_array)
T2_cp3_avg = np.average(T2_cp3_array)
print('Mean T1:' + str(T1_avg) + '+-' + str(np.average(T1_err_array)) + ' T2CP3:' + str(T2_cp3_avg)+ '+-' + str(np.average(T2_cp3_err_array)) + ' T2CP5: ' + str(T2_cp5_avg)+ '+-' + str(np.average(T2_cp5_err_array)))

# plt.figure(5)
# plt.errorbar(loop_index, f_R_array, yerr=f_R_err_array, fmt = 's', mfc = 'none', mew = 2.0, mec = 'r', ecolor = 'r')
# plt.xlabel('Index', size=12.0)
# plt.ylabel('Ramsey freq(MHz)',size=12.0)
# plt.tick_params(labelsize = 14.0)
# plt.grid()
plt.show()