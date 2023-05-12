import numpy as np
from numpy import linalg
from functools import reduce

def MNK(x0,y0,m):
    Ma = []
    Mb = []
    for i in range(m+1):
        arr = []
        for j in range(m+1):
            if i==0 and j==0:
                arr.append(len(x))
            else:
                arr.append(reduce(lambda x1,x2: x1+x2, [xn**(i+j) for xn in x]))
        Ma.append(arr)
        Mb.append(reduce(lambda x1,x2: x1+x2, [y[n]*(x[n])**i for n in range(len(y))]))
    res = np.linalg.solve(Ma,Mb)
    return res

def y_pred(a,x):
    res=a[0]
    for i in range(1,len(a)):
        res+=a[i]*x**i
    return res

def MSE(y,a_pred,x):
    res = 0
    for i in range(len(y)):
        res+=(y[i]-y_pred(a_pred,x[i]))**2
    res**0.5
    return res

x = list(map(float, input().split()))
y = list(map(float, input().split()))
m = int(input())

result = MNK(x,y,m)

print(*result)
for i in range(len(result)):
    if abs(result[i])<0.001:
        print(f'a{i} = 0')
    else:
        print(f'a{i} = {result[i]}')
        
mse = MSE(y,list(result),x)
if mse>=0.0001:
    print(f'MSE = {mse}')
else:
    print(f'MSE<0.0001')
