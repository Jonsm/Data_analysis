from qutip import*
from numpy import pi, sqrt

q1 = (basis(2,0) + 2*basis(2,1)).unit()
print (ket2dm(q1))
q2 = basis(2,0)
q3 = basis(2,0)
phi0 = tensor(q1,q2,q3)
#Create Bell stateand tensor product
phi_bell = cnot(N=3, control=1, target=2)*tensor(q1,snot()*q2, q3)

#Bell measurement
phi1 = cnot(N=3, control=0, target=1)*phi_bell
phi2 = snot(N=3, target=0)*phi1

#Conditional gate
phi3 = cnot(N=3, control=1, target=2)*phi2
phi4 = (cphase(pi, N=3, control = 1, target = 2))*phi3
projector = tensor(qeye(2),qeye(2),q1*q1.dag())
measured = projector*phi4
print (phi0.ptrace(0))
print (phi4.ptrace(2))
print (measured.ptrace(2))




