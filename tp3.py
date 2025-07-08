pieces_acceptees = [2.0, 1.0, 0.5, 0.2, 0.1, 0.05]
prix_cafe = 0.60
credit = 0.0

stock_pieces = {
    2.0: 0,
    1.0: 0,
    0.5: 0,
    0.2: 7,
    0.1: 15,
    0.05: 20
}

while credit < prix_cafe:
    try:
        piece = float(input("Entrez la valeur de la pièce : "))
    except ValueError:
        print("Valeur non valide.")
        continue

    if piece not in pieces_acceptees:
        print("Pièce non acceptée")
        continue

    credit += piece

    if credit < prix_cafe:
        print(f"Crédit insuffisant ({credit:.2f}€/0.60€)")
    elif credit == prix_cafe:
        print("Voici votre café !")
    else:
        monnaie = round(credit - prix_cafe, 2)
        print(f"Voici votre café et votre monnaie ({monnaie:.2f}€) :")

        rendu = {}
        monnaie_restante = monnaie

        stock_temp = stock_pieces.copy()

        for p in pieces_acceptees:
            nb_piece = int(monnaie_restante // p)
            if nb_piece > 0:
                nb_disponible = stock_temp.get(p, 0)
                nb_a_rendre = min(nb_piece, nb_disponible)

                if nb_a_rendre > 0:
                    rendu[p] = nb_a_rendre
                    monnaie_restante = round(monnaie_restante - nb_a_rendre * p, 2)
                    stock_temp[p] -= nb_a_rendre

        if monnaie_restante != 0:
            print("Impossible de rendre la monnaie avec le stock disponible.")
            print("Transaction annulée, veuillez insérer le montant exact.")
            credit = 0.0
        else:
            for p, nb in rendu.items():
                stock_pieces[p] -= nb

            for val, nb in rendu.items():
                print(f"▪ {nb} pièce(s) de {val:.2f}€")
