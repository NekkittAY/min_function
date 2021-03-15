from math import *
import random

def calc(func,x):
    mass=""
    for s in func:
        if s=="x":
            mass+=str(x)
        else:
            mass+=s
    res=eval(mass)
    return res

class min_func:
    def __init__(self,func,x):
        self.x = x
        self.func = func
        
    def function(self):
        self.x0 = (self.x-1)
        self.x1 = (self.x+1)
        self.c0 = calc(func,self.x0)
        self.c1 = calc(func,self.x1)
        self.m = min(self.c0,self.c1)
        return self.m
        
    def update(self):
        if calc(func,self.x)<self.m:
            return self.x
        else:
            if self.m==self.c0:
                self.x=self.x0
                self.x0 = 0
            else:
                self.x=self.x1
                self.x1 = 0

func = input()
rand_x = random.randint(-100,100)
m_func = min_func(func,rand_x)

for i in range(10000):
    m_func.function()
    m_func.update()
    
res = m_func.x
result = calc(func,res)
print("f(x) =", result)
print("x =", res)
