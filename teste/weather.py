import requests
import json
from function import MusicKind

cidade = input('Informe uma cidade: ')
app = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+cidade+"&appid=b77e07f479efe92156376a8b07640ced")
json = app.json()
temperatura = json['main']['temp']
celsius = (temperatura-32)/1.8
genre = MusicKind(celsius)
print(genre.musicKind)