def riz():
    total_grains = 0
    grains_case = 1

    for ligne in range(1, 9):
        for colonne in range(1, 9):
            print(f"Ligne {ligne}, Colonne {colonne} : {grains_case} grains")
            total_grains += grains_case
            grains_case *= 2

    print("Nombre total de grains de riz sur l'échiquier :", total_grains)

riz()
