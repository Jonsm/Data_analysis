import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

#File path
directory = 'D:\Data\Fluxonium #11\One_tone_spec'
measurement = 'One_tone_spec_0mA_7.35to7.37GHz_-20to-30dBm'
path = directory + '\\' + measurement

#Read data
power = np.genfromtxt(path + '_POWER.csv')
power = power[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1::]
phasemag = np.genfromtxt(path + '_PHASEMAG.csv')
phase = phasemag[1::,0] #phase is recorded in rad
# phase = np.unwrap(phase)*180/(np.pi)
mag = phasemag[1::,1]
magdB = 10*np.log10(mag)
Z_mag = np.zeros((len(power), len(freq)))
Z_phase = np.zeros((len(power), len(freq)))
for idx in range(len(power)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    delay = (temp[-1]-temp[0]) / (freq[-1]-freq[0])
    temp = temp - freq*delay
    Z_phase[idx,:] = temp - np.min(temp)
    # Z_phase[idx,:] = np.diff(temp - np.min(temp))
    temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z_mag[idx,:] = temp - np.min(temp)

Z=Z_mag

#Default plot at index 0
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
l, =plt.plot(freq, Z[0])

#Slider defined here
axcolor = 'lightgoldenrodyellow'
axFlux = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
sFlux = Slider(axFlux, 'Index', 0, len(power)-1, valinit = 0, valfmt='%0.00f')

def update(flux):
    idx = int(sFlux.val)
    # idx = current.tolist().index(flux)
    l.set_ydata(Z[idx])
    plt.title(power[idx])

sFlux.on_changed(update)

plt.show()