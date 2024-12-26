import random
import string

# Verifying password
def passwordCheck(password):
    # Length check
    if len(password) < 10:
        return False
    
    # Ending with punctuation
    if password[len(password)-1] not in string.punctuation:
        return False
    
    # Upper check
    index = []
    for i in password:
        if i in string.ascii_uppercase:
            index.append(password.index(i))
    if index[0] + index[1] != 7:
        return False
    if index[1] - index[0] >= 4:
        return False
    
    # Lower check
    if password[index[1]-1] not in string.ascii_lowercase:
        return False
    if password[index[0]-1] not in string.ascii_lowercase:
        return False

def shakePassword(password):
    password = list(password)
    random.shuffle(password)
    return ''.join(password)


def randomPassword(length = 10):
    password = ''
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.digits)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    password += random.choice(string.punctuation)
    password += random.choice(string.punctuation)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_lowercase)

    # Adjustable length
    if length > 10:
        for i in range(length-10):
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    # Testing password and shaking it
    while passwordCheck(password) == False:
        print("-Test-", password)
        password = shakePassword(password)
    return password

print("Valid password:", randomPassword(20))

# Mohl jsem heslo generovat s pevnou pozicí velkých a malých písmen ale toto řešení může generovat širší pásmo hesel.