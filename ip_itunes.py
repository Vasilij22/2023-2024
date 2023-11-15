import requests
import json

URL = "https://itunes.apple.com/search?entity=song&limit=25&term=weezer"

atbilde = requests.get(URL)

print(atbilde)

dati = atbilde.json()

print(json.dumps(dati,indent = 2))

#Konkreta datu izvadišana

#print(dati["results"][0]["trackName"])
#print(dati["results"][1]["trackName"])

#izveido veidu ka var iegut jebkadu skaitu ar nosaukumiem.Piemeram, ja pieprasijuma tiks prasits 20 dziesmas

for a in dati["results"]:
    nosaukums = a["trackName"]
    print(nosaukums)
