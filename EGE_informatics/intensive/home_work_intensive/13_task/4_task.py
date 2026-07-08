from ipaddress import *


net = ip_network('192.168.12.207/255.192.0.0', 0)

for ip in net:
    b = f'{int(ip):032b}'
    if b.count('0')==b.count('1'):
        print(ip)