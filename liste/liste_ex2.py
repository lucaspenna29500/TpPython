# Génère une liste des nombres pairs entre 0 et 20 inclus

paires = [x for x in range(0, 21) if x % 2 == 0]
print(paires)