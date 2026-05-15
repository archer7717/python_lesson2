

file = open('languages.txt', 'r', encoding='utf-8')

content = file.readline()

file.close()

print(content)
