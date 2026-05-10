prenom = input("Entrez votre prenom : ")
note = int(input("Entrez votre note : "))

def etudiant(Prenom, note):
    if note >= 10:
        print("Bonjour", prenom, "resultat : Admis")
    else:
        print("Bonjour", prenom, "resultat : Echec")

etudiant(prenom, note)