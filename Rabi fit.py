from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Rabi'
fname = 'Rabi_YOKO_28.575mA_Cav7.3649GHz_-15dBm_Qubit0.5046GHz_16dBm_Count50_TimeStep100.h5'
path = directory + '\\' + fname
time = np.linspace(0,50*100,50)
#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    phase = phase_raw[0, 0]
    phase =np.unwrap(phase)

plt.plot(time, phase)
plt.show()