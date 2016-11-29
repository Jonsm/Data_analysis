from matplotlib import pyplot as plt
import numpy as np

#File path
directory = 'D:\Data\Fluxonium #10_New software'

measurement = 'T1_auto.txt'
path = directory + '\\' + measurement
phase_data = np.genfromtxt(path)[1:,1]

avg_num = 50
pts_num = 20
phase_sum = np.zeros(pts_num)
time = np.linspace(0, 1, pts_num) #arbitrary unit

for count in range(avg_num):
    phase_temp = np.unwrap(phase_data[count*pts_num : (count+1)*(pts_num)])
    phase_sum += phase_temp

phase_avg = phase_sum / avg_num
plt.plot(time, phase_avg)
plt.show()

# x = np.linspace(1,100,100)
# print x
# for i in range(5):
#     print x[i*20:(i+1)*20]