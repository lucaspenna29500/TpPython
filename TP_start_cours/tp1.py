viande = str(input("Quelle viande souhaitez vous cuire(boeuf, porc, canard) "))
if( viande == "boeuf"):
    cuisson = str(input("Quelle cuisson souhaitez vous avoir pour 500 grammes(bleu, a point, bien cuit) "))
    if cuisson == "bleu":
        print("10 minutes pour une cuisson « Bleu »")
    elif cuisson == "a point":
        print("17 minutes pour une cuisson « À Point »")
    elif  cuisson == "bien cuit":
        print("25 minutes pour une cuisson « Bien Cuit »")
    else:
        print("Je ne connais pas cette cuisson")
elif (viande == "porc"):
    cuisson = str(input("Quelle cuisson souhaitez vous avoir pour 400 grammes(bleu, a point, bien cuit) "))
    if cuisson == "bleu":
        print("15 minutes pour une cuisson « Bleu »")
    elif cuisson == "a point":
        print("25 minutes pour une cuisson « À Point »")
    elif cuisson == "bien cuit":
        print("40 minutes pour une cuisson « Bien Cuit »")
    else:
        print("Je ne connais pas cette cuisson")
elif (viande == "canard"):
    cuisson = str(input("Quelle cuisson souhaitez vous avoir pour 450 grammes(bleu, a point, bien cuit) "))
    if cuisson == "bleu":
        print("20 minutes pour une cuisson « Bleu »")
    elif cuisson == "a point":
        print("25 minutes pour une cuisson « À Point »")
    elif cuisson == "bien cuit":
        print("30 minutes pour une cuisson « Bien Cuit »")
    else:
        print("Je ne connais pas cette cuisson")
else:
    print("Pas d'info de cuisson sur cette viande")