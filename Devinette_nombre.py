import random


nombre = random.randint(1, 10)

utilisateur = int(input("Entrez un nombre : "))

while utilisateur != nombre:
    print("Perdu")
    utilisateur = int(input("Reessayez encore : "))
else:
    print("Bravo")
    