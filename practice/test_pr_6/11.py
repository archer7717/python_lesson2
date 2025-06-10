def input_chocolate_length() -> int:
    """Creates input."""
    inp = int(input("Input the chocolate length (N <= 10000): "))
    return inp


def count_number_of_ways(inp:int):
    """Counts the number of ways how to divide the chocolate bar."""
    if inp == 0:
        pass

    elif inp % 2 !=0:
        pass


    elif inp == 2:
        return  3

    elif inp == 4:
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