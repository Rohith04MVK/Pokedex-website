from flask import Flask, url_for, redirect
from flask.templating import render_template
from flask_wtf import FlaskForm
from flask_wtf import form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError, InputRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '*9cnv8to4#64l5mvn8afb2owqldv4!26t4u'


class pokemon_form(FlaskForm):
    pokemon = StringField('Pokemon',
                          validators=[InputRequired()])


app = Flask(__name__)
app.config['SECRET_KEY'] = '*9cnv8to4#64l5mvn8afb2owqldv4!26t4u'


@app.route('/', methods=["GET", "POST"])
def index():
    form = pokemon_form()
    global pokemon
    pokemon = form.pokemon.data
    print(pokemon)
    if form.validate_on_submit():
        return redirect(url_for('info'))
    return render_template("index.html", form=form)


def get_stats():
    url = (f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    response = requests.get(url, headers={"Accept": "application/json"})
    data = response.json()
    return data


@app.route("/info", methods=["GET", "POST"])
def info():
    return get_stats()


if __name__ == "__main__":
    app.run(debug=True)
