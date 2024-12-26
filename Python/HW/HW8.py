input = open("find_numbers.txt", "r")
output = open("found_numbers.txt", "w")

def test_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def test_fibonacci(number):
    if number == 0:
        return True
    if number == 1:
        return True
    if not (number-1 + number-2) == number:
        return True

# Ano je to zbytečné, šlo by to číst v jednom loopu :P 
input_list = []
for i in input:
    input_list.append(i.strip())

output_list = []
for i in input_list:
    if not test_prime(int(i)):
        continue
    if not test_fibonacci(int(i)):
        continue
    output_list.append(i)
    output.write(i + "\n")


print(output_list)
