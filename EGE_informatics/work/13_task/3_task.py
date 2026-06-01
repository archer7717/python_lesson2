from ipaddress import *

for mask in range(33):
    net = ip_network(f'220.128.112.142/{mask}', 0)
    print(net, net.netmask)
