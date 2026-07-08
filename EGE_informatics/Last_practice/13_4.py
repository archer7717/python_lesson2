from ipaddress import *

net = ip_network('192.168.12.207/255.192.0.0', 0)
for i in range(-1, -10000, -1):
    ip =  net[i]
    b = f'{ip:b}'
    if b.count('0')==b.count('1'):
        print(ip)