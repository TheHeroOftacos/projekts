from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class edaji(db.Model):
   id = db.Column('edaji_id', db.Integer, primary_key = True)
   vards = db.Column(db.String(50))
   klase = db.Column(db.String(50))

def __init__(vards, klase):
   self.vards = vards
   self.klase = klase

@app.route('/')
def show_all():
   return render_template('home.html', edaji = edaji.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['vards'] or not request.form['klase']:
         flash('Kļūme', 'error')
      else:
         edaji = edaji(request.form['vards'], request.form['klase'])
         
         db.session.add(edaji)
         db.session.commit()
         flash('Paldies')
         return redirect(url_for('home'))
   return render_template('home.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)