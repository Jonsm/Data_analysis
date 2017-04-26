# Plot intensity data

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc
rc('text', usetex=False)
fig = plt.figure()

#Enter directory and name of measurement
#File path
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_28.4to28.44mA_Cav_7.3649GHz&-15dBm_QuBit0.5to1.5GHz&16dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1::]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1::,0] #phase is recorded in rad
mag = data[1::,1]
Z = np.zeros((len(current),len(freq)))
# print (phase)
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.max(temp)


X,Y = np.meshgrid(current,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu_r', vmin = -0.5, vmax = 0.5)

##############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_28.44to28.8mA_Cav_7.3649GHz&-15dBm_QuBit0.5to1.5GHz&20dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1::]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1::,0] #phase is recorded in rad
mag = data[1::,1]
Z = np.zeros((len(current),len(freq)))
# print (phase)
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.max(temp)


X,Y = np.meshgrid(current,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu_r', vmin = -0.5, vmax = 0.5)

##############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_28.526to28.529mA_Cav_7.3649GHz&-15dBm_QuBit0.5to0.51GHz&0dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1::]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1::,0] #phase is recorded in rad
mag = data[1::,1]
Z = np.zeros((len(current),len(freq)))
# print (phase)
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.max(temp)


X,Y = np.meshgrid(current,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu_r', vmin = -0.5, vmax = 0)

##############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_28.529to28.53mA_Cav_7.3649GHz&-15dBm_QuBit0.5to0.51GHz&0dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1::]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1::,0] #phase is recorded in rad
mag = data[1::,1]
Z = np.zeros((len(current),len(freq)))
# print (phase)
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.max(temp)


X,Y = np.meshgrid(current,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu_r', vmin = -0.5, vmax = 0)

##############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_28.53to28.535mA_Cav_7.3649GHz&-15dBm_QuBit0.5to0.51GHz&0dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1::]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1::,0] #phase is recorded in rad
mag = data[1::,1]
Z = np.zeros((len(current),len(freq)))
# print (phase)
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.max(temp)


X,Y = np.meshgrid(current,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu_r', vmin = -0.5, vmax = 0)

#Click on the points on screen to define an approximation line for interpolation
def onclick(event):
    print ('[%f, %f],'%(event.xdata, event.ydata))
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()