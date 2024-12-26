
def create_pattern(slovo):
    dict = {}
    list = []
    number = 0
    for i in slovo:
        if i in dict:
            list.append(dict[i])
        else:
            dict[i] = number
            list.append(number)
            number += 1
    return list

def load_dictionary():
    dictionary = []
    with open("dictionary.txt", "r") as f:
        for line in f:
            dictionary.append(line.strip())
    return dictionary


def hw7():
    words=['marta', 'python', 'klavesnice', 'ptakopysk', 'dobromysl', 'panama', 'postoloprty', 'miikue']
    paterns = {}

    for word in words:
        word_pattern = create_pattern(word)
        dictionary = load_dictionary()
        clean_dictionary = []
        for i in dictionary:
            if word_pattern == create_pattern(i):
                clean_dictionary.append(i)
        
        paterns[word] = (word_pattern, clean_dictionary)

    return paterns



paterns = hw7()

for i in paterns:
    print("-"*20)
    print(i, len(paterns[i][1]), paterns[i])

