from flask import Flask, url_for, redirect
from flask.templating import render_template
from flask_wtf import FlaskForm
from flask_wtf import form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError, InputRequired
import requests


def get_stats():
    r = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()

    # abilities
    abilities = r["abilities"]

    for ability in abilities:
        Ability = ability['ability']['name']
        Hidden = ability['is_hidden']
        Slot = ability['slot']

    # forms
    forms = r["forms"]

    for form in forms:
        Form_name = (form['name'])

    print()

    # species
    species = r["species"]

    Species_name = species['name']

    # types
    types = r["types"]

    for poke_type in types:
        Slot_number = (poke_type['slot'])
        Type_name = (poke_type['type']['name'])
    return Slot_number, Hidden, Type_name, Species_name, Form_name, Slot, Ability


app = Flask(__name__)
app.config['SECRET_KEY'] = '2fex6bw*mt03ocad82q1loylh68#kik7!'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


class pokemon_form(FlaskForm):
    pokemon = StringField('Pokemon',
                          validators=[InputRequired()])


@app.route("/", methods=["GET", "POST"])
def index():
    global pokemon_name
    form = pokemon_form()
    pokemon_name = form.pokemon.data
    if form.validate_on_submit():
        return redirect(url_for('info'))
    return render_template("index.html", form=form)


@app.route("/info", methods=["GET", "POST"])
def info():
    pok = pokemon_name
    Slot_number, Hidden, Type_name, Species_name, Form_name, Slot, Ability = get_stats()
    return render_template("info.html", Slot_number=Slot_number, pok=pok, Hidden=Hidden, Type_name=Type_name, Species_name=Species_name, Form_name=Form_name, Slot=Slot, Ability=Ability)


if __name__ == "__main__":
    app.run(debug=True)
