from ipaddress import *

ip1 =ip_address('10.96.180.231')
ip2 =ip_address('10.96.140.118')

for mask in range(33):
    net1 = ip_network(f'{ip1}/{mask}', 0)
    net2 = ip_network(f'{ip2}/{mask}', 0)
    if net1 != net2:
        print(32 - mask)