import requests
import json

city = input('Enter a city: ')

url = 'https://api.weatherbit.io/v2.0/current?city={}&key=413e26530db141f29a0605568691c961'.format(city)

res = requests.get(url)
output = res.json()

values = [(output['data'][0]['app_temp']), (output['data'][0]['sunrise']), (output['data'][0]['sunset']) ]


print("Temperature in", city, ":" , values[(0)], "Celsius")
print("Sunrise today:", values[(1)])
print("Sunset today:", values[(2)])