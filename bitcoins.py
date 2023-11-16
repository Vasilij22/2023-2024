import requests

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

bitcoin = requests.get(URL)
print(bitcoin.json())
cena = bitcoin.json()['bpi']['USD']['rate_float']

input = float(input('ievadi cik gribi kupit: '))

print(cena * input)
