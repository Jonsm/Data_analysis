from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


#File path
directory = 'D:\Data\Fluxonium #10_python code by Jon\T1_T2_(0to1)_YOKO_43p75to45p4mA\T1_YOKO_44p7mA\T1s'
measurement = 'generic_sequence_39'

path = directory + '\\' + measurement

def func(x, a, b, c, d):
    return a*np.exp(-(x-c)/b) + d
count = 0
for i in range(0,10):
    # if i ==8:
    #     continue
    #Read data
    time = np.genfromtxt(path + '_time' + str(i) + '.csv')
    phase= np.genfromtxt(path + '_phase' + str(i) + '.csv')
    phase = np.unwrap(phase)*180/np.pi
    phase = -phase
    phase = phase - np.min(phase)
    guessA= max(phase)-min(phase)

    guess = [guessA, 1e-4, 0, 0]
    try:
        popt, pcov = curve_fit(func, time*1e-9, phase, guess)
    except RuntimeError:
        continue
    a,b,c,d = popt

    perr = np.diag(pcov)
    count = count + 1
    # plt.figure(1)
    # plt.plot(time/1e3, phase,'r.')
    # plt.plot(time/1e3, func(time*1e-9, a,b,c,d),'b-')
    # plt.figure(2)
    # plt.semilogy(time/1e3, phase,'r.')
    # plt.semilogy(time/1e3, func(time*1e-9, a,b,c,d),'b-')
    # print (i)
    # print('T1_'+str(i)+'=' + str(b*1e6) + 'us')
    # print('T1 error=' + str(np.sqrt(perr[1])*1e6)+ 'us')
    if count == 1:
        phaseall = phase
    else:
        phaseall = phaseall + phase

###########################################################
# Curve fitting phase all
###########################################################
# '''
phaseall = phaseall/count
guessA= max(phaseall)-min(phaseall)
guess = [guessA, 1e-4, 0, 0]
popt, pcov = curve_fit(func, time*1e-9, phaseall, guess)

a,b,c,d = popt

perr = np.diag(pcov)


# print(popt)
#print(np.diag(pcov))
print('T1_avg=' + str(b*1e6) + 'us')
# print('T1 error=' + str(np.sqrt(perr[1])*1e6)+ 'us')

plt.figure(1)
plt.plot(time/1e3, phaseall, 's-', time/1e3, func(time*1e-9, a,b,c,d), '-')
# plt.xlabel('Time(us)')
# plt.ylabel('Phase')
# plt.figure(2)
# plt.semilogy(time/1e3, phaseall, 'm.', time/1e3, func(time*1e-9, a,b,c,d), 'g-')
# plt.xlabel('Time(us)')
# plt.ylabel('Phase')
plt.tick_params(labelsize = 18.0)
plt.show()
# '''
