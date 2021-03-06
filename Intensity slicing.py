import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.widgets import Slider

#Enter directory and name of measurement
directory = 'D:\Data\Fluxonium #10'
measurement = 'One tune spectroscopy_YOKO 0mAto50mA_ qubit tone off_Cav_10p30GHz to 10p32GHz_1dBm_pulse_4000_2800_after 2nd thermal cycle'
path_data = directory + '\\' + measurement + '_Phase.csv'
path_freq = directory + '\\' + measurement + '_Freq.csv'
path_vol = directory + '\\' + measurement + '_Current.csv'

RawData = np.genfromtxt(path_data, delimiter =',')
Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
V = np.genfromtxt(path_vol, delimiter =',')

Z = RawData.transpose()
          
#Optional: calculate differential
Z_diff = np.diff(Z.transpose()) 
#Z_diff = Z_diff.transpose()
Freq_diff = Freq[0:len(Freq)-1]

#Plot the data for V =0 here
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
l, =plt.plot(Freq_diff,Z_diff[0])
#Slider defined here
axcolor = 'lightgoldenrodyellow'
axVol = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
sVol = Slider(axVol, 'Voltage index', 0 , len(V)-1, valinit =0, valfmt='%0.0f')

def update(val):
    vol = sVol.val
    l.set_ydata(Z_diff[vol])

sVol.on_changed(update)

plt.show()