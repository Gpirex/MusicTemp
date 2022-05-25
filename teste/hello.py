from flask import Flask, request, redirect
from flask import render_template
from flask import url_for
from back.musicKind import *
from back.weather import *
from back.spotify import * 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/result')
def result():
    playlist = request.args['playlist']
    print(playlist)
    return render_template("result.html")

@app.route('/getData', methods=['GET'])
def inputCity():
    city_name = request.args.get("city_name")
    temp = Weather(city_name)
    musicGenre = MusicKind(temp.cityData)
    list = Tracks(musicGenre.musicKind)
    tracks = list.category

    return redirect(url_for('result', playlist=tracks))


if __name__ == '__main__':
    app.run(debug=True,port='8080')