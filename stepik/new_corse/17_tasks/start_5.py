

file = open('languages.txt', 'r', encoding='utf-8')


languages = [line.strip() for line in file.readlines()]
print(languages)

file.close()
