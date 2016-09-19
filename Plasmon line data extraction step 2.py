from scipy.optimize import curve_fit
import numpy as np
from qutip import*
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Palatino']})
rc('text', usetex=True)
plt.close("all")

#####################################################################################
#####################################################################################
fig =plt.figure()

rough_fluxes1 =[
[0.04169],
[0.04177],
[0.04194],
[0.04207],
[0.04225],
[0.04242],
[0.04258],
[0.04270],
[0.04280],
[0.04291],
[0.04298],
[0.04399],
[0.04419],
[0.04431],
[0.04454],
[0.04472],
[0.04481],
[0.04502],
[0.04505],
[0.04508],
[0.04510],
[0.04593],
[0.04595],
[0.04598],
[0.04606],
[0.0461]
]
rough_fluxes2 =[
[0.04620],
[0.04630],
[0.04640],
[0.04650],
[0.04660],
[0.04670],
[0.04680],
[0.04690],
[0.04704],
[0.0471],
[0.0472],
[0.04724]
]

flux_points1 = np.asarray(rough_fluxes1)
freq_points1 = np.zeros(len(flux_points1))
flux_points2 = np.asarray(rough_fluxes2)
freq_points2 = np.zeros(len(flux_points2))

####################################################################################
#Spectrum at the bottom :) 
directory = 'G:\Projects\Fluxonium & qubits\Data\Fluxonium #10\Raw data'
measurement = 'S21_39to50mA_currentMode_qubit_0dBm_cav_1dBm_avg20K_pulse(test)'
path_data = directory + '\\' + measurement + '_Phase.csv'
path_freq = directory + '\\' + measurement + '_Freq.csv'
path_cur = directory + '\\' + measurement + '_Current.csv'

RawData = np.genfromtxt(path_data, delimiter =',')
Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
Current = np.genfromtxt(path_cur, delimiter =',')
for idx in range(len(Current)-1):
    if (idx%10) == 0:
        f = Freq[idx]
        Z = RawData[idx:idx+11].transpose()
        I = Current[idx:idx+11]
        for idiot, jon_snow in enumerate (flux_points1):   #Iterate through the flux points of interest
            for brutal, ramsey_bolton in enumerate (I): #Iterate through the current (flux) data to match the flux points of interest
                if jon_snow == ramsey_bolton:                 #If data matches the points of interest, then find the transition frequency.                     
                    index_min = np.argmin(Z.transpose()[brutal])
                    freq_points1[idiot] = f[index_min]
                    
        X, Y = np.meshgrid(I, f)
        plt.pcolormesh(X, Y, Z, cmap=cm.GnBu_r, vmin =-5, vmax = 0)

directory = 'G:\Projects\Fluxonium & qubits\Data\Fluxonium #10\Raw data'
measurement = 'S21_46to48mA_currentMode_qubit_0dBm_cav_5dBm_avg20K_pulse(test)'
path_data = directory + '\\' + measurement + '_Phase.csv'
path_freq = directory + '\\' + measurement + '_Freq.csv'
path_cur = directory + '\\' + measurement + '_Current.csv'

RawData = np.genfromtxt(path_data, delimiter =',')
Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
Current = np.genfromtxt(path_cur, delimiter =',')
for idx in range(len(Current)-1):
    if (idx%10) == 0:
        f = Freq[idx]
        Z = RawData[idx:idx+11].transpose()
        I = Current[idx:idx+11]
        for idiot, jon_snow in enumerate (flux_points2):   #Iterate through the flux points of interest
            for brutal, ramsey_bolton in enumerate (I): #Iterate through the current (flux) data to match the flux points of interest
                if jon_snow == ramsey_bolton:                 #If data matches the points of interest, then find the transition frequency.                     
                    index_min = np.argmin(Z.transpose()[brutal])
                    freq_points2[idiot] = f[index_min]
                    
        X, Y = np.meshgrid(I, f)
        plt.pcolormesh(X, Y, Z, cmap=cm.GnBu_r, vmin =-5, vmax = 0)

#############################################################
flux_points = np.zeros(len(flux_points1) + len(flux_points2))
freq_points = np.zeros(len(flux_points))

for idx, value in enumerate (flux_points1):
    flux_points[idx] = value
for idx, value in enumerate (flux_points2):
    flux_points[len(flux_points1)+idx] = value

for idx, value in enumerate (freq_points1):
    freq_points[idx] = value
for idx, value in enumerate (freq_points2):
   freq_points[len(freq_points1)+idx] = value
            
plt.plot(flux_points, freq_points, '-o')  


# this part of the script simply plots the spectrum on top for comparison

