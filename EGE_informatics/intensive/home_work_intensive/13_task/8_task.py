from ipaddress import *


net = ip_network('136.36.240.16/255.255.255.248', 0)
k = 0
for ip in net:
    b = f'{int(ip):032b}'
    if '101' not in b:
        k+=1
        print(b)
print(k)