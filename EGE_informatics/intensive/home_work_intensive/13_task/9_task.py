from ipaddress import *


for mask in range(0, 33):
    net = ip_network(f'154.201.208.17/{mask}', 0)
    print(net, net.netmask)
