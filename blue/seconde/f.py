from flask import Flask,render_template,Blueprint,make_response

seconde=Blueprint("seconde",__name__,template_folder='templates')

@seconde.route("/")
def hello():
    my_response=make_response(render_template("hi.html"))
    my_response.status_code=269
    my_response.headers['warning']='warning'
    return my_response