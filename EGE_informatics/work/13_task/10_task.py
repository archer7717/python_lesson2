from ipaddress import *

for mask in range(33):
    net = ip_network(f'175.122.80.13/{mask}', 0)
    if net.num_addresses >= 60:
        print(net)