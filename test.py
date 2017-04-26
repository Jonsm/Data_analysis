import numpy as np
import matplotlib.pyplot as plt

directory = "D:\Data\Fluxonium #10_7.5GHzCav\T1"
fname = "042117_T1_auto_28.45to28.6mA_twoToneResult.csv"
path = directory + "\\" + fname
data = np.genfromtxt(path)[1::]
freq = data[:,1]
phase = np.unwrap(data[:,3])
# print freq
# print phase
print np.cos(np.pi/3)
plt.plot(phase)
plt.show()

