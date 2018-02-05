
from matplotlib import pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import h5py

#File path
directory = 'D:\Data\Calibration'
measurement = 'Calibration_IQ_NOAMP-30dBm_40mV_2.csv'
path = directory + '\\' + measurement
I = np.genfromtxt(path)[1:5001,0]
Q = np.genfromtxt(path)[1:5001,1]
I_ref = np.genfromtxt(path)[1:5001,2]
Q_ref= np.genfromtxt(path)[1:5001,3]

phase = np.arctan2(Q,I)
phase_ref = np.arctan2(Q_ref,I_ref)
phase = phase - phase_ref
amp = np.sqrt(I**2+Q**2)
I = amp*np.cos(phase)
Q = amp*np.sin(phase)
plt.figure(1)
plt.plot(I,Q, '.')
plt.axis('equal')

I_mean = np.mean(I)
I_variance = np.var(I)
I_sigma = np.sqrt(I_variance)
Q_mean = np.mean(Q)
Q_variance = np.var(Q)
Q_sigma = np.sqrt(Q_variance)

# plt.figure(2)
# n, bins, patches = plt.hist(I, 50, normed=1, facecolor='green', alpha=0.75)
# x = np.linspace(min(I), max(I), 100)
# plt.plot(x, mlab.normpdf(x, I_mean, I_sigma))

# plt.figure(3)
# n, bins, patches = plt.hist(Q, 50, normed=1, facecolor='green', alpha=0.75)
# x = np.linspace(min(Q), max(Q), 100)
# plt.plot(x, mlab.normpdf(x, Q_mean, Q_sigma))

SNR = np.sqrt(I_mean**2 + Q_mean**2)/np.sqrt(I_sigma**2 + Q_sigma**2)

print (SNR)

plt.show()