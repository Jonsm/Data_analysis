# Plot intensity data

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc
from scipy import interpolate

rc('text', usetex=False)

#Enter directory and name of measurement
directory = 'G:\Projects\Fluxonium & qubits\Data\\2016_01\\13'
measurement = 'S21_Phase2tones_ZNB_0&n40_BW100Hz_SMB_n20dBm_6to8GHz_YOKO_n7ton10V'
path_data = directory + '\\' + measurement + '_Phase_diff.csv'
path_freq = directory + '\\' + measurement + '_Freq.csv'
path_vol = directory + '\\' + measurement + '_Voltage.csv'

RawData = np.genfromtxt(path_data, delimiter =',')
Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
V = np.genfromtxt(path_vol, delimiter =',')

Z = RawData.transpose()
          
#Optional: calculate differential
Z_diff = np.diff(Z.transpose()) 
Z_diff = Z_diff.transpose()

#Plot the intensity map
X, Y = np.meshgrid(V,Freq)
fig=plt.figure()
#plt.pcolormesh(X, Y, Z, cmap=cm.BuGn, vmin =-4 , vmax =1)
plt.title(measurement)
plt.xlabel("Voltage (V)")
plt.ylabel("Frequency (GHz)")
#plt.colorbar()

##################################Approximation line#################################
A = np.array([
[28.414113, 1.478659],
[28.418044, 1.439024],
[28.422581, 1.382622],
[28.426210, 1.338415],
[28.460685, 0.986280],
[28.464919, 0.934451],
[28.468246, 0.888720],
[28.474597, 0.832317],
[28.478226, 0.797256],
[28.482762, 0.757622],
[28.485786, 0.721037],
[28.490020, 0.690549],
[28.496371, 0.638720],
[28.502117, 0.588415],
[28.509980, 0.550305],
[28.519960, 0.515244],
[28.525403, 0.509146],
[28.532359, 0.510671],
[28.538105, 0.527439],
[28.545060, 0.557927],
[28.553528, 0.617378],
[28.559879, 0.669207],
[28.564415, 0.705793],
[28.568347, 0.739329],
[28.585585, 0.917683],
[28.591331, 0.964939],
[28.624899, 1.339939],
[28.626714, 1.359756],
[28.630645, 1.400915],
[28.634577, 1.455793]

])
x=A[:,0]
y=A[:,1]
#plt.plot(x,y,'bo')

################################Interpolation##################################

tck = interpolate.splrep(x, y, s=1)
f = interpolate.splev(V, tck, der=0)
#plt.plot(V,f,'r-.')

################################Find minimum###################################
seek_range = 0.2
Freq_min = np.zeros(len(V))
for idy in range(len(Z[0,:])):
    min_val = 0.0
    for idx in range(len(Z[:,0])):
        if (Freq[idx] < (f[idy] + seek_range)) and (Freq[idx] > (f[idy] - seek_range)):
            if (Z[idx,idy] < min_val):
                min_val = Z[idx,idy]
                idxo=idx
    Freq_min[idy] = Freq[idxo]

plt.plot(V,Freq_min,'k--',linewidth = '2')
#############################################
directory = 'G:\Projects\Fluxonium & qubits\Data\\2016_01\\12'
measurement = 'S21_Phase_ZNB_0dBm&n40dB_YOKO_n11p4ton11p9'
path_data = directory + '\\' + measurement + '_Phase_diff.csv'
path_freq = directory + '\\' + measurement + '_Freq.csv'
path_vol = directory + '\\' + measurement + '_Voltage.csv'

RawData = np.genfromtxt(path_data, delimiter =',')
Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
V = np.genfromtxt(path_vol, delimiter =',')
Z = RawData.transpose()          
X, Y = np.meshgrid(V,Freq)
plt.pcolormesh(X, Y, Z)

plt.show()
