import numpy as np
from numpy import linalg
from functools import reduce

def MNK(x0,y0):
    a = []
    b = []
    c = []
    d = []
    e = []
    y = []
    for n in range(5):
        a.append(reduce(lambda x1,x2: x1+x2, [i**(8-n) for i in x0]))
        b.append(reduce(lambda x1,x2: x1+x2, [i**(7-n) for i in x0]))
        c.append(reduce(lambda x1,x2: x1+x2, [i**(6-n) for i in x0]))
        d.append(reduce(lambda x1,x2: x1+x2, [i**(5-n) for i in x0]))
        e.append(reduce(lambda x1,x2: x1+x2, [i**(4-n) for i in x0]))
        y.append(reduce(lambda x1,x2: x1+x2, [x0[i]**(4-n)*y0[i] for i in range(len(x))]))
    e[-1] = len(x)
    arr = []
    for i in range(5):
        arr.append([a[i], b[i], c[i], d[i], e[i]])
    m = np.array(arr)
    det_m = np.linalg.det(m)
    arr = []
    for i in range(5):
        arr.append([y[i], b[i], c[i], d[i], e[i]])
    m_a = np.array(arr)
    det_m_a = np.linalg.det(m_a)
    arr = []
    for i in range(5):
        arr.append([a[i], y[i], c[i], d[i], e[i]])
    m_b = np.array(arr)
    det_m_b = np.linalg.det(m_b)
    arr = []
    for i in range(5):
        arr.append([a[i], b[i], y[i], d[i], e[i]])
    m_c = np.array(arr)
    det_m_c = np.linalg.det(m_c)
    arr = []
    for i in range(5):
        arr.append([a[i], b[i], c[i], y[i], e[i]])
    m_d = np.array(arr)
    det_m_d = np.linalg.det(m_d)
    arr = []
    for i in range(5):
        arr.append([a[i], b[i], c[i], d[i], y[i]])
    m_e = np.array(arr)
    det_m_e = np.linalg.det(m_e)
    return det_m_a/det_m,det_m_b/det_m,det_m_c/det_m,det_m_d/det_m,det_m_e/det_m

x = list(map(float, input().split()))
y = list(map(float, input().split()))

a,b,c,d,e = MNK(x,y)
print(f'f(x) = {a}x^4+{b}x^3+{c}x^2+{d}x+{e}')
