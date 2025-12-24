

language = input('Введите русский язык или английский')
text = input('Введите текст')
k = int(input('Введите ключ'))
direction = input('зашифровать или дешифровать')

def ceaser_cipher(user, key, lang, direction):
    res, n = [], ''

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
    b = len(text)
    for i in range(b):
        if text[i].isalpha():
            if direction == 'зашифровать':
                if text[i] in lowercase_letters:
                    res = ((lowercase_letters.index(text[i]) + k ) % alphas)
                    n += lowercase_letters[res]
                else:
                    res = ((upppercase_letters.index(text[i]) + k ) % alphas)
                    n += upppercase_letters[res]
            else:
                if text[i] in lowercase_letters:
                    res = ((lowercase_letters.index(text[i]) - k ) % alphas)
                    n += lowercase_letters[res]
                else:
                    res = ((upppercase_letters.index(text[i])  - k ) % alphas)
                    n += upppercase_letters[res]
        else:
            n+=text[i]

    return n

#Усффлв


print(ceaser_cipher(text, k, language, direction))