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

'''
#####################################################################################################################################################################################
#####################################################################################################################################################################################

directory = 'D:\Data\Fluxonium #10'
measurement = 'S21_43to44mA_currentMode_qubit_2p5to3p2GHz_0dBm_cav5dBm_avg50K_pulse(test)'
path_data = directory + '\\' + measurement + '_Phase.csv'
path_freq = directory + '\\' + measurement + '_Freq.csv'
path_current = directory + '\\' + measurement + '_I.csv'

RawData = np.genfromtxt(path_data, delimiter =',')
Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
I = np.genfromtxt(path_current, delimiter =',')
Z = RawData.transpose()
X, Y = np.meshgrid(I,Freq)
plt.pcolormesh(X, Y, Z, cmap=cm.GnBu_r, vmin = -5 , vmax = 0)
########################################################################
directory = 'D:\Data\Fluxonium #10'
measurement = 'S21_43p15to43p85mA_currentMode_qubit_1p5to2p5GHz_0dBm_cav5dBm_avg50K_pulse(test)'
path_data = directory + '\\' + measurement + '_Phase.csv'
path_freq = directory + '\\' + measurement + '_Freq.csv'
path_current = directory + '\\' + measurement + '_I.csv'

RawData = np.genfromtxt(path_data, delimiter =',')
Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
I = np.genfromtxt(path_current, delimiter =',')
Z = RawData.transpose()
X, Y = np.meshgrid(I,Freq)
plt.pcolormesh(X, Y, Z, cmap=cm.GnBu_r, vmin = -5 , vmax = 0)
########################################################################
directory = 'D:\Data\Fluxonium #10'
measurement = 'Two tune spectroscopy_YOKO 43p4to43p6mA_ qubit tone 10p5to11p2GHz_5dBm_Cav_10p304GHz_8dBm_pulse 34us duty2_avg5K'
path_data = directory + '\\' + measurement + '_Phase.csv'
path_freq = directory + '\\' + measurement + '_Freq.csv'
path_current = directory + '\\' + measurement + '_I.csv'

RawData = np.genfromtxt(path_data, delimiter =',')
Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
I = np.genfromtxt(path_current, delimiter =',')-0.00003
Z = RawData.transpose()
X, Y = np.meshgrid(I,Freq)
plt.pcolormesh(X, Y, Z, cmap=cm.RdBu_r, vmin = -5 , vmax = 5)
########################################################################
directory = 'D:\Data\Fluxonium #10'
measurement = 'Two tune spectroscopy_YOKO 43p4to43p6mA_ qubit tone 8p5to10p2GHz_5dBm_Cav_10p304GHz_8dBm_pulse 34us duty2_avg5K'
path_data = directory + '\\' + measurement + '_Phase.csv'
path_freq = directory + '\\' + measurement + '_Freq.csv'
path_current = directory + '\\' + measurement + '_I.csv'

RawData = np.genfromtxt(path_data, delimiter =',')
Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
I = np.genfromtxt(path_current, delimiter =',')-0.00003
Z = RawData.transpose()
X, Y = np.meshgrid(I,Freq)
plt.pcolormesh(X, Y, Z, cmap=cm.RdBu_r, vmin = -5 , vmax = 5)
#####################################################################################################################################################################################
#####################################################################################################################################################################################
directory = 'D:\Data\Fluxonium #10'
measurement = 'S21_39to50mA_currentMode_qubit_0dBm_cav_1dBm_avg20K_pulse(test)'
path_data = directory + '\\' + measurement + '_Phase.csv'
path_freq = directory + '\\' + measurement + '_Freq.csv'
path_cur = directory + '\\' + measurement + '_Current.csv'

RawData = np.genfromtxt(path_data, delimiter =',')
Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
Current = np.genfromtxt(path_cur, delimiter =',')
#Voltage = np.linspace(0,3,3000)
for idx in range(len(Current)-1):
    if (idx%10) == 0:
        f = Freq[idx]
        Z = RawData[idx:idx+11].transpose()
        I = Current[idx:idx+11]
        X, Y = np.meshgrid(I, f)
        plt.pcolormesh(X, Y, Z, cmap=cm.GnBu_r, vmin =-5, vmax = 0)
########################################################################        
directory = 'D:\Data\Fluxonium #10'
measurement = 'S21_46to48mA_currentMode_qubit_0dBm_cav_5dBm_avg20K_pulse(test)'
path_data = directory + '\\' + measurement + '_Phase.csv'
path_freq = directory + '\\' + measurement + '_Freq.csv'
path_cur = directory + '\\' + measurement + '_Current.csv'

RawData = np.genfromtxt(path_data, delimiter =',')
Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
Current = np.genfromtxt(path_cur, delimiter =',')
#Voltage = np.linspace(0,3,3000)
for idx in range(len(Current)-1):
    if (idx%10) == 0:
        f = Freq[idx]
        Z = RawData[idx:idx+11].transpose()
        I = Current[idx:idx+11]
        X, Y = np.meshgrid(I, f)
        plt.pcolormesh(X, Y, Z, cmap=cm.GnBu_r, vmin =-5, vmax = 0)

#####################################################################################################################################################################################
#####################################################################################################################################################################################
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'Two tone spec_YOKO41mA_46mA_Qubit2p5 to 4GHz 5dBm_Cav 10p304GHz 5dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURR.dat')
current = current[1::]/1e3
freq = np.genfromtxt(path + '_FREQ.dat')
freq = freq[1::]
data = np.genfromtxt(path + '_PHASEMAG.dat')
phase = data[1::,0] #phase is recorded in rad
phase = phase#
mag = data[1::,0]

Z = np.zeros((len(current),len(freq)))
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    Z[idx,:] = temp - np.average(temp)
Z = Z*180/(np.pi)
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'GnBu_r', vmin = -5, vmax=0, alpha = 1)
'''
################################################################################
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'Two_tone_spec_YOKO_38to40mA_Qubit_3.5to5GHz_10dBm_Cav_10.3045GHz_5dBm_IF_0.05GHz_measTime_500ns_avg_50000'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_CURR.dat')#*1e3
current = current[1:-1]/1e3 + 0.04*1e-3
freq = np.genfromtxt(path + '_FREQ.dat')
freq = freq[1::]
data = np.genfromtxt(path + '_PHASEMAG.dat')
phase = data[1::,0] #phase is recorded in rad
mag = data[1::,1]
Z = np.zeros((len(current),len(freq)))
# print (phase)
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    Z[idx,:] = temp - np.average(temp)

