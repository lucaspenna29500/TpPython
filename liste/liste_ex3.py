# génére la liste des élèves ayant eu moins de 8
from liste_ex3_data import eleves

eleves_moins_de_8 = [eleve for eleve in eleves if eleve[1] < 8]

for nom, note in eleves_moins_de_8:
    print(f"{nom} a eu {note}/20")