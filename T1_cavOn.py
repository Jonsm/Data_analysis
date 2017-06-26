from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

def func(x, a, b, c, d):
    return a*np.exp(-(x-c)/b) + d

directory = 'D:\Data\Fluxonium #10_7.5GHzCav\T1'
fname = '062517_T1CavityOn_YOKO_24.49mA_Cav7.3644GHz_-7dBm_Qubit4.136GHz_25dBm_PiPulse580ns_Acquisition_time100000_Avg5000_LoopNum_10.h5'
path = directory + '\\' + fname
acquisition_time = 1e5 #ns
decimation = 1
f_IF = 50e6 #Hz
T_IF = 1/f_IF
clock = 1e-9
pts_num = acquisition_time / decimation
time_step = clock*decimation
time_raw = np.linspace(0, pts_num*time_step, pts_num)
loop_num = 11
average = 200 #points in phase trace to average together

#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    data = hf.get('IQ_A0')
    dataB = hf.get('IQ_B0')
    count = 0
    for loop_count in range(loop_num):
        trace = data[loop_count,:]
        plt.figure(1)
        plt.plot(time_raw, trace)

        #Demodulated from IF frequency
        pts_num_per_period = int(T_IF/time_step) #number of points per IF period
        pts_num_IF = int(pts_num / pts_num_per_period) #number of demod points
        # print (T_IF, pts_num_per_period, pts_num_IF)
        t_demod = np.linspace(0,pts_num_per_period, pts_num_per_period)*time_step
        I = np.zeros(pts_num_IF)
        Q = np.zeros(pts_num_IF)
        for idx in range(pts_num_IF):
            S = trace[idx*pts_num_per_period:(idx+1)*pts_num_per_period]
            for idy in range(pts_num_per_period):
                I[idx] = I[idx]+S[idy]*time_step*np.cos(2*np.pi*f_IF*t_demod[idy])/T_IF
                Q[idx] = Q[idx]+S[idy]*time_step*np.sin(2*np.pi*f_IF*t_demod[idy])/T_IF

        time_IF = np.linspace(0, pts_num_IF*T_IF, pts_num_IF)
        # plt.figure(2)
        # plt.plot(time_IF, I)
        # plt.figure(3)
        # plt.plot(time_IF, Q)
        phase_IF = np.arctan(Q/I)
        phase_IF = np.unwrap(phase_IF)*180/np.pi
        # phase_IF = phase_IF - phase_IF[-1]
        # plt.figure(4)
        # plt.plot(time_IF, phase_IF)

        pts_num_avg = int(pts_num_IF/average)
        phase_avg = np.zeros(pts_num_avg)
        for idx in range(pts_num_avg):
            phase_avg[idx] = np.average(phase_IF[idx*average:(idx+1)*average])

        time_avg = np.linspace(0, pts_num_avg*T_IF*average, pts_num_avg)*1e9

        time_avg = time_avg[1:]
        phase_avg = phase_avg[1:]
        # phase_avg = phase_avg - phase_avg[0]
        if np.max(phase_avg) - np.min(phase_avg) > 2:
            print ("Entry " + str(loop_count) + " is not good")
            continue
        ###################################
        #Optional: using reference signal
        ###################################
        # '''
        traceB = dataB[loop_count,:]
        # plt.figure(1)
        # plt.plot(time_raw, trace)

        #Demodulated from IF frequency
        pts_num_per_period = int(T_IF/time_step) #number of points per IF period
        pts_num_IF = int(pts_num / pts_num_per_period) #number of demod points
        # print (T_IF, pts_num_per_period, pts_num_IF)
        t_demod = np.linspace(0,pts_num_per_period, pts_num_per_period)*time_step
        IB = np.zeros(pts_num_IF)
        QB = np.zeros(pts_num_IF)
        for idx in range(pts_num_IF):
            SB = traceB[idx*pts_num_per_period:(idx+1)*pts_num_per_period]
            for idy in range(pts_num_per_period):
                IB[idx] = IB[idx]+SB[idy]*time_step*np.cos(2*np.pi*f_IF*t_demod[idy])/T_IF
                QB[idx] = QB[idx]+SB[idy]*time_step*np.sin(2*np.pi*f_IF*t_demod[idy])/T_IF

        time_IF = np.linspace(0, pts_num_IF*T_IF, pts_num_IF)
        # plt.figure(2)
        # plt.plot(time_IF, I)
        # plt.figure(3)
        # plt.plot(time_IF, Q)
        phaseB_IF = np.arctan(QB/IB)
        phaseB_IF = np.unwrap(phaseB_IF)*180/np.pi
        # phaseB_IF = phaseB_IF - phaseB_IF[-1]
        # plt.figure(4)
        # plt.plot(time_IF, phase_IF)

        pts_num_avg = int(pts_num_IF/average)
        phaseB_avg = np.zeros(pts_num_avg)
        for idx in range(pts_num_avg):
            phaseB_avg[idx] = np.average(phaseB_IF[idx*average:(idx+1)*average])

        time_avg = np.linspace(0, pts_num_avg*T_IF*average, pts_num_avg)*1e9

        time_avg = time_avg[1:]
        phaseB_avg = phaseB_avg[1:]
        # phase_avg = phase_avg - phase_avg[0]
        if np.max(phaseB_avg) - np.min(phaseB_avg) > 2:
            print ("Entry " + str(loop_count) + " is not good")
            continue
        # '''
        plt.figure(5)
        # phase_avg = phase_avg - phaseB_avg
        # phase_avg = phase_avg - phase_avg[0]
        plt.plot(time_avg, phase_avg, '-s')
        plt.plot(time_avg, phaseB_avg, '-s')

        count= count + 1

        if loop_count == 0:
            phase_final = phase_avg
        else:
            phase_final = phase_final + phase_avg

phase_final = phase_final / count
guess = [phase_final[0]-phase_final[-1], 50e-6, 0, phase_final[-1]]

popt, pcov = curve_fit(func, time_avg*1e-9, phase_final, guess)
a,b,c,d = popt
perr = np.sqrt(abs(np.diag(pcov)))
time_nice = np.linspace(0, pts_num_avg*T_IF*average, pts_num_avg)*1e9

plt.figure(6)
plt.plot(time_avg, phase_final, 'rd')
plt.plot(time_nice, func(time_nice*1e-9, a, b, c, d))
plt.title(str( b*1e6)+ r'$\pm$' +str(perr[1]*1e6))
plt.show()