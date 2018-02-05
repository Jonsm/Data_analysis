from matplotlib import pyplot as plt
import numpy as np
from qutip import*

#File path
directory = 'D:\Data\Fluxonium #13\T1'
measurement = 'T1_auto_input_31.07to31.41mA.csv'
path = directory + '\\' + measurement

e = 1.602e-19    #Fundamental charge
h = 6.62e-34    #Placnk's constant
phi_o = h/(2*e) #Flux quantum
N = 50
B_coeff = 25.5
def trans_energy(current, E_l, E_c, E_j, A, offset):
    energy = np.zeros(len(current))
    flux = current * B_coeff * A * 1e-4
    phi_ext = (flux/phi_o-offset) * 2 * np.pi
    a = tensor(destroy(N))
    phi = (a + a.dag()) * (8.0 * E_c / E_l) ** (0.25) / np.sqrt(2.0)
    na = 1.0j * (a.dag() - a) * (E_l / (8 * E_c)) ** (0.25) / np.sqrt(2.0)
    for idx in range(len(current)):
        ope = 1.0j * (phi - phi_ext[idx])
        H = 4.0 * E_c * na ** 2.0 + 0.5 * E_l * phi ** 2.0 - 0.5 * E_j * (ope.expm() + (-ope).expm())
        energy[idx] = H.eigenenergies()[1] - H.eigenenergies()[0]
    return energy

E_l = 1.0168105
E_c = 0.835632
E_j = 2.9964865
A = 2.738042e-10
offset = 0.017897167

current = np.linspace(31.07-0.115, 31.41-0.115, 35)*1e-3
energy = trans_energy(current, E_l, E_c, E_j, A, offset)
energy = np.round(energy, decimals = 3)
current = current*1e3+0.115
input_dat = np.array([current, energy]).transpose()
np.savetxt(path, input_dat, delimiter =',')
test = np.genfromtxt(path, delimiter = ',')

plt.plot(current, energy)
plt.show()