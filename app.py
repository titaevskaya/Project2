from flask import Flask, render_template  # сперва подключим модуль
import json
from itertools import islice

app = Flask(__name__)  # объявим экземпляр фласка

with open("tours.json", encoding='utf-8') as file:
    tours = json.load(file)
print(type(tours))


@app.route('/')
def render_main():
    return render_template('index.html', tours=dict(islice(tours["tours"].items(), 6)), main_pic=tours["tours"]['9'],
                           tours_all_field=tours)


@app.route('/departures/<departure>/')
def render_departures(departure):
    filtered_tours = [{**v, 'id': k} for k, v in tours['tours'].items() if v.get('departure') == departure]
    return render_template('departure.html', tours=filtered_tours,
                           departures=tours["departures"], departure=departure)


@app.route('/tours/<id>/')
def render_tours(id):
    return render_template('tour.html', tour=tours["tours"][id], departures=tours["departures"])


if __name__ == '__main__':
    app.run()
