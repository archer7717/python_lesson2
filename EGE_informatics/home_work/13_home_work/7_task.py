from ipaddress import *

for mask in range(33):
    net = ip_network(f'191.173.145.240/{mask}', 0)
    print(net, net.num_addresses)