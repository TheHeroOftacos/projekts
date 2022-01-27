from flask import Flask, render_template, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy


# Create new flask session
app = Flask(__name__, template_folder='template')

# Configure flask session
# !IMPORTANT! store these values in .env (python-dotenv)
app.config['SECRET_KEY'] = 'nMga6QCvyZ89wCYm'                           
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

# Create db connection
db = SQLAlchemy(app)


class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True, nullable=False)
   password = db.Column(db.String(120), unique=True, nullable=False)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/admin'))
    return render_template('end.html', error=error)
#problēma - 
#Not Found 
#The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
#vajag salabot login pogu lai viņš sūta uz end.html
@app.route('/')
@app.route('/home')
def index():
   return render_template("home.html")

@app.route('/admin')
def admin():
    return render_template("end.html")


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
