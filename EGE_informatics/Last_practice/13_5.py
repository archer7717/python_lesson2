from ipaddress import *


net = ip_network('112.160.0.0/255.240.0.0', 0)
k = 0
for i in net:
    b = bin(int(i))[2:]
    if b.count('1')%5==0:
        k+=1
print(k)