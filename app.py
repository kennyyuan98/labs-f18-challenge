import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/pokemon/<var>', methods=['GET'])
def pokemon(var):
    r = requests.get('https://www.pokeapi.co/api/v2/pokemon/' + var).json()
    return render_template('pokemon.html', name=r['name'], id=str(r['id']))


if __name__ == '__main__':
    app.run()
