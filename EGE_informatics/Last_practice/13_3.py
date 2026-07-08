from ipaddress import *

net = ip_network('98.71.254.171/255.248.0.0', 0)

for i in range(1, 100000):
    ip = net[i]
    b = f'{ip:b}'
    if b.count('1')%7==0:
        print(ip)