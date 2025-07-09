# créez une fonction qui prend en paramètre une suite de longueur indéterminée de int
# et qui renvoi la valeur en bit de la multiplication de ceux ci

def taille_en_bits_multiplication(*nombres):
    if not nombres:
        return 0

    produit = 1
    for n in nombres:
        produit *= n

    return produit.bit_length()

print(taille_en_bits_multiplication(15, 50, 60))
