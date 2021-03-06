import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

#File path
directory = 'D:\Data\Fluxonium #10_7.5GHzCav\One_tone_spec'
measurement = 'One_tone_spec_0mA_7.35to7.37GHz_-15to-30dBm'
path = directory + '\\' + measurement

#Read data
current = np.genfromtxt(path + '_POWER.csv')
current = current[1:-1]
freq = np.genfromtxt(path + '_FREQ.csv')
freq = freq[1::]
phasemag = np.genfromtxt(path + '_PHASEMAG.csv')
phase = phasemag[1::,0] #phase is recorded in rad
# phase = np.unwrap(phase)*180/(np.pi)
mag = phasemag[1::,1]
magdB = 10*np.log10(mag)
Z_mag = np.zeros((len(current), len(freq)))
Z_phase = np.zeros((len(current), len(freq)))
for idx in range(len(current)):
    temp = np.unwrap(phase[idx*len(freq):(idx+1)*len(freq)])
    delay = (temp[-1]-temp[0]) / (freq[-1]-freq[0])
    temp = temp - freq*delay
    Z_phase[idx,:] = temp - np.min(temp)
    # Z_phase[idx,:] = np.diff(temp - np.min(temp))
    temp = mag[idx*len(freq):(idx+1)*len(freq)]
    Z_mag[idx,:] = temp - np.min(temp)

Z=Z_phase
#Default plot at index 0
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
l, =plt.plot(freq,Z[0])

M = np.zeros((len(current), len(freq)))
for idx in range(len(current)):
    temp = mag[idx*len(freq):(idx+1)*len(freq)]
    M[idx,:] = temp - np.average(temp)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
l, =plt.plot(freq,M[0])
ax.set_xlabel('Freq (GHz)')
ax.set_ylabel('Phase (deg)')

#Slider defined here
axcolor = 'lightgoldenrodyellow'
axFlux = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
sFlux = Slider(axFlux, 'Index', 0, len(current)-1, valinit = 0, valfmt='%0.00f')

def update(flux):
    idx = int(sFlux.val)
    # idx = current.tolist().index(flux)
    l.set_ydata(M[idx])
    plt.title(current[idx])

sFlux.on_changed(update)

plt.show()
