class MonContext:

    def __enter__(self):

        print("Connexion ouverte")

    def __exit__(self, exc_type, exc_val, exc_tb):

        print("Connexion fermée")

with MonContext():
    print("Traitement des données")