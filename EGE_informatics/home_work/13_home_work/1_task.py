# from ipaddress import *
#
# net = ip_network('10.8.248.131/255.255.224.0', 0)
# print(net)

print('.'.join(f'{x:>08b}' for x in [10,8,248,131]))
print()
print('.'.join(f'{x:>08b}' for x in [255,255,224,0]))