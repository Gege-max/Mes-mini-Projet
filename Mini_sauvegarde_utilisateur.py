prenom = input("Entrez votre prenom : ")
age = input("Entrez votre age : ")

profil = {
    "Prenom": prenom,
    "Age" : age
}

with open("profil.txt", "w") as fichier:
    fichier.write("Prenom : " + profil["Prenom"] + "\n")
    fichier.write("Age : " + profil["Age"])

print("Sauvegarde Terminé")