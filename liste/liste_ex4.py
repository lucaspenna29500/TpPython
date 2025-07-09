# enlever le nom de famille et mettre que le prénom
from liste_ex4_data import eleves

eleves_prenoms = [(nom.split()[0], note) for nom, note in eleves]

for prenom, note in eleves_prenoms:
    print(f"{prenom} : {note}")