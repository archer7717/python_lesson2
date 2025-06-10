#1
# x = int(input())
# y = int(input())
# r = int(input())
# if x**2+y**2 <= r*r:
#     print("Yes")
# else:
#     print("No")
#2 потом сделать
# vklad = int(input())
# p = int(input())
# y = int(input())
# year = 0
# while vklad <y:
#     year+=1
#     vklad+=vklad*p/100
#     kopeeiki = vklad * 100
#     kopeeiki = int(kopeeiki)
#     kopeeiki = kopeeiki/100
#     vklad = kopeeiki
#     #vklad = int(vklad)
#
# print(year)
#3
# N = int(input())
# A = [0]*N
# n = 0
# curren_max = 0
# max = 0
# for k in A:
#     b  = int(input())
#     A[n] = b
#     if A[n] ==1:
#         curren_max +=1
#         if curren_max > max:
#             max = curren_max
#     else:
#         curren_max = 0
#     n+=1
# print(max)


#
# n = int(input())
# counter_3_summ = 0
# counter_3 = 0
# remainder = 0
# average = 0
# av = 0
# max = 0
# min = 99999999
# while n!="#":
#     counter_3_summ +=n
#     counter_3+=1
#     if counter_3 ==3:
#         remainder += counter_3_summ%n
#         # print(remainder, counter_3_summ)
#         counter_3_summ=0
#         counter_3=0
#
#     av+=1
#     average +=n
#     if n > max:
#         max = n
#     if n <min:
#         min = n
#     a = input()
#     if a == '#':
#         break
#     else:
#         n = int(a)**2**0.5
#     print(a)
#
# average = round(average/av,3)
#
#
# print(average,max,min,remainder)

#4
# A =['#'] * 100000
# b = 0
# n = int(input())
# number_1 = 0
# number_2 = 1
# number_3 = 2
# counter_3 = 0
# counter_3_summ = 0
# remainder = 0
# average = 0
# av = 0
# max = 0
# min = 99999999
# while n!='#':
#     A[b] = n
#     b+=1
#     a = input()
#     if a=='#':
#         break
#     else:
#         n = int(a)
# b = 0
# while A[b]!='#':
#     if A[b] > max:
#         max = A[b]
#     if A[b] < min:
#         min = A[b]
#     average +=A[b]
#     av+=1
#     b+=1
#
# average= round(average/av,3)
# b = 0
# while A[number_1]!='#':
#     counter_3_summ = A[number_1] + A[number_2] +A[number_3]
#     remainder+=counter_3_summ%A[number_3]
#     counter_3_summ=0
#     number_1+=3
#     number_2+=3
#     number_3+=3
#
# print(average,max,min,remainder)

#5_not_done
# A = []
# n = int(input())
# b = input()
# while b!='#':
#     x, y =map(int, b.split())
#     A.append(x)
#     A.append(y)
#     b = input()
# print(A)
#
#
#6
# def create_input_data() -> list[int]:
#     """Creates input data."""
#     arr = []
#     print("Input the data in the following format:\n"
#           "- The first line is a number of students;\n"
#           "- The last line is a line with a symbol #;\n"
#           "- The lines between the first and last ones in the format:\n"
#           "    student_id value,\n"
#           "    0 <= student_id <= N (a number of students),\n"
#           "    1 <= value <= 10.")
#     while True:
#         inp = input()
#         if inp == '#':
#             break
#         elif len(inp.split()) == 1:
#             arr.append(int(inp))
#         else:
#             arr.append([int(inp.split()[0]), int(inp.split()[1])])
#     return arr
#
#
# def find_sorted_ids(arr: list) -> list:
#     """Finds sum of mark for every student and sort their ids."""
#     arr_short = arr[1:]
#     arr_st = [0] * arr[0]
#     for el in arr_short:
#         arr_st[el[0]] += el[1]
#     indexed_arr = list(enumerate(arr_st))
#     sorted_indexed_arr = sorted(indexed_arr, key=lambda x: x[1], reverse=True)
#     sorted_indexes = [tpl[0] for tpl in sorted_indexed_arr]
#     return sorted_indexes
#
#
# def sort_student_marks(arr: list, sorted_indexes: list) -> list:
#     """Sorts the students marks."""
#     sorted_marks = sorted(
#         arr[1:],
#         key=lambda x: (sorted_indexes.index(x[0]), -x[1])
#     )
#     return sorted_marks
#
#
# def create_string_output(sorted_marks: list) -> str:
#     """Returns sorted marks in one line."""
#     string_output = " ".join([str(el[1]) for el in sorted_marks])
#     return string_output
#
#
# def main() -> None:
#     input_data = create_input_data()
#     sorted_indexes = find_sorted_ids(input_data)
#     sorted_marks = sort_student_marks(input_data, sorted_indexes)
#     string_output = create_string_output(sorted_marks)
#     print(string_output)
#     # return string_output
#
#
# if __name__ == "__main__":
#     main()


def input_chocolate_length() -> int:
    """Creates input."""
    inp = int(input("Input the chocolate length (N <= 10000): "))
    return inp


def count_number_of_ways(inp: int) -> int | str:
    """Counts the number of ways how to divide the chocolate bar."""
    if inp == 0:  # 3 x 0
        mes = (
            "It is impossible to divide the chocolate bar because there is " 
            "no chocolate."
        )
    elif inp % 2 !=0: #3 x 1, 3 x 3, 3 x 5, ...
        mes = (
            f"It is impossible to divide the chocolate bar because the amount "
            f"of chocolate pieces is odd: 3 x {inp}"
        )
    elif inp == 2: #3 x 2
        return  3

    elif inp == 4: # 3 x 4
        return  11
    elif inp > 4:
        arr = [0] * (int(inp / 2))
        arr[0] = 3
        arr[1] = 11
        for idx in range(2, len(arr)):
            arr[idx] = 4 * arr[idx - 1] - arr[idx - 2]
        return arr[-1]



def main():
    inp = input_chocolate_length()
    ways = count_number_of_ways(inp)
    print(ways)

main()