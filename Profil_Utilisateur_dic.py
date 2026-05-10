prenom = input("Entrez votre prenom : ")
age = int(input("Entrez votre age : "))
pays = input("Entrez votre pays : ")

Personne = {
    "Utilisateur": prenom,
    "Age": age,
    "Pays": pays
}

for cle, valeur in Personne.items():
    print(cle, valeur)
    