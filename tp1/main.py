from flask import Flask, render_template
from function.read import Read
from database.data import Data
import sqlite3

# initiat database object
dat = Data()

app = Flask(__name__)


# this methode will check if table exist and if not it will creat one
@app.before_first_request
def chek():

    dat.disconnect()
    cheker = dat.check()
    if not cheker.fetchall():
        print("table created")
        read = Read()
        table_query = read.readfile()
        dat.create_table(table_query)
    dat.disconnect()


@app.route("/")
def ini():
    return render_template("accueil.html", title="accueil")


# @app.route("/article/")

if __name__ == '__main__':
    app.run(debug=True)
