def est_palindrome_mot(mot):
    mot = mot.lower().replace(" ", "")
    return mot == mot[::-1]

# 🔎 Exemple de test
print(est_palindrome_mot("Radar"))
print(est_palindrome_mot("Python"))
print(est_palindrome_mot("Engage le jeu que je le gagne"))