import numpy as np
from matplotlib import pyplot as plt

directory = 'G:\Projects\Resonators\\2017-09-04-JJ-Xerxces'
fucking_date = '2017-09-04-'
fucking_meas = '-FluxSweepNegCurrentAfterWarmUp_MLOG_6.75 GHz_7.1 GHz_-40.00dBm_'
fucking_number = np.linspace(38,183, (183-38) + 1)
current = np.linspace(29.0, 0.0, 29.0/0.2 + 1.0)
path = directory + '\\'+ fucking_date + '38' + fucking_meas  + '29.00000' + 'mA.dat'
freq = np.genfromtxt(path, skip_header=13)[:,0]
mag = np.zeros((len(freq), len(current)))

for idx in range(len(current)):
    current_string = str(format(current[idx], '.5f'))
    path = directory + '\\'+ fucking_date + str(int(fucking_number[idx])) + fucking_meas  + current_string + 'mA.dat'
    fucking_data = np.genfromtxt(path, skip_header=13)
    mag[:,idx] = fucking_data [:,1]

X,Y = np.meshgrid(freq,current)
Z = mag

plt.pcolormesh(X,Y,Z.transpose(), vmin = -1, vmax = 0)
plt.colorbar()
plt.show()



