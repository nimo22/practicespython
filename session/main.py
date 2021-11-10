from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap
from db.data import Data
from read.rd import File
from verifie.verifielog import Ver
import secrets

path = File()
que = Data()
ver = Ver()

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "GET":
        if request.args.get("message") is None:
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
    return redirect(url_for('home', title="good", message="good"))


def create_db():
    que.execute(path.read("./db/insert.sql"))


if __name__ == '__main__':
    app.run(debug=True)
