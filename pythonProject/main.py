
import sqlite3
from flask import Flask,render_template
conn=sqlite3.connect("customer.db")

app = Flask(__name__)
@app.route('/')
def index():
 return render_template("f.html")

@app.route('/', methods=['POST'])
def home():
  return render_template("home.html")

if __name__ == '__main__':
 app.run(debug=True,port=800)

