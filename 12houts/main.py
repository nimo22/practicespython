from redo import Re
from db.db import Data
from flask import Flask, render_template, request, make_response, session, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from flask_marshmallow import Marshmallow
import secrets

# predifined values
database = Data()
app = Flask(__name__)
ma = Marshmallow(app)
app.secret_key = secrets.token_urlsafe(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
base = automap_base()
base.prepare(db.engine, reflect=True)
users = base.classes.users


class UserSchema(ma.Schema):
    class Meta:
        model = users
@app.route("/json")
def index():
    one_user=db.session.query(users).all()
    user_schema=UserSchema(many=True)
    output=user_schema
    return jsonify({'user' :output})

@app.route("/", methods=["POST", "GET"])
def bonjour():
    y = db.session.query(users).all()
    if request.method == "GET":
        return render_template("form.html")
    else:
        session["loguser"] = request.form.get("email")
        new_email = session["loguser"]
        password = request.form.get("password")
        db.session.add(users(name=new_email, password=password))
        db.session.commit()

        for x in y:
            print(x.name)
        return redirect(url_for("log"))


@app.route("/log")
def log():
    return render_template("customer.html", user=session['loguser'])


@app.route("/logout")
def logout():
    session.pop('loguser')
    return f"<p>logout<p>"


@app.route("/all-users")
def all_users():
    deleted_user = db.session.query(users).filter_by(name=session['loguser']).all()
    for x in deleted_user:
        db.session.delete(x)
    remain = db.session.query(users).all()
    for x in remain:
        print(x.name)
    name = session['loguser']
    session.pop('loguser')
    db.session.commit()
    return render_template("done.html", user=name)


if __name__ == '__main__':
    app.run(debug=True, port=4999)
