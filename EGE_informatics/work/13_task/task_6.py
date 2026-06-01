from ipaddress import *
#
# print('.'.join(f'{x:>08b}' for x in [76, 155, 48, 2]))
# print()
# print('.'.join(f'{x:>08b}' for x in [76, 155, 48, 0]))

for mask in range(33):
    net = ip_network(f'76.155.48.2/{mask}', 0)
    print(net)