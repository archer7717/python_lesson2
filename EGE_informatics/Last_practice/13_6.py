from ipaddress import *

net = ip_network('112.208.0.0/255.255.128.0', 0)
k = 0
for ip in net:
    b = f'{int(ip):032b}'
    if b.count('0')%11==0:
        k+=1
print(k)