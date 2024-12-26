dict = {1:['e','a','o','n','r','t','l','s','u'],
        2:['d','g'], 
        3: ['b','c','m','p'], 
        4: ['f','h','v','w','y'], 
        5: ['k'], 
        8: ['j','x'], 
        10: ['q','z']}



def calculate_score(word):
    score = 0
    for i in word:
        for key, value in dict.items():
            if i in value:
                score += key
    return score


test = ['hi', 'quiz', 'bomb', 'president']
test2 = ['zero', 'one', 'two', 'three', 'four', 'five']
rawinput = open("dictionary.txt", "r").read()
input = rawinput.split("\n")
bum = []
for word in input:
    bum.append(word.lower())

input = bum


def worthOfList(list):
    # Create dictionary with words and their scores
    words_dict = {}
    for i in list:
        words_dict[i] = calculate_score(i)

    # Find max value
    max = 0
    for key, value in words_dict.items():
        if value > max:
            max = value

    # Find all words with max value
    result = []
    for key, value in words_dict.items():
        if value == max:
            result.append(key)
    return result


def betterPrinter(list):
    if len(list) < 10:
        for i in list:
            print(i , " : " , calculate_score(i))
    else:
        print("Too many results")
        print(len(list), "results : " , calculate_score(list[0])) 




betterPrinter(worthOfList(input))