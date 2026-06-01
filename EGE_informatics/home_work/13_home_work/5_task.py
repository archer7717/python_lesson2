from ipaddress import *

for mask in range(33):
    net = ip_network(f'173.103.25.118/{mask}', 0)
    print(net, net.netmask)