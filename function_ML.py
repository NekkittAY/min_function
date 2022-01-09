class min_func:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def learn(self):
        for i in range(1000):
            m_func.update_c()
        for j in range(1000):
            m_func.update_a()
        for k in range(1000):
            m_func.update_b()
        for t in range(1000):
            m_func.update_d()
        
    def update_a(self):
        self.a0 = (self.a-0.1)
        self.a1 = (self.a+0.1)
        self.ra0 = MSE(self.a0,self.b,self.c,self.d)
        self.ra1 = MSE(self.a1,self.b,self.c,self.d)
        self.rn = MSE(self.a,self.b,self.c,self.d)
        self.ma = min(self.ra0,self.ra1,self.rn)
        if self.ma==self.ra1:
            self.a=self.a1
        elif self.ma==self.ra0:
            self.a=self.a0

    def update_b(self):
        self.b0 = (self.b-0.1)
        self.b1 = (self.b+0.1)
        self.rb0 = MSE(self.a,self.b0,self.c,self.d)
        self.rb1 = MSE(self.a,self.b1,self.c,self.d)
        self.rn = MSE(self.a,self.b,self.c,self.d)
        self.mb = min(self.rb0,self.rb1,self.rn)
        if self.mb==self.rb1:
            self.b=self.b1
        elif self.mb==self.rb0:
            self.b=self.b0

    def update_c(self):
        self.c00 = (self.c-1)
        self.c01 = (self.c+1)
        self.c10 = (self.c-2)
        self.c11 = (self.c+2)
        self.rc00 = MSE(self.a,self.b,self.c00,self.d)
        self.rc01 = MSE(self.a,self.b,self.c01,self.d)
        self.rc10 = MSE(self.a,self.b,self.c10,self.d)
        self.rc11 = MSE(self.a,self.b,self.c11,self.d)
        self.rn = MSE(self.a,self.b,self.c,self.d)
        self.mc = min(self.rc00,self.rc01,self.rc10,self.rc11,self.rn)
        if self.mc==self.rc00:
            self.c=self.c00
        elif self.mc==self.rc01:
            self.c=self.c01
        elif self.mc==self.rc10:
            self.c=self.c10
        elif self.mc==self.rc11:
            self.c=self.c11


    def update_d(self):
        self.d0 = (self.d-0.1)
        self.d1 = (self.d+0.1)
        self.rd0 = MSE(self.a,self.b,self.c,self.d0)
        self.rd1 = MSE(self.a,self.b,self.c,self.d1)
        self.rn = MSE(self.a,self.b,self.c,self.d)
        self.md = min(self.rd0,self.rd1,self.rn)
        if self.md==self.rd1:
            self.d=self.d1
        elif self.md==self.rd0:
            self.d=self.d0
            
func = input("f(x)= ")
f1 = calc(func)
f2 = []
for j in range(-100,101):
    f2.append(j)
m_func = min_func(1,0,1,0)
print_func = str(m_func.a)+"*(x+"+str(m_func.b)+")^"+str(m_func.c)+"+"+str(m_func.d)
print("machine function:",print_func)
print("MSE:",MSE(m_func.a,m_func.b,m_func.c,m_func.d))
