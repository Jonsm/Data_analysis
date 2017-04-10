from matplotlib import pyplot as plt
import numpy as np
import h5py
from scipy.optimize import curve_fit

directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Rabi'
# directory = 'D:\Data\Fluxonium #10_7.5GHzCav\Raman'
fname = 'Rabi_YOKO_28.583mA_Cav7.3649GHz_-15dBm_Qubit0.5041GHz_25dBm_Count50_TimeStep20.h5'
path = directory + '\\' + fname
pts_num = 50
time_step = 20
time = np.linspace(0, pts_num*time_step, pts_num)
#Read data and fit
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    count = np.array(hf.get('count'))
    phase_raw = hf.get('PHASEMAG_Phase0')
    phase = phase_raw[0, 0]
    phase = np.unwrap(phase)*180/np.pi
    phase = phase - np.min(phase)

plt.plot(time, phase)
plt.grid()
plt.show()