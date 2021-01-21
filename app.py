from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_create = db.Column(db.DateTime, default=datetime.now)


@app.route('/<name>/<location>', methods=['POST'])
def create_user(name, location):
    user = User(name=name, location=location)
    db.session.add(user)
    db.session.commit()

    return user, 201


@app.route('/<name>', methods=['GET'])
def get_user(name):
    user = User.query.filter_by(name=name).first()
    response = {'name': user.name, 'location': user.location}

    return response, 200

