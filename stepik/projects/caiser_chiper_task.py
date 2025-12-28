text = input()

lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
upppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def caiser_chiper(words):
    res  = ""
    words = words.split()
    for char in words:
        for a in char:
            if a in lowercase_letters:
                alphabet = lowercase_letters
            elif a in upppercase_letters:
                alphabet = upppercase_letters
            else:
                char += a

            new_index = alphabet.index(a) +




caiser_chiper(text)