#directory = 'G:\Projects\Fluxonium & qubits\Data\Fluxonium #10\Raw data'
#measurement = 'S21_0to20mA_currentMode_qubit_n30dBm_cav_1dBm_avg50K_pulse25'
#path_data = directory + '\\' + measurement + '_Phase.csv'
#path_freq = directory + '\\' + measurement + '_Freq.csv'
#path_vol = directory + '\\' + measurement + '_Current.csv'
#
#RawData = np.genfromtxt(path_data, delimiter =',')
#Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
#Voltage = np.genfromtxt(path_vol, delimiter =',')
##Voltage = np.linspace(0,3,3000)
#for idx in range(len(Voltage)-1):
#    if (idx%10) == 0:
#        f = Freq[idx]
#        Z = RawData[idx:idx+11].transpose()
#        V = Voltage[idx:idx+11]
#        X, Y = np.meshgrid(V, f)
#        plt.pcolormesh(X, Y, Z, cmap=cm.GnBu_r, vmin =-5, vmax = 0)
#
#directory = 'G:\Projects\Fluxonium & qubits\Data\Fluxonium #10\Raw data'
#measurement = 'S21_20to30mA_currentMode_qubit_n5dBm_cav_5dBm_avg20K_pulse(test)'
#path_data = directory + '\\' + measurement + '_Phase.csv'
#path_freq = directory + '\\' + measurement + '_Freq.csv'
#path_vol = directory + '\\' + measurement + '_Current.csv'
#
#RawData = np.genfromtxt(path_data, delimiter =',')
#Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
#Voltage = np.genfromtxt(path_vol, delimiter =',')
##Voltage = np.linspace(0,3,3000)
#for idx in range(len(Voltage)-1):
#    if (idx%10) == 0:
#        f = Freq[idx]
#        Z = RawData[idx:idx+11].transpose()
#        V = Voltage[idx:idx+11]
#        X, Y = np.meshgrid(V, f)
#        plt.pcolormesh(X, Y, Z, cmap=cm.GnBu_r, vmin =-5, vmax = 0)    
#        
#directory = 'G:\Projects\Fluxonium & qubits\Data\Fluxonium #10\Raw data'
#measurement = 'S21_30to32mA_currentMode_qubit_n5dBm_cav_5dBm_avg20K_pulse(test)'
#path_data = directory + '\\' + measurement + '_Phase.csv'
#path_freq = directory + '\\' + measurement + '_Freq.csv'
#path_vol = directory + '\\' + measurement + '_Current.csv'
#
#RawData = np.genfromtxt(path_data, delimiter =',')
#Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
#Voltage = np.genfromtxt(path_vol, delimiter =',')
##Voltage = np.linspace(0,3,3000)
#for idx in range(len(Voltage)-1):
#    if (idx%10) == 0:
#        f = Freq[idx]
#        Z = RawData[idx:idx+11].transpose()
#        V = Voltage[idx:idx+11]
#        X, Y = np.meshgrid(V, f)
#        plt.pcolormesh(X, Y, Z, cmap=cm.GnBu_r, vmin =-5, vmax = 0)
#
#directory = 'G:\Projects\Fluxonium & qubits\Data\Fluxonium #10\Raw data'
#measurement = 'S21_32to39mA_currentMode_qubit_n5dBm_cav_5dBm_avg20K_pulse(test)'
#path_data = directory + '\\' + measurement + '_Phase.csv'
#path_freq = directory + '\\' + measurement + '_Freq.csv'
#path_vol = directory + '\\' + measurement + '_Current.csv'
#
#RawData = np.genfromtxt(path_data, delimiter =',')
#Freq = np.genfromtxt(path_freq, delimiter =',')/1e9
#Voltage = np.genfromtxt(path_vol, delimiter =',')
##Voltage = np.linspace(0,3,3000)
#for idx in range(len(Voltage)-1):
#    if (idx%10) == 0:
#        f = Freq[idx]
#        Z = RawData[idx:idx+11].transpose()
#        V = Voltage[idx:idx+11]
#        X, Y = np.meshgrid(V, f)
#        plt.pcolormesh(X, Y, Z, cmap=cm.GnBu_r, vmin =-5, vmax = 0)                                
##########################################################################################################################################################################
##########################################################################################################################################################################

#Define constants
e = 1.602e-19    #Fundamental charge
h = 6.62e-34    #Placnk's constant
phi_o = h/(2*e) #Flux quantum

"""
First section of the script attempts to plot the energies vs external flux
"""
#Hamiltonian definition
def Ho(N, E_l, E_c, E_j_sum, d, phi_squid, phi_ext):
    E_j1 = 0.5*(E_j_sum + d*E_j_sum)
    E_j2 = 0.5*(E_j_sum - d*E_j_sum)
    a = tensor(destroy(N))
    mass = 1.0/(8.0*E_c)
    w = sqrt(8.0*E_c*E_l)
    phi = (a+a.dag())*(8.0*E_c/E_l)**(0.25)/np.sqrt(2.0)
    na = 1j*(a.dag()-a)*(E_l/(8.0*E_c))**(0.25)/np.sqrt(2.0)
    ope1 = 1j*(-phi + phi_ext)
    ope2 = 1j*(phi - phi_ext + phi_squid)
    H = 4.0*E_c*na**2 + 0.5*E_l*(phi)**2.0 - 0.5*E_j1*(ope1.expm() + (-ope1).expm()) - 0.5*E_j2*(ope2.expm() + (-ope2).expm())
    return H.eigenenergies() 
    
