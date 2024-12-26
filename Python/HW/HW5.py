
fileIn = open("accounts.txt", "r")
fileOut = open("hw5_afkjb.txt", "w")

def moduloCheck(line):
    result = 0
    for i in range(len(line), 0, -1):
        result += int(line[len(line)-i])*((2**i)%11)
    return result%11

def accountsCheck(fileIn):
    for line in fileIn:
        line = line.strip()
        separator = line.split("/")
        if moduloCheck(separator[0]) == 0:
            print(separator[0] + " / " + separator[1])
            fileOut.write(separator[0] + "/" + separator[1] + "\n")

accountsCheck(fileIn)


fileIn.close()
fileOut.close()