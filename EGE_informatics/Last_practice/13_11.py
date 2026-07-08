from ipaddress import *

for mask in range(0,33):
    net = ip_network(f'108.133.75.91/{mask}', 0)
    print(net,2**(32-mask))