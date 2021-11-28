from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import secrets
import os

# global bariable
os = os.getcwd()
# initialisation
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os + '/db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Caar(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    moddel = db.Column(db.String(50), unique=False)


class Auttthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class CarSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Caar

    id = ma.auto_field()
    moddel = ma.auto_field()


class AuttthorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Auttthor

    id = ma.auto_field()
    name = ma.auto_field()


if __name__ == "__main__":
    #
    author_schema = AuttthorSchema()

    print(author_schema.dump(Auttthor.query.first()))

    car_schema = CarSchema()

    print(car_schema.dump(Caar.query.first()))
