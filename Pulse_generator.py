import numpy as np
from matplotlib import pyplot as plt
plt.close("all")

######################################################################
sample_num = int(2e3)
cavity_start = int(1e3)
cavity_width = int(1e3)
marker_width = int(1e2)
delay_qubit_cavity = 80
delay_cavity_marker = 300
#########################QUBIT PULSE#########################
#Gaussian shape
gaussian_peak = 200
gaussian_width = 100
time = np.linspace(0,2*gaussian_peak,2*gaussian_peak)
gaussian_pulse = np.exp(-np.log(2)*(2*(time-gaussian_peak)/gaussian_width)**2)

#Qubit pulse stops right before cavity pulse starts
q_pulse = np.zeros(sample_num)
q_pulse[cavity_start-gaussian_peak:cavity_start] = gaussian_pulse[gaussian_peak::]
q_pulse[0:gaussian_peak] =  gaussian_pulse[0:gaussian_peak]
q_pulse[gaussian_peak:cavity_start-gaussian_peak] = 1

#########################CAVITY PULSE#########################
c_pulse = np.zeros((sample_num, 3))
cavity_start = cavity_start - delay_qubit_cavity
marker_start = cavity_start + delay_cavity_marker
c_pulse[cavity_start:cavity_start+cavity_width, 0] = 1
c_pulse[marker_start:marker_start+marker_width, 1] = 1
c_pulse[marker_start:marker_start+marker_width, 2] = 1

c_pulse = np.zeros((sample_num, 3))
c_pulse[:,0] = 1
c_pulse[0:1000,1] = 1
c_pulse[0:1000,2] = 1
directory = 'D:\Data\Pulses'
path_qu = directory + '\\' + 'continuous.txt'
path_ca = directory + '\\' + 'continuous.txt'
# np.savetxt(path_qu, q_pulse)
np.savetxt(path_ca, c_pulse)
x_axis = np.linspace(0,sample_num,sample_num)
# plt.plot(x_axis, q_pulse)
plt.plot(x_axis, c_pulse[:, 0])
plt.plot(x_axis, c_pulse[:, 1])
plt.show()