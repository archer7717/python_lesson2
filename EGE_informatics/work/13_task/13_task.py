#
# print('.'.join(f'{x:>08b}' for x in [255, 255, 255, 240]))
# print(' ')
# print('.'.join(f'{x:>08b}' for x in [192, 168, 156, 235]))


from ipaddress import *
k = 0
net = ip_network('192.168.0.0/255.255.128.0')
for ip in net:
    if int(ip) %4 == 0:
        k+=1
print(k)