from ipaddress import  *

ip = ip_address('238.237.149.255')



for mask in range(31):
    net = ip_network(f'238.237.149.255/{mask}', 0)
   # print(mask, net, net.broadcast_address)
    if  net[0] < ip < net[-1]:
        print(mask, net)