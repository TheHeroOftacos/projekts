from flask import Flask, render_template, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange
from datetime import date



# Create new flask session
app = Flask(__name__, template_folder='template')

# Configure flask session
# !IMPORTANT! store these values in .env (python-dotenv)
app.config['SECRET_KEY'] = 'nMga6QCvyZ89wCYm'                           
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

# Create db connection
db = SQLAlchemy(app)

class Esana(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    vards = StringField('vārds Uzvārds')
    klase = SelectField('Izvēlies savu klasi',
        choices=[ ('', ''), ('7a', '7A'),
        ('7b', '7B'),
        ('8a', '8A'),
        ('8b', '8B'), 
        ('9a', '9A'),
        ('9b', '9B'),
        ('10vid', '10VID'),
        ('10sp', '10SP'),
        ('10vv', '10VV'),
        ('11id', '11ID'),
        ('11sp', '11SP'),
        ('11vv', '11VV'),
        ('12ek', '12EK'),
        ('12ip', '12IP'),
        ('12dz', '12DZ') ])
    diena =  RadioField('dienas', choices=[('1','Pirmdiena'),('2','Otrdiena'),('3','Trešdiena'),('4','Ceturtdiena'),('5','Piektdiena')])
    # updated - date - handled in the route function
    updated = HiddenField()
    submit = SubmitField('Iesniegt')

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True, nullable=False)
   password = db.Column(db.String(120), unique=True, nullable=False)

	

# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type
class Sock(db.Model):
    __tablename__ = 'socks'
    id = db.Column(db.Integer, primary_key=True)
    vards = db.Column(db.String)
    klase = db.Column(db.String)
    diena = db.Column(db.String)
    updated = db.Column(db.String)

    def __init__(self, vards, klase, diena, updated):
        self.vards = vards
        self.klase = klase
        self.diena = diena
        self.updated = updated


@app.route('/admin')
def admin():
    return render_template("end.html") 


@app.route('/')
@app.route('/home')
def index():
   return render_template("home.html")

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Nebūs'
        else:
            return redirect(url_for('admin'))
    return render_template('home.html', error=error)
    #https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#installation
#problēma - 
#Not Found 
#The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
#vajag salabot login pogu lai viņš sūta uz end.html

if __name__ == "__main__":
   
   # Deal with database
   try:
      # Query database
      User.query.all()
   except:
      # If query fails database
      # doesn't exits,
      db.create_all()

   # Run flask session
   app.run(debug=True, port=5000)
#username - admin password - skola
