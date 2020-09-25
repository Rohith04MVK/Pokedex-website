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
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()

    # abilities
    abilities = r["abilities"]

    for ability in abilities:
        print(f"Ability : {ability['ability']['name']}")
        print(f"Hidden : {ability['is_hidden']}")
        print(f"Slot : {ability['slot']}\n")

    print()

    # forms
    forms = r["forms"]

    for form in forms:
        print(f"Form name: {form['name']}\n")

    print()

    # species
    species = r["species"]

    print(f"Species name: {species['name']}\n\n")

    # types
    types = r["types"]

    for poke_type in types:
        print(f"Slot number: {poke_type['slot']}")
        print(f"Type name: {poke_type['type']['name']}\n")


@app.route("/info", methods=["GET", "POST"])
def info():
    pok = pokemon
    da = get_stats()
    return render_template("info.html", pok=pok, da=da)


get_stats()

if __name__ == "__main__":
    app.run(debug=True)
