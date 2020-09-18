from flask import Flask
from flask.templating import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError, InputRequired
import requests


class Main_form(FlaskForm):
    pokemon = StringField('Pokemon',
                          validators=[InputRequired()])


app = Flask(__name__)
app.config['SECRET_KEY'] = '*9cnv8to4#64l5mvn8afb2owqldv4!26t4u'


@app.route('/', methods=["GET", "POST"])
def index():
    form = Main_form()
    print(form.pokemon.data)
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
