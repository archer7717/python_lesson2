text = input()

lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
upppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caiser_chiper(words):
    res, count = "", 0
    words = words.split(" ")
    for i in words:
        count=0
        for c in i:
            if c.isalpha():
                print(c)
                count+=1
        for x in i:
            if x in lowercase_letters:
                alphabet = lowercase_letters
                b = ((alphabet.index(x) + count) % 26)
                res+=alphabet[b]
            elif x in upppercase_letters:
                alphabet = upppercase_letters
                b = ((alphabet.index(x) + count) % 26)
                res+=alphabet[b]
            else:
                res+=x
        res+=" "
    return res


print(caiser_chiper(text))  # ['G', 'd', 'b', ',', 'q', 'm', 'g', 'i', '.', '"', 'C', 'i', 'e', 'v', '"', 'k', 'u', 'b', 't', 'p', 'z', 'a', 'h', 'r', 'l', '!']