from math import *
import random

def calc(func):
    result = []
    for i in range(-100,101):
        mass=""
        for s in func:
            if s=="x":
                mass+=str(i)
            else:
                mass+=s
        try:
            res=eval(mass)
            result.append(res)
        except:
            res=1000000
            result.append(res)
    return result

def MSE(w):
    res=0
    for i in range(0,len(f1)-1):
        d=(f1[i]-f2[i]*w)**2
        res+=d
    res/=len(f1)
    return res

class min_func:
    def __init__(self,w):
        self.w = w
        
    def function(self):
        self.x0 = (self.w-0.001)
        self.x1 = (self.w+0.001)
        self.c0 = MSE(self.x0)
        self.c1 = MSE(self.x1)
        self.m = min(self.c0,self.c1)
        return self.m
        
    def update(self):
        if MSE(self.w)<self.m:
            return self.w
        else:
            if self.m==self.c1:
                self.w=self.x1
                self.x0 = 0
            else:
                self.w=self.x0
                self.x1 = 0

func = input("f(x)= ")
f1 = calc(func)
f2 = []
for j in range(-100,101):
    f2.append(j)
rand_x = 0
m_func = min_func(rand_x)

for i in range(100000):
    m_func.function()
    m_func.update()
    
res = m_func.w
print("w =", res)
