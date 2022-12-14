import numpy as np
from matplotlib import pyplot as plt

def unitstep(t):
    if (t < 0): return 0
    elif (t == 0):return 0.5
    else: return 1

def v1(t):
    if (t >= 0): return 2/3*(1 + np.exp(-t*1.5e6))*unitstep(t)
    else: return 0


k = np.linspace(0,1e-5,100000)

Vstim = []
for i in k:
    Vstim.append(v1(i))
Vanalysis = np.loadtxt('/home/bhanu/v2.txt')

plt.plot(k,Vstim[:])
plt.plot(Vanalysis[:,0],Vanalysis[:,1],'.')
plt.ylabel("$V_{C_{0}}(t) (V)$")
plt.xlabel("$t(s)")
plt.grid()
plt.legend(['Simulation','analysis'])
plt.show()
