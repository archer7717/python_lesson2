from ipaddress import *

for mask in range(33):
    net = ip_network(f'118.193.30.139/{mask}', 0)
    print(net, net.netmask)