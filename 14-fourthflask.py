#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hellobasic.html")  ## html file should be in folder templates

@app.route("/<username>")
def usertemp(username):
    return render_template("helloname.html", name = username)

@app.route("/scoretest/<int:score>")  ## the int makes the score an integer
def scorer(score):
    return render_template("highscore.html", marks=score)

if __name__ == "__main__":
    app.run(port=5005)


