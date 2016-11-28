
from matplotlib import pyplot as plt
import numpy as np
import h5py

#File path
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'T1_auto_35to36p1mA.h5'
path = directory + '\\' + measurement
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    print count
    phase_raw = hf.get('demod_Phase0')
    freq = np.array(hf.get('freq'))
    flux = np.array(hf.get('flux'))
    for idx in range(110):
        phase = -phase_raw[idx,0]
        phase = np.unwrap(phase)
        phase = phase - np.mean(phase)
        phase = phase*180/np.pi
        plt.plot(phase)

plt.show()