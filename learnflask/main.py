
from flask import Flask ,escape, render_template,url_for,redirect

app = Flask(__name__)
@app.route("/")
def ini():
    return render_template("ini.html")
@app.route("/<string:user>")
def user(user):
    return f"hello {user}"

with app.test_request_context():
    print(url_for('user', user='John doe'))
if __name__ == '__main__':
 app.run(debug=True)
 print("dsadsadas")