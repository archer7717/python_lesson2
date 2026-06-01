from ipaddress import *

for mask in range(33):
    net = ip_network(f'158.116.11.146/{mask}', 0)
    print(net, net.netmask)