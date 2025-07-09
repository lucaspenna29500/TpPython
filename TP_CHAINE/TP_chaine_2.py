# comptez le nombre de voyelles et de consonnes dans un string

str = str(input('Enter a string: ')).lower()
voyelles = "aeiouy"
compte_voyelles = 0
compte_consonnes = 0

for lettre in str:
    if lettre.isalpha():
        if lettre in voyelles:
            compte_voyelles += 1
        else:
            compte_consonnes += 1

print(f"Nombre de voyelles : {compte_voyelles}")
print(f"Nombre de consonnes : {compte_consonnes}")

