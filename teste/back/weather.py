import requests
import json
class Weather():
    def __init__(self,city):
        self.cityData = self.cityData(city)
        
    def cityData(self, city):
        app = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b77e07f479efe92156376a8b07640ced")
        json = app.json()
        temperaturaJson = json['main']['temp']
        celsius = (temperaturaJson-32)/1.8
        return celsius
