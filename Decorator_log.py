def mon_decorateur(fonction):

    def wrapper():

        print("Début")

        fonction()

        print("Fin")

    return wrapper

@mon_decorateur

def bonjour():
    print("Bonjour")

bonjour()