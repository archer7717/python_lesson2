

language = input('Введите русский язык или английский')
text = input('Введите текст')
k = int(input('Введите ключ'))
direction = input('зашифровать или дешифровать')

def ceaser_cipher(user, key, lang):
    res, n = [], ''

    if lang in ['русский', 'russian']:
        lowercase_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        upppercase_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    elif lang in ['английск', 'english']:
        lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        upppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        return "Такого языка нет в опции"

    pass

        