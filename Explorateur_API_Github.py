import requests


reponse = requests.get("https://api.github")

print(reponse.status_code)

data = reponse.json()

print(data["current_user_url"])
print(data["authorizations_url"])
print(data["repository_url"])