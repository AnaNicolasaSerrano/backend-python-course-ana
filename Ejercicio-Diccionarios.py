import pokebase as pb
import requests

pokemon_to_search = input("Ingresa el nombre de un pokemon\n\n")
data = pb.pokemon(pokemon_to_search).__dict__
id_ = data.get('id_')
name = data.get('name')
height = data.get('height')
weight = data.get('weight')

print("ID: ", id_)
print("Nombre: ", name)
print("Altura: ", height)
print("Peso: ", weight)

url = f"https://pokeapi.co/api/v2/characteristic/{id_}/"
response = requests.get(url, timeout=10)
for description_dict in response.json().get("descriptions"):
    if description_dict.get("language", {}).get("name") == "es":
        description = description_dict.get("description")
        print("Descripción: ", description)
