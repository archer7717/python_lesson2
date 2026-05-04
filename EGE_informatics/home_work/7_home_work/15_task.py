def f(x):
    P = 135 <=x <=218
    Q = 174 <=x<= 308
    R = 246 <=x<=382
    A = a1<=x <=a2
    return (not(Q <= (P or R)) <= ((not A) <= (not Q))
