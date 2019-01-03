# Plot intensity data

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
from qutip import*

rc('text', usetex=False)
plt.close("all")
fig=plt.figure()
ax = plt.gca()
ax.get_yaxis().get_major_formatter().set_useOffset(False)

##############################################################################################################################
###################################################    Data    ###############################################################
##############################################################################################################################
contrast_max = 1.5
contrast_min = -1.5

#File path
directory = 'D:\Data\Julius II\Two_tone'

measurement = '100618_Two_tone_spec_YOKO_0to1.75mA_Cav_7.5064GHz&-5dBm_QuBit3to5.5GHz&-5dBm'
path = directory + '\\' + measurement
#
# #Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3  b
current = current[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1:]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1:,0] #phase is recorded in rad
mag = data[1:,1]
Z = np.zeros((len(current),len(freq)))
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)
plt.figure(1)
#
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)

measurement = '100618_Two_tone_spec_YOKO_1.24to1.6mA_Cav_7.5064GHz&-10dBm_QuBit1.2to3GHz&0dBm'
path = directory + '\\' + measurement
#
# #Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3  b
current = current[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1:]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1:,0] #phase is recorded in rad
mag = data[1:,1]
Z = np.zeros((len(current),len(freq)))
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)
plt.figure(1)
#
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)

measurement = '100618_Two_tone_spec_YOKO_1.504to1.7mA_Cav_7.5064GHz&-10dBm_QuBit0.3to1.2GHz&0dBm'
path = directory + '\\' + measurement
#
# #Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3  b
current = current[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1:]
data = np.genfromtxt(path + '_PHASEMAG.csv')
phase = data[1:,0] #phase is recorded in rad
mag = data[1:,1]
Z = np.zeros((len(current),len(freq)))
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    temp = temp*180/(np.pi)
    # temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z[idx,:] = temp - np.mean(temp)
plt.figure(1)
#
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)



##############################################################################################################################
directory = 'D:\Data\Julius II\Summary'

measurement = 'T1 summary 2018_10_08_0mA.txt'
path = directory + '\\' + measurement
data = np.genfromtxt(path)
current = data[1:,0]
freq = data[1:,1]
T1 = data[1:,2]
T1_error = data[:,3]
plt.figure(1)
plt.plot(current, freq, 'r.')
plt.xlabel('I (mA)')
plt.ylabel('freq (GHz)')
plt.figure(2)
plt.ylabel('T1 (us)')
plt.xlabel('Frequency 01 (GHz)')
plt.yscale('log')
plt.ylim([0,100])
plt.errorbar(freq, T1, yerr= data[1:,3], fmt='rs', label='t1')
plt.legend()


# measurement = 'T1_summary_2018_04_13.txt'
# path = directory + '\\' + measurement
# data = np.genfromtxt(path)
# current = data[1:,0]
# freq = data[1:,1]
# T1 = data[1:,2]
# plt.figure(1)
# T1err = data[1:,3]
# #.plot(current, freq, 'r.')
# plt.figure(2)
# plt.errorbar(freq, T1, yerr=T1err, fmt='c^', label='45mA')
# plt.legend()
# plt.savefig('T1_0ma_vs_45ma')

# measurement = 'T1 wrong data4_4_18.txt'
# path = directory + '\\' + measurement
# data = np.genfromtxt(path)
# current = data[1:,0]
# freq = data[1:,1]
# T1 = data[1:,2]
# plt.figure(1)
# #T1_error = data[:,3]
# plt.plot(current, freq, 'm^')
# plt.figure(2)
# plt.plot(freq, T1, 'm^')


# measurement = 'T1_auto_31.07to31.41mA.csv'
# path = directory + '\\' + measurement
# data = np.genfromtxt(path)
# current = data[:,0]
# freq = data[:,1]
# T1 = data[:,2]
# T1_error = data[:,3]
# plt.plot(current, freq, 'r.')
##############################################################################################################################
##############################################################################################################################
# e = 1.602e-19    #Fundamental charge
# h = 6.62e-34    #Placnk's constant
# phi_o = h/(2*e) #Flux quantum
# N = 50
# B_coeff = 25.5
# def trans_energy(current, E_l, E_c, E_j, A, offset):
#     energy = np.zeros(len(current))
#     flux = current * B_coeff * A * 1e-4
#     phi_ext = (flux/phi_o-offset) * 2 * np.pi
#     a = tensor(destroy(N))
#     phi = (a + a.dag()) * (8.0 * E_c / E_l) ** (0.25) / np.sqrt(2.0)
#     na = 1.0j * (a.dag() - a) * (E_l / (8 * E_c)) ** (0.25) / np.sqrt(2.0)
#     for idx in range(len(current)):
#         ope = 1.0j * (phi - phi_ext[idx])
#         H = 4.0 * E_c * na ** 2.0 + 0.5 * E_l * phi ** 2.0 - 0.5 * E_j * (ope.expm() + (-ope).expm())
#         energy[idx] = H.eigenenergies()[1] - H.eigenenergies()[0]
#     return energy
#
# E_l = 1.0168105
# E_c = 0.835632
# E_j = 2.9964865
# A = 2.738042e-10
# offset = 0.017897167

# current = np.linspace(59,62,301)*1e-3
# energy = trans_energy(current, E_l, E_c, E_j, A, offset)
# plt.plot(current*1e3+0.39, energy)
plt.show()

