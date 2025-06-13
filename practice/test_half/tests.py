

truck_without = int(input())
truck_height = int(input())
piano = int(input())
piano_height = int(input())
fridge = int(input())
fridge_height = int(input())
max_weight_bridge = int(input())
max_height_tunnel = int(input())



def wave_1():
    if piano + fridge + truck_without > max_weight_bridge:
        return 0
    elif truck_height + fridge_height < max_height_tunnel:
        return 1
    else:
        return 0



def wave_2():
    if  truck_height + max(fridge_height, piano_height) > max_height_tunnel:
        return 0
    elif truck_without + piano > max_weight_bridge:
        return 0
    else:
        return 1

if wave_1() ==1  or wave_2() == 1:
    print('YES')
else:
    print('NO')