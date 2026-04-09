from itertools import permutations
count = 0

for x in permutations('АБИКОЛУН'):
    s = ''.join(x)
    s = s.replace('И','А').replace("О", "А").replace("У", "А")
    s = s.replace("К", "Б").replace("Л", 'Б').replace("Н", 'Б')

    if 'АА' not in s and 'ББ' not in s:
        count+=1
        
print(count)
