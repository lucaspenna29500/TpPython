#soit la liste d'élèves suivante
eleves = [
    "Thomas", "Bertrand", "Marie", "Etienne", "Jean", "Arnaud", "Bertrand", "Xavier", "Martin", "Jeanne",
    "David", "Rodolphe", "Genevieve", "Pierre", "Karim", "Ines", "Adrien", "Magalie", "Romaric", "Antoine",
    "Karim", "Ines", "Adrien", "Sofia", "Mehdi", "Clara", "Julien", "Amira", "Lucas", "Sarah", "Nicolas",
    "Leïla", "Thomas", "Amina", "Hugo", "Lina", "Yassine", "Emma", "Maxime", "Nawel", "Romain", "Chloé",
    "Antoine", "Samira", "Bastien", "Lila", "Quentin", "Jade", "Yanis", "Camille", "Alexandre", "Hana",
    "Théo", "Myriam", "Enzo", "Salma", "Victor", "Zoé", "Ayoub", "Manon"
]

# compte le nombre d'élèves

nombre_eleves = len(eleves)
print(f"Nombre total d'élèves : {nombre_eleves}")

# en utilisant filter, crée un liste avec les élèves dont le prénom contient un a

prenoms_avec_a = list(filter(lambda prenom: 'a' in prenom.lower(), eleves))
print("Prénoms avec un 'a' :", prenoms_avec_a)

# en utilisant filter, crée un liste avec les élèves dont le prénom contient plus de 7 caractère

prenoms_avec_7 = list(filter(lambda prenom: len(prenom) > 7, eleves))
print("Prénoms avec plus de 7 caractères :", prenoms_avec_7)

# en utilisant filter, crée un liste avec les élèves dont le prénom fini par un d
prenoms_end_d = list(filter(lambda prenom: prenom.lower().endswith('d'), eleves))
print("Prénoms finissant par 'd' :", prenoms_end_d)