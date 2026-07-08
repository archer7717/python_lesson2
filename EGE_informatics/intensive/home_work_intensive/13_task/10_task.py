from ipaddress import *

for mask in range(0, 33):
    net = ip_network(f'142.198.113.106/{mask}', 0)
    print(net, net.netmask)

