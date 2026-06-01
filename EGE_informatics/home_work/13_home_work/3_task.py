from ipaddress import *

ip = ip_address('154.201.208.17')

for mask in range(33):
    net = ip_network(f'{ip}/{mask}', 0)
    #if net[0] < ip < net[1]:
    print(net, net.netmask)