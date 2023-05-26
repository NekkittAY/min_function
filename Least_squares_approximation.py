import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt
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
    res = res/len(y)
    return res

def euclidean_metric(y,a_pred,x):
    res = 0
    for i in range(len(y)):
        res+=(y[i]-y_pred(a_pred,x[i]))**2
    res = res**0.5
    return res

def MAE(y,a_pred,x):
    res = 0
    for i in range(len(y)):
        res+=(y[i]-y_pred(a_pred,x[i]))
    res = res/len(y)
    return res

def plot(x,y,a):
    plt.scatter(x,y,color='r')
    X = np.arange(min(x)-1,max(x)+1,0.01)
    f = f'{a[0]}'
    for i in range(1,len(a)):
        f+=f'+{a[i]}*X**{i}'
    f = eval(f)
    plt.plot(X,f,mec='b')
    plt.xlim(min(x)-1,max(x)+1)
    plt.ylim(min(y)-1,max(y)+1)
    plt.grid(True)
    plt.show()

x = list(map(float, input().split()))
y = list(map(float, input().split()))
m = int(input())

result = MNK(x,y,m)

print(*result, end='\n\n')

for i in range(len(result)):
    if abs(result[i])<0.001:
        print(f'a{i} = 0')
    else:
        print(f'a{i} = {result[i]}')

print("")
      
mse = MSE(y,list(result),x)
if mse>=0.0001:
    print(f'MSE = {mse}')
else:
    print(f'MSE<0.0001')

mae = MAE(y,list(result),x)
if mae>=0.0001:
    print(f'MAE = {mae}')
else:
    print(f'MAE<0.0001')
    
metric = euclidean_metric(y,list(result),x)
if mae>=0.0001:
    print(f'Euclidean Metric = {metric}')
else:
    print(f'Euclidean Metric<0.0001')

plot(x,y,list(result))
