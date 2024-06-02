import requests
import json

city= input("Enter city name your want weather conditions of:");
url = f"https://api.weatherapi.com/v1/current.json?key=525c9d1cee8e4f79920145056232012&q={city}";

r= requests.get(url);
wDetails= json.loads(r.text);

print(f"TEMPRETURE OF {city},{wDetails['location']['region']},{wDetails['location']['country']} is {wDetails['current']['temp_c']} Degree celcius and Weather is {wDetails['current']['condition']['text']}");
print(f"last updated on {wDetails['current']['last_updated']} {wDetails['location']['tz_id']}");
