from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

directory = 'D:\Data\Fluxonium #10_7.5GHzCav\T1'
fname = '062517_HistogramTest_YOKO_24.49mA_Cav7.3644GHz_-7dBm_Qubit4.136GHz_-70dBm_PiPulse580ns_Acquisition_time100000_Avg5000_LoopNum_10.h5'
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
trace_num = 5000
integration_time = 50e-6
pts_num_integrate = int(integration_time / T_IF)

print pts_num_integrate
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    data = hf.get('TRACE_A0')
    dataB = hf.get('TRACE_B0')
    for loop_count in range(2):
        phase_integrated = np.zeros(trace_num)
        for trace_count in range(trace_num):
            trace = data[loop_count, trace_count,:]
            #Demodulated from IF frequency
            pts_num_per_period = int(T_IF/time_step) #number of points per IF period
            pts_num_IF = int(pts_num / pts_num_per_period) #number of demod points
            t_demod = np.linspace(0,pts_num_per_period, pts_num_per_period)*time_step
            I = np.zeros(pts_num_IF)
            Q = np.zeros(pts_num_IF)
            for idx in range(pts_num_IF):
                S = trace[idx*pts_num_per_period:(idx+1)*pts_num_per_period]
                for idy in range(pts_num_per_period):
                    I[idx] = I[idx]+S[idy]*time_step*np.cos(2*np.pi*f_IF*t_demod[idy])/T_IF
                    Q[idx] = Q[idx]+S[idy]*time_step*np.sin(2*np.pi*f_IF*t_demod[idy])/T_IF
            time_IF = np.linspace(0, pts_num_IF*T_IF, pts_num_IF)
            phase_IF = np.arctan(Q/I)
            phase_IF = np.unwrap(phase_IF)*180/np.pi


            traceB = dataB[loop_count, trace_count,:]
            #Demodulated from IF frequency
            pts_num_per_period = int(T_IF/time_step) #number of points per IF period
            pts_num_IF = int(pts_num / pts_num_per_period) #number of demod points
            t_demod = np.linspace(0,pts_num_per_period, pts_num_per_period)*time_step
            IB = np.zeros(pts_num_IF)
            QB = np.zeros(pts_num_IF)
            for idx in range(pts_num_IF):
                SB = traceB[idx*pts_num_per_period:(idx+1)*pts_num_per_period]
                for idy in range(pts_num_per_period):
                    IB[idx] = IB[idx]+SB[idy]*time_step*np.cos(2*np.pi*f_IF*t_demod[idy])/T_IF
                    QB[idx] = QB[idx]+SB[idy]*time_step*np.sin(2*np.pi*f_IF*t_demod[idy])/T_IF
            phaseB_IF = np.arctan(QB/IB)
            phaseB_IF = np.unwrap(phaseB_IF)*180/np.pi

            phase = phase_IF - phaseB_IF
            phase_integrated[trace_count] = np.average(phase[1:pts_num_integrate])

        # Empirical average and variance are computed
        avg = np.mean(phase_integrated)
        var = np.var(phase_integrated)
        # From that, we know the shape of the fitted Gaussian.
        pdf_x = np.linspace(np.min(phase_integrated),np.max(phase_integrated),1000)
        pdf_y = 1.0/np.sqrt(2*np.pi*var)*np.exp(-0.5*(pdf_x-avg)**2/var)

        plt.hist(phase_integrated, bins='auto', normed=True)
        plt.plot(pdf_x, pdf_y, 'k--')

plt.show()

