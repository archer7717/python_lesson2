number = int(input("Enter a number: "))

def translation(n):
    res = []
    res.append(bin(n))
    res.append(oct(n))
    res.append(hex(n))
    return res

end = translation(number)
for i in end:
    print(i[2:].upper())