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

# Share A Swipe About Page
@app.route("/sas_about")
def sas_about():
    return render_template("sas_about.html")

# Share A Swipe Log In
@app.route("/sas_login")
def sas_login():
    return redirect("/sas_home") # ignore login for now, assuming nyu mfa?

# Share A Swipe Home
@app.route("/sas_home")
def sas_home():
    return render_template("sas_home.html")


if __name__ == "__main__":
    app.debug = True
    app.run()