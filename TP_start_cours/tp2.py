numeros_cheques = []
montants_cheques = []

print("Entrez les chèques (0 pour arrêter) :")

while True:
    numero = int(input("Numéro du chèque : "))
    if numero == 0:
        break
    montant = float(input("Montant du chèque (€) : "))
    numeros_cheques.append(numero)
    montants_cheques.append(montant)

nb_cheques = len(montants_cheques)
total_montants = sum(montants_cheques)
moyenne = total_montants / nb_cheques if nb_cheques > 0 else 0

nb_inf_200 = 0
total_inf_200 = 0

nb_sup_ou_egal_200 = 0
total_sup_ou_egal_200 = 0

if nb_cheques > 0:
    montant_min = montants_cheques[0]
    numero_min = numeros_cheques[0]
    montant_max = montants_cheques[0]
    numero_max = numeros_cheques[0]

    for i in range(nb_cheques):
        montant = montants_cheques[i]
        if montant < 200:
            nb_inf_200 += 1
            total_inf_200 += montant
        else:
            nb_sup_ou_egal_200 += 1
            total_sup_ou_egal_200 += montant

        if montant < montant_min:
            montant_min = montant
            numero_min = numeros_cheques[i]
        if montant > montant_max:
            montant_max = montant
            numero_max = numeros_cheques[i]

    print("Nombre de chèques :", nb_cheques)
    print("Montant total des chèques : {:.2f} €".format(total_montants))
    print("Moyenne des montants : {:.2f} €".format(moyenne))
    print("Chèques < 200€ : {} pour un total de {:.2f} €".format(nb_inf_200, total_inf_200))
    print("Chèques >= 200€ : {} pour un total de {:.2f} €".format(nb_sup_ou_egal_200, total_sup_ou_egal_200))
    print("Chèque le plus petit : N°{} avec {:.2f} €".format(numero_min, montant_min))
    print("Chèque le plus grand : N°{} avec {:.2f} €".format(numero_max, montant_max))
else:
    print("Aucun chèque saisi.")