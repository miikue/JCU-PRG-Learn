
def print_shape(no):
    for i in range(1,no+1):
        print(" " * (no - i) + ''.join(str(i) for i in range(1, i+1)) + ''.join(str(i) for i in range(i-1, 0, -1)))
    for i in range(no - 2, -1, -1):
        print(" " * (no - i - 1) + "".join(str(i) for i in range(1, i + 2)) + "".join(str(i) for i in range(i, 0, -1)))


print_shape(8)


# Ty postupná čísla mě dost zamotala :D












































