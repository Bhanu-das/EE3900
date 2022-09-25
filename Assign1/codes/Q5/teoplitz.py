from scipy.linalg import toeplitz
import numpy as np
n = np.arange(14)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2
nh=len(h)
x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
nx = len(x)
column = []
for i in h:
    column.append(i)
for j in range(0, 5):
    column.append(0)
row = []
row.append(h[0])
for k in range(0, 5):
    row.append(0)
matrix = toeplitz(row, column)
x_t = np.transpose(x)
matrix_t = np.transpose(matrix)
np.dot(matrix_t, x)
y_2 = np.zeros(nx+nh-1)

for k in range(0,nx+nh-1):
	for n in range(0,nh):
		if k-n >= 0 and k-n < nx:
			y_2[k]+=x[k-n]*h[n]

print(y_2)
