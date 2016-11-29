from matplotlib import pyplot as plt
import numpy as np

#File path
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'test.dat'
path = directory + '\\' + measurement

data = np.genfromtxt(path)
phase = np.unwrap(data[1::,0])*180/np.pi
mag =  data[1::,1]
freq = np.linspace(10.3,10.4,len(phase))
slope = (phase[-1]-phase[0])/(freq[-1]-freq[0])
plt.plot(freq,mag)
plt.show()
plt.plot(freq,phase-slope*freq)
plt.show()