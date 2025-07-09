# créez une fonction qui prend en paramètres un **kwargs
# et qui renvoi la concaténation de toutes les clés valeur
# exemple function(je="suis", un="kwarg") doit renvoyer "jesuisunkwarg"
# exemple function(la="jolie", maison="dans", la="prairie") doit renvoyer "lajoliemaisondanslaprairie"

def concatener(**kwargs):
    test = ""
    for key, value in kwargs.items():
        test += str(key) + str(value)
    return test


print(concatener(je="suis", un="kwarg"))

print(concatener(la="jolie", maison="dans", prairie="verte"))
