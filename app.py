# basic internet ver

from flask import Flask, render_template, redirect

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# Homepage
@app.route("/")
def home():
    return render_template("home.html")

# Share A Swipe Main Page
@app.route("/sas_about")
def home():
    return render_template("sas_about.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
