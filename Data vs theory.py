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
contrast_min = -1.5
contrast_max = 0.5
# '''
#File path
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_26to27mA_Cav_7.365GHz&-15dBm_QuBit3to4GHz&5dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1::]
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
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)

##############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_25to26mA_Cav_7.3649GHz&-15dBm_QuBit3.5to4.5GHz&5dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1::]
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
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)

##############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_27to30mA_Cav_7.365GHz&-15dBm_QuBit2.5to3.5GHz&5dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1::]
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
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max)
# '''

##############################################################################################################################
############################################################Second CD#########################################################
##############################################################################################################################
# '''
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_30to26mA_Cav_7.3649GHz&-15dBm_QuBit0.5to3.5GHz&20dBm'
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


X,Y = np.meshgrid(current-0.015, freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max, alpha = 1)

##############################################################################################################################
#!st CD
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_28.3to28.8mA_Cav_7.365GHz&-15dBm_QuBit0.45to2.5GHz&10dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1::]
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


X,Y = np.meshgrid(current-0.035,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max, alpha = 1)

##############################################################################################################################
#############################################################Third CD#########################################################
##############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_26.2to25.7mA_Cav_7.3649GHz&-15dBm_QuBit2.5to3.5GHz&15dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1::]
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


X,Y = np.meshgrid(current-0.015,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max, alpha = 1)

#############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_25.5to23mA_Cav_7.3649GHz&-15dBm_QuBit3.5to5.5GHz&10dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURRENT.csv')#*1e3
current = current[1::]
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


X,Y = np.meshgrid(current-0.02,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max, alpha = 1)

#############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_23to22mA_Cav_7.3649GHz&-15dBm_QuBit4.5to5.5GHz&5dBm'
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


X,Y = np.meshgrid(current-0.02,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max, alpha = 1)

#############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_22to21mA_Cav_7.366GHz&-15dBm_QuBit5to6GHz&5dBm'
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


X,Y = np.meshgrid(current-0.02,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max, alpha = 1)

#############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_22to22.5mA_Cav_7.3656GHz&-15dBm_QuBit5.4to5.8GHz&10dBm'
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


X,Y = np.meshgrid(current-0.02,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu', vmin = contrast_min, vmax = contrast_max, alpha = 1)

#############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_22.8to23.064mA_Cav_7.3654GHz&-15dBm_QuBit0.5to5.5GHz&15dBm'
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


X,Y = np.meshgrid(current-0.02,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu')#, vmin = contrast_min, vmax = contrast_max, alpha = 1)

#############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_23.064to23.364mA_Cav_7.3654GHz&-15dBm_QuBit4to5.5GHz&15dBm'
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

X,Y = np.meshgrid(current-0.02,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu')

#############################################################################################################################
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Two_tone_spec'
measurement = 'Two_tone_spec_YOKO_22.86to23mA_Cav_7.3654GHz&-15dBm_QuBit3to4.8GHz&25dBm'
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

X,Y = np.meshgrid(current-0.02,freq)
plt.figure(1)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu')
##############################################################################################################################
###################################################    Theory    #############################################################
##############################################################################################################################
'''
#Define constants
e = 1.602e-19    #Fundamental charge
h = 6.62e-34    #Placnk's constant
phi_o = h/(2*e) #Flux quantum

"""
First section of the script attempts to plot the energies vs external flux
"""
#Hamiltonian definition
def Ho(N,E_l, E_c, E_j_sum, d, phi_squid, phi_ext):
    E_j1 = 0.5*E_j_sum*(1+d)
    E_j2 = 0.5*E_j_sum*(1-d)
    a = tensor(destroy(N))
    mass = 1.0/(8.0*E_c)
    w = np.sqrt(8.0*E_c*E_l)
    phi = (a+a.dag())*(8*E_c/E_l)**(0.25)/np.sqrt(2)
    na = 1j*(a.dag()-a)*(E_l/(8*E_c))**(0.25)/np.sqrt(2)
    ope1 = 1j*(-phi + phi_ext)
    ope2 = 1j*(phi - phi_ext + phi_squid) # phi_squid and phi_ext here are the external phases, or normalized flux, = flux*2pi/phi_o
    H = 4.0*E_c*na**2 + 0.5*E_l*(phi)**2 - 0.5*E_j1*(ope1.expm() + (-ope1).expm()) - 0.5*E_j2*(ope2.expm() + (-ope2).expm())
    return H.eigenenergies()


def trans_energies(N, E_l, E_c, E_j_sum, d, A_j, A_c, B_coeff, beta_squid, beta_ext, level_num, current, iState):  
    B_field = current*B_coeff*1e-4  # in T, this depends on a seperate measurement 
    phi_squid = B_field*A_j # these are flux, not normalized
    phi_ext = B_field*A_c
    trans_energy = np.zeros((level_num-iState,len(phi_ext))) 
    for idx in range(len(phi_ext)):
        energies = Ho(N,E_l, E_c, E_j_sum, d, 2*np.pi*(phi_squid[idx]/phi_o - beta_squid), 2*np.pi*(phi_ext[idx]/phi_o - beta_ext)) #normalize the flux -> phase here    
        for level in range(iState+1,level_num):
            trans_energy[level-iState,idx] = energies[level]-energies[iState]
    return trans_energy  
    

########################################################################

N = 50
E_l = 0.722729827116
E_c = 0.552669197076
E_j_sum = 17.61374383
A_j = 4.76321410213e-12
A_c = 1.50075181762e-10
d = 0.125005274368
beta_squid = 0.129912406349
beta_ext = 0.356925557542

B_coeff = 60 / 28.53 * 45.56
level_num = 5
current = np.linspace(0.025, 0.03, 501)
energies = np.zeros((len(current),level_num))

# iState = 0
# spectrum = trans_energies(N, E_l, E_c, E_j_sum, d, A_j, A_c, B_coeff, beta_squid, beta_ext, level_num, current, iState)
# for idx in range(iState,level_num):
#     line = plt.plot(current*1e3, spectrum[idx,:])  # transition from state (iState)
#     plt.setp(line,linewidth=2.0, linestyle ='-', color = "black", alpha=0.5)
    # line = plt.plot(current, spectrum[idx,:]+10.304)  # transition from state (iState)
    # plt.setp(line,linewidth=2.0, linestyle ='--', color = "black", alpha=0.5)
    # line = plt.plot(current, -spectrum[idx,:]+10.304)  # transition from state (iState)
    # plt.setp(line,linewidth=2.0, linestyle ='--', color = "black", alpha=0.5)

# iState = 1
# spectrum = trans_energies(N, E_l, E_c, E_j_sum, d, A_j, A_c, B_coeff, beta_squid, beta_ext, level_num, current, iState)
# for idx in range(iState,level_num):
    # line = plt.plot(current, spectrum[idx-iState,:])  # transition from state (iState)
    # plt.setp(line,linewidth=2.0, linestyle ='-', color = "red", alpha=0.5)
    # line = plt.plot(current, spectrum[idx-iState,:]+10.304)  # transition from state (iState)
    # plt.setp(line,linewidth=2.0, linestyle ='--', color = "red", alpha=0.5)
    # line = plt.plot(current, -spectrum[idx-iState,:]+10.304)  # transition from state (iState)
    # plt.setp(line,linewidth=2.0, linestyle ='-.', color = "red", alpha=0.5)
'''
# plt.grid()
plt.show()

