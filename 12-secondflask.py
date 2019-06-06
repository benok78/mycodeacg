#!/usr/bin/python3

from flask import Flask, redirect, url_for ##importing classes from flask library
app = Flask(__name__)

@app.route("/admin") ##admin url
def hello_admin():
    return "Hello admin!"

@app.route("/guest/<guest>") ##guest url
def hello_guest(guest):
    return "Hello {} Guest".format(guest)

@app.route("/user/<name>") ##user url
def hello_user(name):
    if name.lower() == "admin":  ##user entered admin
        return redirect(url_for("hello_admin"))  ##user will be redirected to admin url 
    else:
        return redirect(url_for("hello_guest", guest=name))  ##user will be redirected to guest url if name is not admin


if __name__ == "__main__":
    app.run(port=5005)

