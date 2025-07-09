from random import randint

animaux = {
    1: 3,  # 3 mange 1
    2: 1,  # 1 mange 2
    3: 2   # 2 mange 3
}

def generateTable(n):
    return [[randint(1, 3) for _ in range(n)] for _ in range(n)]

def afficher(tableau):
    for ligne in tableau:
        print(" ".join(str(x) for x in ligne))
    print()

def ecosystem(tableau):
    x, y = 1, 1
    centre = tableau[x][y]
    predateur = animaux[centre]

    voisins = [
        tableau[i][j]
        for i in range(x - 1, x + 2)
        for j in range(y - 1, y + 2)
        if not (i == x and j == y)
    ]

    nb_predateurs = voisins.count(predateur)
    nb_proies = voisins.count(animaux[predateur])
    nb_neutres = 8 - nb_predateurs - nb_proies

    if nb_predateurs > nb_proies:
        tableau[x][y] = predateur
    elif nb_predateurs == nb_proies or (nb_predateurs > 0 and nb_neutres > 0):
        if randint(0, 1) == 1:
            tableau[x][y] = predateur

print(generateTable(5))
