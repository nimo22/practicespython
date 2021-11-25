from flask import Flask, render_template, redirect, url_for, request, session, make_response,escape
from flask_bootstrap import Bootstrap
from db.data import Data
from read.rd import File
from verifie.verifielog import Ver
import secrets
from flask_sqlalchemy import SQLAlchemy

path = File()
que = Data()
ver = Ver()

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/login.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
users = db.Table('users', db.metadata, autoload=True, autoload_with=db.engine)


@app.route('/view')
def view():

    all=db.session.query(users).all()
    #me=db.session.users(email="eqwe")
    insert_stmnt = users.insert().values(email="saddddddas")
    db.session.execute(insert_stmnt)
    db.session.commit()
    db.session.close()
    #db.session.add(me)
    print(all)
    return ''


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "GET":
        if request.cookies.get("logout") is None:
            return render_template("home.html", title="main")
        else:
            return render_template("home.html", message="savely home")
    else:
        if ver.ver_username_pass(ver.get_username_pass(), request.form.get('email'),
                                 request.form.get('password')) is True:
            user_email = que.cursor().execute("select email from users where username like (?)",
                                              (request.form.get("email"),)).fetchall()
            print(user_email[0][0])
            session["email"] = user_email[0][0]
            session["username"] = request.form.get('email')
            return redirect(url_for('home_page', name=request.form.get('email'), title="success"))
        else:
            return render_template("home.html", title="false")


@app.route('/ss')
def essay():
    return render_template("login.html")


@app.route('/<name>')
def home_page(name):
    if "username" in session:
        return render_template("login.html", name=name, title=request.args.get('title'), email=session["email"])
    else:

        return redirect(url_for('home', title="error"))


@app.route('/logout')
def logout():
    session.pop("username", None)
    session.pop("email", None)
    print("ok")
    res = make_response(redirect(url_for('home')))
    res.set_cookie("logout", value="you logout succefuly ", max_age=6)
    print("ok")
    res.status_code = 711

    return res


def create_db():
    que.execute(path.read("./db/insert.sql"))


if __name__ == '__main__':
    app.run(debug=False)
