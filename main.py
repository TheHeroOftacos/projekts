# from venv import create
# from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__, template_folder="template")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)


# @app.route('/')
# def index():
#    return render_template("home.html")
# class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(80), unique=True, nullable=False)
#    password = db.Column(db.String(120), unique=True, nullable=False)
   
#    def __repr__(self):
#         return '<User %r>' % self.username

# @app.route('/admin')
# def admin():
#     return render_template("end.html")


# if __name__ == "__main__":
#    # app.run(debug=True)