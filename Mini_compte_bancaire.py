class CompteBancaire:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde

        print("Le compte de : ", self.nom)
        print("Solde : ", self.solde)

    def deposer(self, montant):
        self.solde += montant
        print("Depot de : ", montant)

    def retirer(self, montant):
        self.solde -= montant

        print("Retrait de : ", montant)

    def afficher_solde(self):
        print("Le solde final est ", self.solde)

Compte = CompteBancaire("Germain", 1000)
Compte.deposer(500)
Compte.retirer(200)
Compte.afficher_solde()
        