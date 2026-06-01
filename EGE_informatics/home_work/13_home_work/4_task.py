from ipaddress import *

for mask in range(33):
    net = ip_network(f'122.21.49.91/{mask}', 0)
    print(net, net.netmask)
