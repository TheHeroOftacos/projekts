from flask import Flask, request, flash, url_for, redirect, render_template
import sqlalchemy as db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)

class login(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True, nullable=False)
   password = db.Column(db.String(120), unique=True, nullable=False)

def __init__(self):
   return '<User %r>' % self.username