# Pour un logiciel de gestion rh d'une agence d'interim
# complétez la fonction suivante sui calcule le salaire journalier
# d'un intérimaire
# après 8 heures de travail, les heures sont majorées de 25%, après 11heures de 50%

def calcul_salaire_journalier(nb_heures, taux_horaire):
    def calcul_tranche(heures, taux):
        return heures * taux

    salaire = 0

    if nb_heures <= 8:
        salaire = calcul_tranche(nb_heures, taux_horaire)
    elif nb_heures <= 11:
        heures_normales = 8
        heures_25 = nb_heures - 8
        salaire = ( calcul_tranche(heures_normales, taux_horaire) + calcul_tranche(heures_25, taux_horaire * 1.25))
    else:
        heures_normales = 8
        heures_25 = 3
        heures_50 = nb_heures - 11
        salaire = ( calcul_tranche(heures_normales, taux_horaire) + calcul_tranche(heures_25, taux_horaire * 1.25) + calcul_tranche(heures_50, taux_horaire * 1.5))

    return salaire

heures = float(input("Entrez le nombre d'heures travaillées : "))
taux = float(input("Entrez le taux horaire en euros : "))

salaire = calcul_salaire_journalier(heures, taux)
print(f"Salaire journalier : {salaire:.2f} €")