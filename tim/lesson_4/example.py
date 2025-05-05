def is_simple_number(x):
    """ Определяет, является ли число простым.
        x - целове положительное число
        Если простое, то возвращает True,
        а иначе - False
    """
    divisor = 2
    while divisor < x:
        if x%divisor == 0:
            return False
        divisor+=1
    return True
def factorize_number(x):
    """ Расскладывает число на множители.
        Печатает на экран.
        x- целове положительное число
        """
    divisor = 2
    while x > 1:
        if x%divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor+=1
