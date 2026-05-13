import asyncio

async def connexion():

    print("Connexion API....")

    await asyncio.sleep(3)

    print("Données recues")


asyncio.run(connexion())