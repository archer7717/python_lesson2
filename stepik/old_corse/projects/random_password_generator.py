
import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'


def get_data():
    chars = ''
    count = input( 'How many passwords do you want to generate?:  ')
    lenght = int(input(('Len of passwords: ')))
    numbers = input('Add numbers? 0123456789: ')
    if numbers == 'да':
        chars+=digits
    letters_up = input('Add upper case? ABCDEFGHIJKLMNOPQRSTUVWXYZ: ')
    if letters_up == 'да':
        chars+=uppercase_letters
    letters_down = input('Add lower case? abcdefghijklmnopqrstuvwxyz: ')
    if letters_down == 'да':
        chars+=lowercase_letters

    symbols = input('Add symbols? !#$%&*+-=?@^_: ')
    if symbols == 'да':
        chars+=punctuation
    ambiguous_characters = input('Add ambiguous characters? il1Lo0O: ')
    if ambiguous_characters != 'да':
        for i in "il1Lo0O":
            chars = chars.replace(i,"")
    print(chars)
    return chars, lenght, int(count)


def generate_password(chars, lenght, count):
    for i in range(count):
        password = []
        for _ in range(lenght):
            password.append(random.choice(chars))
        print(''.join(password))

a,b,c = get_data()

generate_password(a,b,c)
