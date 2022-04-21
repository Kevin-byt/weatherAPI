import requests

from keys import API_KEY #personal file with key

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requestUrl = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(requestUrl)
if response.status_code == 200:
    data = response.json()
    # print(data) prints all the data from the api
     
    weather = data['weather'][0]['description']
    temp = data['main']['temp']

    print(f'The weather is {weather}')
    print(f'The temperature is {temp} degrees Kelvin = {round(temp-273, 2)} degrees celcius')

else:
    print("Invalid Response")
