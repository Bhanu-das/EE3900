from cmath import exp
import numpy as np
from matplotlib import pyplot as plt

def unitstep(t):
    if (t < 0): return 0
    elif (t == 0):return 0.5
    else: return 1

def v(t):
    k = 1-np.exp((-1.5*(10**6) * t))
    return (4/3)*k*unitstep(t)

k = np.linspace(0,1e-5,100000)
t = np.linspace(0,1e-5,100)
print(k)

Varr=[]
for i in k :
    Varr.append(v(i))

Vanalysis = np.loadtxt('/home/bhanu/v1.txt')

plt.plot(k,Varr[:])
plt.plot(Vanalysis[:,0],Vanalysis[:,1],'.')
plt.grid()
plt.xlabel("$t(s)$'")
plt.ylabel("$V_{C_{0}}(t) (V)$'")
plt.legend(['Stimulation, Analysis'])
plt.show()