Z = Z*180/(np.pi)
X,Y = np.meshgrid(current,freq)
plt.pcolormesh(X,Y,Z.transpose(), cmap= 'Reds_r', vmin = -5, vmax=0, alpha = 0.2)

#####################################################################################################################################################################################
#####################################################################################################################################################################################

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
    w = sqrt(8.0*E_c*E_l)
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
            trans_energy[level-iState,idx]=energies[level]-energies[iState]    
    return trans_energy  
    

########################################################################
# '''
N = 50
E_l = 0.746959655208
E_c = 0.547943694372
E_j_sum = 21.9627179709
level_num = 10
B_coeff = 60
A_j = 3.80888914574e-12
A_c = 1.49982268962e-10
beta_squid = 0.00378012644185
beta_ext = 0.341308382441
d=0.0996032153487
current = np.linspace(0.038,0.04,400)

iState = 0
spectrum = trans_energies(N, E_l, E_c, E_j_sum, d, A_j, A_c, B_coeff, beta_squid, beta_ext, level_num, current, iState)
for idx in range(iState,level_num):
    line = plt.plot(current, spectrum[idx,:])  # transition from state (iState)
    plt.setp(line,linewidth=2.0, linestyle ='-', color = "black", alpha=0.5)
    # line = plt.plot(current, spectrum[idx,:]+10.304)  # transition from state (iState)
    # plt.setp(line,linewidth=2.0, linestyle ='--', color = "black", alpha=0.5)
    # line = plt.plot(current, -spectrum[idx,:]+10.304)  # transition from state (iState)
    # plt.setp(line,linewidth=2.0, linestyle ='--', color = "black", alpha=0.5)

iState = 1
spectrum = trans_energies(N, E_l, E_c, E_j_sum, d, A_j, A_c, B_coeff, beta_squid, beta_ext, level_num, current, iState)
for idx in range(iState,level_num):
    line = plt.plot(current, spectrum[idx-iState,:])  # transition from state (iState)
    plt.setp(line,linewidth=2.0, linestyle ='-', color = "red", alpha=0.5)
    # line = plt.plot(current, spectrum[idx-iState,:]+10.304)  # transition from state (iState)
    # plt.setp(line,linewidth=2.0, linestyle ='--', color = "red", alpha=0.5)
    # line = plt.plot(current, -spectrum[idx-iState,:]+10.304)  # transition from state (iState)
    # plt.setp(line,linewidth=2.0, linestyle ='-.', color = "red", alpha=0.5)
    
    

# '''
#plt.grid("on")
plt.xlabel("YOKO I (mA)")
plt.ylabel("Freq (GHz)")
#plt.ylim([3.2,3.24])
#plt.title(measurement)
plt.tick_params(labelsize=10)
# plt.colorbar()
plt.show()
#plt.show()

