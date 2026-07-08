from ipaddress import *

net = ip_network('98.71.254.171/255.248.0.0', 0)

for ip in net:
    b = f'{int(ip):032b}'
    if b.count('1')%7==0:
        print(ip)
        break