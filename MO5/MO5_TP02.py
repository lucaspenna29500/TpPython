def compter_lettres(chaine):
    compteur = {}
    for lettre in chaine.replace(" ", ""):
        if lettre.isalpha():
            lettre = lettre.lower()
            compteur[lettre] = compteur.get(lettre, 0) + 1
    return compteur

def est_anagramme(a, b):
    return compter_lettres(a) == compter_lettres(b)

print(est_anagramme("Chien", "Niche"))
print(est_anagramme("mor t esp", "espmort"))
print(est_anagramme("test de test", "port eer"))