from matplotlib import pyplot as plt
import numpy as np
import scipy.optimize as opt

#File path
directory = 'D:\Data\Fluxonium #10_New software'
measurement = 'auto_test_two_tone_result2.txt'
path = directory + '\\' + measurement
imported=np.genfromtxt(path)
ffit=[]
for i in range(2,3):
    print i
    phase = imported[1:,2][201*i:201*(i+1)]
    freq = imported[1:,1][201*i:201*(i+1)]
    phase=np.unwrap(phase)
    measurement = 'Trans_energy_0to1_from_44.04to45.04mA.txt'
    directory = 'D:\Data\Fluxonium #10_New software\Input_for_auto_meas'
    path = directory + '\\' + measurement
    fguess=np.round(np.genfromtxt(path)[40*i+1,1],5)

    def f(x,a,b,c,d):
        return a+b*1/(1+((x-d)/c)**2)

    guess=[np.mean(phase),-0.1,0.05,fguess]
    try:
        func,t=opt.curve_fit(f,freq,phase,guess)
        a,b,c,d = func
        ffit.append(d)
        plt.plot(freq,f(freq,a,b,c,d),'--')
        plt.plot(freq,phase)

        plt.show()
    except RuntimeError:
        print 'fguess used'

plt.plot(ffit)
plt.show()