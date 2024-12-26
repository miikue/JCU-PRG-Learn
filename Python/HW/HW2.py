

x = input("Type x: ")
y = input("Type y: ")
print("Operations: conjunction, disjunction, implication, exclusive, equivalence")
operation = input("Type operation: ")

if operation == "conjunction":
    print(eval("x and y"))
elif operation == "disjunction":
    print(eval("x or y"))
elif operation == "implication":
    print(eval("not x or y"))
elif operation == "exclusive":
    print(eval("(x or y) and not(x and y)"))
elif operation == "equivalence":
    print(eval("not ((x or y) and not (x and y))"))

#Oprava
# Zkusil jsem se podívat na ty eval funkce a podařilo se mi to zjednodušit.
# Původně mě vůbec nenapadlo to uvádět v takovýchv "expresions" (i přes to, že jsem to používal v minulosti :D )



# Původní kód
def original():
    x = input("Type x: ")
    y = input("Type y: ")
    operation = input("Type operation: ")

    if operation == "conjunction":
        if x == 1 and y == 1:
            print("1")
        else:
            print("0")
    elif operation == "disjunction":
        if x == 0 and y == 0:
            print("0")
        else:
            print("1")
    elif operation == "implication":
        if x == 1 and y == 0:
            print("0")
        else:
            print("1")
    elif operation == "exclusive":
        if x == y:
            print("0")
        else:
            print("1")
    elif operation == "equivalence":
        if x == y:
            print("1")
        else:
            print("0")

    # Nenapadlo mě nic jiného než toto. 

