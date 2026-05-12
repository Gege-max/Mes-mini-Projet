import json

prenom = input("Entrez votre prenom : ")
age = input("Entrez votre age : ")
pays = input("Entrez votre pays : ")

personne = {
    "Prenom" : prenom,
    "Age": age,
    "Pays": pays
}

with open("utilisateur.json", "w") as fichier:
    json.dump(personne, fichier)

print("Sauvegarde reussie ! ")