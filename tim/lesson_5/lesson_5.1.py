# Массивы (тип list)

# A = [1,2,3,4,5]
# for x in A:
#     # x= x*x
#     # print(x)
# #    print(x)
#     x+=1
#     print(x)
# #print(A)
# A = [1,2,3,4,5]
# for k in range(5):
#     A[k] = A[k]*A[k]

# A = [0]*1000
# top = 0
# x = int(input())
# while x!=0:
#     A[top] = x
#     top+=1
#     x = int(input())
#
# for i in range(top-1, -1, -1):
#     print(A[i])

#
# N = int(input())
# A = [0]*N
# B = [0]*N
# for k in range(N):
#     A[k] = int(input())
# for k in range(N):
#     B[k] = A[k]

# Полное копирование списка, а не ссылка на уже существующий список
# N = 1000
# A = [0]*N
# C = list(A)
# print(C)

#Линейный поиск в массиве

def array_search(A:list, N:int, x:int):
    ''' Осуществляет поиск числа x в массиве A
        от 0 до N-1 индекса включительно.
        Возвращает индекс элемента x в массиве A.
        Или -1, если такого нет.
        Если в массиве несколько одинаковых элементов,
        равных x, то вернуть индекс певрого по счёту.
    '''
    for k in range(N):
        if  A[k] == x:
            return  k
    return -1


def test_array_search():
    A1 = [1,2,3,4,5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")


    A2 = [-1,-2,-3,-4,-5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print("#test3 - ok")
    else:
        print("#test3 - fail")

test_array_search()


















