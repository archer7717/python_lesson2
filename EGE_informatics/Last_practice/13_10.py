from ipaddress import *


for mask in range(0, 33):
    net = ip_network(f'241.185.253.57/{mask}', 0)
    print(net, 32-mask)