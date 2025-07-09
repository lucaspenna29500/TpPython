def max_value(a, b):
    if a > b:
        return a
    else:
        return b

def compare(a, b):
    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return -1

def test_functions():
    a = float(input("Entrez la première valeur : "))
    b = float(input("Entrez la deuxième valeur : "))

    print("La valeur maximale est :", max_value(a, b))

    result = compare(a, b)
    if result == 0:
        print("Les deux valeurs sont égales.")
    elif result == 1:
        print("La première valeur est plus grande.")
    else:
        print("La deuxième valeur est plus grande.")

test_functions()
