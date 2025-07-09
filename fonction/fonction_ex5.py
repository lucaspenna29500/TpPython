# Dans cette liste d'infos sur des chats via le résultat de l'appel api get sur https://api.thecatapi.com/v1/breeds (tu peux essayer dans Postman si tu veux
# c'est une liste de dictionnaires
# fais une iteration sur cette liste puis sur chaque élément
# compte le nombre de chats représentés
# crée un fonction get_name(**kwarg) qui va te renvoyer et print l'attribut name
# crée une fonction get_life_span(**kwarg) qui va te renvoyer et print l'attribut life_span puis utilise la pour faire la moyenne d'espérance de vie de ces chats
# utilise un set pour lister tous les attributs qui existent
# rajoute les attributs où ils manquent en mettant "indéterminé"


from fonction_ex5_data import liste


nombre_chats = len(liste)
print(f"Nombre de races de chats représentées : {nombre_chats}")

# 2. Fonction pour afficher le nom
def get_name(**kwarg):
    return kwarg.get("name", "indéterminé")

def get_life_span(**kwarg):
    return kwarg.get("life_span", "indéterminé")

total_annees = 0
compte_esp = 0

for cat in liste:
    print("Nom :", get_name(**cat))




