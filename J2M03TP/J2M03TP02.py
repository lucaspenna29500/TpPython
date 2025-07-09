def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def afficher_nombres_premiers(limite):
    compteur = 0
    for nombre in range(2, limite + 1):
        if est_premier(nombre):
            print(nombre)
            compteur += 1
    print(f"\nNombre total de nombres premiers trouvés : {compteur}")

def lancer_recherche():
    try:
        limite = int(input("Entrez la limite supérieure (par exemple 1000) : "))
    except:
        limite = 1000
        print("Valeur invalide, utilisation de la valeur par défaut : 1000")

    afficher_nombres_premiers(limite)

lancer_recherche()
