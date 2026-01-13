import json
import requests
print("🌦️Welcome to get temp by city name program ")
city_name=input("Enter a city name : ")
api_key="6ee2873eaaec145c9adc521f361e7f6l"
api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
get_server_info=requests.get(api_url)
data =get_server_info.json()
temp=data["main"]["temp"]
print(f"☀️Temp of {city_name} is : {temp} ")
