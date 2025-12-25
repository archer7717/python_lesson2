

language = input('Введите русский язык или английский')
text = input('Введите текст')
#k = int(input('Введите ключ'))
direction = input('зашифровать или дешифровать')

def ceaser_cipher(user,  lang, direction):
    results = []

    if lang in ['русский', 'russian']:
        alphas = 32
        lowercase_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        upppercase_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    elif lang in ['английский', 'english']:
        alphas = 26
        lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        upppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        return "Такого языка нет в опции"

    for key in range(1, alphas+1):
        result= ''


        for char in text:
            if char in lowercase_letters:
                alphabet = lowercase_letters

            elif char in upppercase_letters:
                alphabet = upppercase_letters
            else:
                result += char
                continue

            if  direction == 'зашифровать':
                new_index = (alphabet.index(char) + key) % alphas
            else:  # дешифровать
                new_index = (alphabet.index(char) - key) % alphas
            result += alphabet[new_index]
        results.append(f"Ключ {key}: {result}")
    return results
#Усффлв
all_results = ceaser_cipher(text, language, direction)

#print(ceaser_cipher(text,language, direction))

for result in all_results:
    print(result)