from flask import Flask, render_template,request,url_for,redirect
app = Flask(__name__)

arr=[
    {
        "auteur": "mohamad-ali berry",
        "lieu": "montreal",
        "boulot": "programmer"
    },
    {
        "auteur": "shaza hammoud",
        "lieu": "montreal",
        "boulot": "banque"
    }
]
"""
basicly this is the index of the application
"""
@app.route("/home")
@app.route("/")
def hello():
    tata()
    return render_template("home.html",arr=arr,title="home")
def tata():
    x=3
    return x
@app.route("/form",methods=["POST","GET"])
def register():
    if request.method == "POST" :
        user =request.form["exampleInputEmail1"]
        print(user)
        password=request.form["exampleInputPassword1"]
        return redirect(url_for("success",user=user,password=password))
    else:
        return render_template("form.html",title="registre")
@app.route("/<user>/<password>")
def success(user,password):
    return  render_template("succes.html",user=user,password=password,title="horai")
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    name="momo"
    age="27"
    print(f"hello,{name}. age {age}")
    for x in arr:
        print(x.get("lieu"))

    for x in arr:
       for y,z in x.items():
         print(y+" : "+z)

    app.run(debug=True,port=600)




