import re

# Metoda pro testování patternu
def testPattern(pattern, test_string):
    if re.match(pattern, test_string):
        print("Přijat")
    else:
        print("Nepřijat")

# Základní test
pattern = r'a*bc+[0-5a-z]'
test_string = "aaaaaabccccf"

testPattern(pattern, test_string) # Přijat

# Telefonní číslo
pattern = r'^\d{3} \d{3} \d{3}$'
test_string = "123 435 789"

testPattern(pattern, test_string) # Přijat

# Email
pattern = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$'
test_string = "nejakyEmail@email.cz"

testPattern(pattern, test_string) # Přijat

pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
test_string = "31/12/2020"

testPattern(pattern, test_string) # Přijat

# Mac adresa
pattern = r'^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$'
test_string = "01:23:45:67:89:AB"

testPattern(pattern, test_string) # Přijat