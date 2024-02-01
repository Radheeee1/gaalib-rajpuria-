from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")
@app.route("/Hello")
def hello():
    return"Hello WORLD"
@app.route("/name")
def name():
    return"Lokesh"
@app.route("/age")
def age():
    return "40"
@app.route("/classs")
def classs():
    return "first"
@app.route("/year")
def year():
    return "2024"