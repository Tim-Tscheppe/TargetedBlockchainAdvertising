from bottle import run, route, request, template

@route("/")
def index():
    return template("FrontEnd.html")

@route("/form", method=*T)
def form