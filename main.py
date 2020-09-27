from flask import Flask, url_for, redirect
from flask.templating import render_template
from flask_wtf import FlaskForm
from flask_wtf import form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError, InputRequired
import requests
app = Flask(__name__)
app.config['SECRET_KEY'] = '*9cnv8to4#64l5mvn8afb2owqldv4!26t4u'


app = Flask(__name__)
app.config['SECRET_KEY'] = '*9cnv8to4#64l5mvn8afb2owqldv4!26t4u'

class pokemon_form(FlaskForm):
    pokemon = StringField('Pokemon',
                          validators=[InputRequired()])
@app.route("/", methods=["GET", "POST"])
def index():
    form=pokemon_form()
    global pokemon
    pokemon = form.pokemon.data
    if form.validate_on_submit():
        return redirect(url_for('info'))
    return render_template("index.html", form=form)

@app.route("/info", methods=["GET", "POST"])
def info():
    pok = pokemon
    print(pokemon)
    return render_template("info.html", pok=pok)




if __name__ == "__main__":
    app.run(debug=True)
    