def Ho_alt(N,E_l, E_c, E_j_sum, d, phi_squid, phi_ext):
    E_j = E_j_sum*np.cos(phi_squid/2.0)*np.sqrt(1+(d*np.tan(phi_squid/2.0))**2.0)
    theta = np.arctan(d*np.tan(phi_squid/2.0))
    a = tensor(destroy(N))
    mass = 1.0/(8.0*E_c)
    w = sqrt(8.0*E_c*E_l)
    phi = (a+a.dag())*(8*E_c/E_l)**(0.25)/np.sqrt(2)
    na = 1j*(a.dag()-a)*(E_l/(8*E_c))**(0.25)/np.sqrt(2)
    ope = 1j*(phi - phi_ext + theta + phi_squid/2.0) # phi_squid and phi_ext here are the external phases, or normalized flux, = flux*2pi/phi_o
    H = 4.0*E_c*na**2 + 0.5*E_l*(phi)**2 - 0.5*E_j*(ope.expm() + (-ope).expm())
    return H.eigenenergies()
        
def trans_energies(current, E_l, E_c, E_j_sum, A_j, A_c, d, offset_squid, offset_ext): 
    N=50    
    B_coeff = 60
    B_field = current*B_coeff*1e-4
    phi_squid = B_field*A_j
    phi_ext = B_field*A_c
    trans_energy = np.zeros(len(current))     
    for idx in range(len(current)):
        energies = Ho(N, E_l, E_c, E_j_sum, d, 2*np.pi*(phi_squid[idx]/phi_o - offset_squid), 2*np.pi*(phi_ext[idx]/phi_o - offset_ext))     
        trans_energy[idx]=energies[1]-energies[0]
    return trans_energy    
    
def plot_trans_energies(N, E_l, E_c, E_j_sum, d, phi_squid, phi_ext, offset_squid, offset_ext, level_num, current):  
    energy0 = np.empty((level_num,len(phi_ext)),dtype=float) 
    energy1 = np.empty((level_num,len(phi_ext)),dtype=float)
    energy2 = np.empty((level_num,len(phi_ext)),dtype=float) 
    for idx in range(len(phi_ext)):
        energies = Ho(N,E_l, E_c, E_j_sum, d, 2*np.pi*(phi_squid[idx]/phi_o- offset_squid), 2*np.pi*(phi_ext[idx]/phi_o- offset_ext))
        #1 photon
        for level in range(0,level_num):
            energy0[level,idx]=energies[level]-energies[0]
            #energy1[level,idx]=energies[level]-energies[1]
            #energy2[level,idx]=energies[level]-energies[2]
    for idx in range(0,level_num):    
        line = plt.plot(current, energy0[idx,:])
        plt.setp(line,linewidth=1.0, linestyle ='-', color = "black", alpha=0.7)
        #line = plt.plot(current, energy1[idx,:])
        #plt.setp(line,linewidth=1.0, linestyle ='-', color = "red", alpha=0.7)  
        
    return   

##########################################################################################################################################################################
##########################################################################################################################################################################
#Energy scale in GHz                                                            
E_l_guess = 0.72
E_c_guess = 0.538
E_j_sum_guess = 22.35

#Define external parameters
A_j_guess = 3.78e-12  #in m
A_c_guess = 147.2e-12
d_guess = 0.102                                        
offset_squid_guess = 0
offset_ext_guess=0                                                  
guess = ([E_l_guess, E_c_guess, E_j_sum_guess, A_j_guess, A_c_guess, d_guess, offset_squid_guess, offset_ext_guess])                                                           
opt, cov = curve_fit(trans_energies, flux_points, freq_points, guess) 
                                                                     
################################################################################################################################################################################

E_l_fit = opt[0]
E_c_fit = opt[1]
E_j_fit = opt[2]
A_j_fit = opt[3]
A_c_fit = opt[4]
d_fit = opt[5]
offset_squid_fit = opt[6]
offset_ext_fit = opt[7]

print 'E_l=' + str(E_l_fit) + ', E_c=' + str(E_c_fit) + ', E_j_sum=' + str(E_j_fit) + '\n' + 'A_j=' + str(A_j_fit) + ', A_c=' + str(A_c_fit) + ', d=' + str(d_fit)# + \
', beta_squid=' + str(offset_squid_fit) + ', beta_ext=' + str(offset_ext_fit)
#Only plot the first excited state transition

current = np.linspace(0.04,0.05,1000)
plt.plot (current, trans_energies(current, E_l_fit, E_c_fit, E_j_fit, A_j_fit, A_c_fit, d_fit), color = "black", alpha=0.7) 
#plt.plot (current, trans_energies(current, E_l_guess, E_c_guess, E_j_sum_guess, A_j_guess, A_c_guess, d_guess, beta_squid_guess, beta_ext_guess)) 

#Plot other transition    
N=50
level_num = 5
B_coeff = 60
B_field = current*B_coeff*1e-4
phi_squid = B_field*A_j_fit
phi_ext = B_field*A_c_fit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
fig = plt.figure(1)
plot_trans_energies(N, E_l_fit, E_c_fit, E_j_fit, d_fit, phi_squid, phi_ext, offset_squid_fit, offset_ext_fit, level_num, current)
plt.ylim([0,12]) 
plt.grid()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
plt.show()

