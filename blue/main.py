from flask import Flask
from seconde.f import seconde

app = Flask(__name__)
app.register_blueprint(seconde, url_prefix="")

if __name__ == "__main__":
    app.run(debug=True,port=3000)
