from ipaddress import *


net = ip_network('211.48.136.64/255.255.255.224')
k = 0
for ip in net:
    b = (f'{ip:b}')
    if b[-2:] == '11':
        print(b)
        k+=1
print(k)