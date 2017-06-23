import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
directory = "D:\Data\Fluxonium #10"
fname = "One tune spectroscopy_YOKO 0mAto50mA_ qubit tone off_Cav_10p30GHz to 10p32GHz_1dBm_pulse_4000_2800_after 2nd thermal cycle"
path = directory + '\\' + fname
freq = np.genfromtxt(path + '_Freq.csv', delimiter = ',')/1e9
phase = np.genfromtxt(path + '_Phase.csv', delimiter = ',')
mag = np.genfromtxt(path + '_Mag.csv', delimiter = ',')

phase = phase[80,:]*np.pi/180
# delay = (phase[-1] - phase[0])/(freq[-1] - freq[0])
# phase = phase - freq*delay
phase = phase - np.mean(phase)
mag = mag[80,:]
mag = 10.0**(mag/20.0) #linear

real = mag*np.cos(phase)
imag = mag*np.sin(phase)
plt.figure(1)
plt.plot(freq, phase)
plt.figure(2)
plt.plot(freq, mag)
tofit = np.array([real, imag]).flatten()
fo = freq[np.argmin(mag)]

def S21(f,Qi,Qc,Qci,tau1,tau2,tau3):
    Qc = Qc + 1j*Qci
    x=(f-fo)/fo
    S = (Qc+2j*Qc*Qi*x)/(Qi+Qc+2j*Qc*Qi*x)
    S = S*tau1*np.exp(1j*(tau2+f*tau3))
    return S

def func(f,Qi,Qc,Qci,tau1,tau2,tau3):
    Qc = Qc + 1j*Qci
    x=(f-fo)/fo
    S = (Qc+2j*Qc*Qi*x)/(Qi+Qc+2j*Qc*Qi*x)
    S = S*tau1*np.exp(1j*(tau2+f*tau3))
    return np.array([np.real(S), np.imag(S)]).flatten()


# guess = ([5000,2000, 500, 1, 0, 0])
# qopt,qcov = curve_fit(func, freq, tofit, guess)
#
# freq_nice = np.linspace(freq[0], freq[-1], 1000)
# plt.figure(1)
# plt.plot(freq_nice, np.real(S21(freq_nice, *qopt)))
# plt.figure(2)
# plt.plot(freq_nice, np.imag(S21(freq_nice, *qopt)))
#
# Qi, Qc, Qci, t1, t2, t3 = qopt
#
# print ((1/Qi + 1/Qc)*fo*1e9/1e6)
plt.show()

