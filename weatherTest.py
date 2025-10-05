import requests

while True:
    capitalWeather = input("Please insert a capital: ")
    requestResponse = requests.get(f'http://api.weatherapi.com/v1/current.json?key=e64a9a77d8f6428aa1b92656250510&q={capitalWeather}&aqi=no')
    
    if requestResponse.status_code == 200:
        data = requestResponse.json()
        print(data['current']['condition']['text'])
        location = data['location']
        region = location['region']
        country = location['country']
        fullName = location['name']
        print(f'From: {fullName} , {region or None} , {country}')
    else:
        print('Something went wrong!')