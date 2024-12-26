
def reverse_ascending(lst):
    if len(lst) == 0:
        return []

    result = []
    helpList = []
    i = 0
    while i < len(lst)-1:
        if lst[i] <= lst[i+1]:
            helpList.append(lst[i])
        else:
            helpList.append(lst[i])
            result += helpList[::-1]
            helpList = []
        i += 1
    helpList.append(lst[-1])
    result += helpList[::-1]
    return result



print(reverse_ascending([1, 2, 3, 4, 5]))

print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]))


