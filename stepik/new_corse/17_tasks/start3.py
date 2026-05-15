

file = open('languages.txt', 'r', encoding='utf-8')

line = file.readline()


while line != '':
    print(line.strip())
    line = file.readline()

file.close()

