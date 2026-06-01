# print('.'.join(f'{x:>08b}' for x in [135,12,171,214]))
# print('.'.join(f'{x:>08b}' for x in [255,255,248,0]))
from ipaddress import *

net = ip_network('135.12.171.214/255.255.248.0', 0)
print(net)