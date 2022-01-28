import requests

API_KEY = "a9e53b0c7fc921be70fcb096d4db4ce5"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response =  requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    #print(data)
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15)
    humidity = data ['main']['humidity']
    speed = data ['wind']['speed']
    print("Weather:", weather)
    print("Temperature:", temperature, "degrees celsius")
    print("Humidity:", humidity, "%")
    print("Wind Speed:", speed, "kmph")
else:
    print("An error occured.")
