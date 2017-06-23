# Plot intensity data

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
# from qutip import*

rc('text', usetex=False)
plt.close("all")
fig=plt.figure()
ax = plt.gca()
ax.get_yaxis().get_major_formatter().set_useOffset(False)

##############################################################################################################################
###################################################    Data    ###############################################################
##############################################################################################################################
contrast_max = 0.5
contrast_min = -0.5

#File path
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_29.5to27.8mA_Cav_7.3649GHz&-15dBm_QuBit0.5to3.5GHz&25dBm'
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
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)
plt.figure(1)
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)
#############################################################################################

measurement = 'Two_tone_spec_YOKO_27.81to26.83mA_Cav_7.3649GHz&-15dBm_QuBit0.5to3.5GHz&25dBm'
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
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)
plt.figure(1)
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)
#############################################################################################

measurement = 'Two_tone_spec_YOKO_26.82to26.2mA_Cav_7.3651GHz&-15dBm_QuBit3to4GHz&25dBm'
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
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)
plt.figure(1)
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)
#############################################################################################

measurement = 'Two_tone_spec_YOKO_26.2to25.5mA_Cav_7.3652GHz&-15dBm_QuBit2to5GHz&25dBm'
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
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)
plt.figure(1)
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)
#############################################################################################

measurement = 'Two_tone_spec_YOKO_25.86to25.5mA_Cav_7.36504GHz&-15dBm_QuBit2.5to4.5GHz&20dBm'
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
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)
plt.figure(1)
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)
#############################################################################################

measurement = 'Two_tone_spec_YOKO_25.51to24.8mA_Cav_7.3651GHz&-15dBm_QuBit4to4.5GHz&20dBm'
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
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)
plt.figure(1)
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)
#############################################################################################

measurement = 'Two_tone_spec_YOKO_24.81to24.1mA_Cav_7.3651GHz&-15dBm_QuBit4.2to4.9GHz&14dBm'
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
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)
plt.figure(1)
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)

#############################################################################################

measurement = 'Two_tone_spec_YOKO_24.1to24.2mA_Cav_7.3651GHz&-15dBm_QuBit4.2to4.9GHz&0dBm'
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
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)
plt.figure(1)
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)

#############################################################################################

measurement = 'Two_tone_spec_YOKO_28.3to28.8mA_Cav_7.365GHz&-15dBm_QuBit0.45to2.5GHz&10dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1::]-0.022
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
    Z[idx,:] = temp - np.mean(temp)


X,Y = np.meshgrid(current,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max, alpha = 1)

#############################################################################################

measurement = 'Two_tone_spec_YOKO_28.53to28.58mA_Cav_7.3649GHz&-15dBm_QuBit0.48to0.55GHz&25dBm'
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
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)
plt.figure(1)
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)
#############################################################################################

##############################################################################################################################
######################################################Fit points##############################################################
##############################################################################################################################
current = []
freq = []

current_temp = np.array([ 29.49,  29.47,  29.39,  29.31,  29.23,  29.16,  29.07, 29.02,  28.91,  28.88,
  28.86,  28.83,  28.81,  28.8,   28.79,  28.74,  28.74,  28.72,  28.71,  28.7,   28.7,
  28.68,  28.68,  28.44,  28.43,  28.42,  28.4,   28.39,  28.38,  28.37,  28.36,
  28.36,  28.34,  28.32,  28.3,   28.28,  28.26,  28.22,  28.19,  28.08,  28.02,
  27.96,  27.9,   27.84]
)
freq_temp = np.array([ 3.07888274,  3.10784471,  3.17865846,  3.22597436,  3.23681812,  3.22320857,
  3.16459389,  3.11824053,  2.95300943,  2.88047903,  2.82613973,  2.72755895,
  2.64500435,  2.59857406,  2.54924519,  2.21633936,  2.2163394,   2.04476789,
  1.95202107,  1.85533752,  1.85091906,  1.64373926,  1.64429497,  1.47401488,
  1.66631586,  1.77094064,  1.97274242,  2.06573406 , 2.15365691,  2.23814375,
  2.31364724 , 2.3136059,   2.45072464 , 2.56460009 , 2.66056089 , 2.74271461,
  2.80908828,  2.91991385,  2.98801628 , 3.14554225 , 3.19727651 , 3.23425782,
  3.25317485,  3.25691738]
)

current = np.append(current, current_temp)
freq = np.append(freq, freq_temp)

current_temp = np.array([ 27.78 , 27.75 , 27.72  ,27.63 , 27.59,  27.54,  27.51,  27.5,   27.41,  27.39 ,
  27.37,  27.14 , 27.13 , 27.11,  27.1,   27.07 , 27.03 ,    27 ,   26.96 ,
  26.94,  26.91]

)
freq_temp = np.array([ 3.24242972 , 3.22979035,  3.20861888 , 3.1282661,  3.06436295  ,2.96457013 ,
  2.86313308 , 2.82206851,  2.23510137 , 2.00624104 , 1.79130058,  1.65934637 ,
  1.79404183,  2.06283957 , 2.19171163 , 2.54986395,  2.91141597,  3.08730759 ,
   3.24059697,  3.29833139,  3.37084768]

)

current = np.append(current, current_temp)
freq = np.append(freq, freq_temp)

current_temp = np.array([ 26.78 , 26.74 , 26.53 , 26.44,  26.37]
)
freq_temp = np.array([ 3.57758774 , 3.62154917,  3.75181656,  3.7706683,   3.76730393]
)

current = np.append(current, current_temp)
freq = np.append(freq, freq_temp)

current_temp = np.array([ 26.13 , 26.12 , 26.1,  26.09]
)
freq_temp = np.array([ 3.54407536,  3.49693351 , 3.34704922,  3.2380784]
)

current = np.append(current, current_temp)
freq = np.append(freq, freq_temp)

current_temp = np.array([ 25.68 , 25.63 , 25.59,  25.55]
)
freq_temp = np.array([ 3.31545838 , 3.85662582,  3.9756649,   4.04288432]
)

current = np.append(current, current_temp)
freq = np.append(freq, freq_temp)

plt.plot(current, freq, 'ro')
##############################################################################################################################
##############################################################################################################################
plt.show()

