#Laika noteikšana

import requests

URL = "https://worldtimeapi.org/api/timezone/Europe/Riga"
dati = requests.get(URL)
print(dati)
laiksLatvija = dati.json()
print(laiksLatvija)
print(laiksLatvija["datetime"])

#ASV, New_York

URL2 = "https://worldtimeapi.org/api/timezone/America/New_York"
dati2 = requests.get(URL2)
print(dati2)
laiksAmerika = dati2.json()
print(laiksAmerika)
print(laiksAmerika["datetime"])
