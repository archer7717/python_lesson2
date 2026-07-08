from ipaddress import *

net = IPv4Network('10.22.44.0/255.255.252.0', 0)
c = 0
for host in net.hosts():
    num = int(host) & int(net.hostmask)
    if f'{num:b}'.count('1') % 2 == 0:
        c += 1
print(c) 