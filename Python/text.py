import string

text = open("raven.txt", "r").read()
sub_text = ""
sub_Strings = []

# marta rešení
#txt2 = "".join([symbols.lower() for symbols in text if symbols in string.ascii_lowercase])


for symbols in text:
    if symbols in string.punctuation or symbols.isspace() or symbols == "-" or symbols == "—":
        continue
    symbols = symbols.lower()


    if symbols in sub_text:
        sub_Strings.append(sub_text)
        sub_text = ""
    else:
        sub_text += symbols



size = len(max(sub_Strings, key=len))

print("The longest substring are: ", [i for i in sub_Strings if len(i) == size])