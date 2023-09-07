import requests

print("Lista de Reproducción\n")

# Referencia: https://www.deezer.com/en/channels/explore

print("Ingresa la palabra que te gustaría")
print("Ejemplo: 'rock', y obtendrás un playlist de canciones o artistas que incluyan la palabra rock")

word_to_search = input()

url = "https://deezerdevs-deezer.p.rapidapi.com/search"
querystring = {"q": word_to_search}
headers = {
    "X-RapidAPI-Key": "3ed98f551fmshe4e6260228c4eadp13db17jsn8c893e1194da",
    "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
}
response = requests.request(
    "GET", url, headers=headers, params=querystring, timeout=10).json()
for element in response['data']:
    my_list = [element['title'], element['artist']['name']]
    # print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
