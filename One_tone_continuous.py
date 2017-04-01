import numpy as np
from matplotlib import pyplot as plt

#File path
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\One_tone_spec'
fname = 'test_cont_test.csv'

path = directory + '\\' + fname
traceA = np.genfromtxt(path)[1::,0]
traceB = np.genfromtxt(path)[1::,1]

IF_freq = 20e6
denom = 1
avg_num = 10
plt.plot(traceA[0:10000])
plt.show()
def demod(trace, f_IF, denominator):
    sample_num = len(trace)
    T_IF = 1.0/f_IF
    sampling_rate = 1e9 / denominator
    dt = 1.0/sampling_rate
    sec_length = int(T_IF / dt)
    array_length = int((sample_num * dt/ T_IF))
    I = np.zeros(array_length)
    Q = np.zeros(array_length)
    time = np.linspace(0, array_length, array_length)*T_IF
    t = np.linspace(0, sec_length, sec_length)
    for idx in range(array_length):
        for idy in range(sec_length):
            I[idx] = I[idx] + dt*trace[idx*sec_length + idy]*np.cos(2*np.pi*f_IF*t[idy])
            Q[idx] = Q[idx] + dt*trace[idx*sec_length + idy]*np.sin(2*np.pi*f_IF*t[idy])
    return I/T_IF, Q/T_IF, time

I_A, Q_A, time = demod(traceA, IF_freq, denom)
I_B, Q_B, time = demod(traceB, IF_freq, denom)


array_avg_length = int(len(I_A) /avg_num)
I_1 = np.zeros(array_avg_length)
Q_1 = np.zeros(array_avg_length)
I_2 = np.zeros(array_avg_length)
Q_2 = np.zeros(array_avg_length)
time_avg = np.linspace(0,time[-1],len(time)/avg_num)
print array_avg_length
for idx in range(array_avg_length):
    I_1[idx] = np.average(I_A[idx*avg_num:(idx+1)*avg_num])
    Q_1[idx] = np.average(Q_A[idx*avg_num:(idx+1)*avg_num])
    I_2[idx] = np.average(I_B[idx*avg_num:(idx+1)*avg_num])
    Q_2[idx] = np.average(Q_B[idx*avg_num:(idx+1)*avg_num])

phase = np.unwrap(np.arctan((I_1*Q_2 - I_2*Q_1)/(I_1*Q_1+I_2*Q_2)))
phase = phase * 180 /np.pi
mag = np.sqrt(I_1**2 + Q_1**2)
plt.figure(1)
plt.plot(time_avg*1e3, phase)
plt.figure(2)
plt.plot(time_avg*1e3, mag)
plt.show()