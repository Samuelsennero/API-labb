import requests
import json
from config import input_key

city = input('Enter a city: ')

link_key = input_key()

url = (link_key.format(city))

res = requests.get(url) 
output = res.json()

values = [(output['data'][0]['app_temp']), (output['data'][0]['sunrise']), (output['data'][0]['sunset']) ]


print("Temperature in", city, ":" , values[(0)], "Celsius")
print("Sunrise today:", values[(1)])
print("Sunset today:", values[(2)])