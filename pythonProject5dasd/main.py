from flask import Flask, Request, Blueprint, render_template, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import secrets
import os
import requests
import json

# global variable
base_directory = os.getcwd()

# initialasation
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + base_directory + '/db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


def inpt():
    nam = input("please enter your name\n")
    stri = True

    while stri is True:
        try:
            print(type(nam))
            int(nam)
            print("{0} is not a valide name ,please try again".format(nam))
            nam = input("please enter a valide name\n")
        except Exception as e:
            stri = False
            continue

    return nam


def add_to_table(nam):
    new_input = Person(name=nam)
    db.session.add(new_input)
    db.session.commit()


def create():
    db.create_all()


class PersonSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Person

    id = ma.auto_field()
    name = ma.auto_field()


class AuthorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Person

    id = ma.auto_field()
    name = ma.auto_field()


@app.route("/", methods=['GET'])
def affiche():
    person_schema = AuthorSchema()
    print("ok")
    one = Person.query.all()
    print(one)
    y = []
    for persons in one:
        y.append(person_schema.dump(persons))
    print("ok")
    nada = {
        "name": "ali",
        "local": "500"
    }
    print(jsonify(name="ddd",
            email="aa",
            id=1))
    print("----------------")
    print(jsonify({"data":nada}))
    resp=make_response(render_template("try.html",result=y, x=jsonify(nada)))

    return jsonify({"data":nada})

@app.route("/res")
def res():
    res="http://127.0.0.1:4999/"
    response=requests.get(res)
    js=json.load(response)
   # print(js['name'])
    return "p"



if __name__ == "__main__":
    app.run(debug=True)
    create()

'''
 #app.run(debug=True)
    create()
    person_schema = AuthorSchema()
    #add_to_table("john")
    one=Person.query.all()
    print(one)
    for persons in one:
        y = person_schema.dump(persons)
        print(y)
    for x in range(5):
        add_to_table(inpt())'''
