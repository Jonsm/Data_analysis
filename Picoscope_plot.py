import numpy as np
from matplotlib import pyplot as plt

directory = 'D:\Data\Calibration\\2018-12-05-Spectrum'
fname = 'IQ_100MHzMod_gaussian_40nsWidth2.txt'
'''
Channel 2
Signal's parameters:
  2048                      (Record Length)
Waveform

 0.00000000000000E+0000       X-Value of the first point, Main unit)
s       (Main Dimension of horizontal axes)
s       (Auxiliary Dimension of horizontal axes)
 5.00000000000E-0011       (Sample interval, Main unit)
 1.00000000000000E+0000         (X-Axis Auxiliary coeffitient)
V        (Dimension of vertical axes)
 1.00000000000E-0003        (Vertical offset)
Display's parameters:
 0.00000000000000E+0000      X-Value of left side of the screen
 1.00000000000000E-0008      X-Value/div
1         (Horizontal zoom factor)
 0.00000000000000E+0000         (Horizontal zoom position in div)
 2.00000000000E-0002        (Vertical Scale per division)
 1.26000000000E-0001        (Vertical Pozition)
'''
path = directory + '\\' + fname
data = np.genfromtxt(path, skip_header=24)
sample_num = 2048
time_step = 5.00000000000E-0011
time_offset = 0
volt_step = 2.64000000000E-0001
time = np.linspace(0,sample_num,sample_num)*time_step + time_offset
plt.plot(time*1e9, data*volt_step)
plt.xlabel('ns')
# plt.ylabel('V')
plt.show()
