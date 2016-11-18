
from matplotlib import pyplot as plt
import numpy as np
import h5py

#File path
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'Rabi_test_PHASEMAG.h5'
path = directory + '\\' + measurement
with h5py.File(path,'r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    data = hf.get('demod_Phase0')
    np_data = np.array(data)[0,0,:]
    print np_data

plt.plot(np.unwrap(np_data))
plt.show()