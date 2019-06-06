#!/usr/bin/python3

from flask import Flask

app = Flask(__name__) #Always do this in your flask script

@app.route("/") # to goto the ROOT of your server
def endoftheday(): # function to trigger at ROOT
    return "Test message" # Return this if you goto ROOT

@app.route("/hello/<name>", defaults={'position': 'Administrative Assistant'})
@app.route("/hello/<name>/<position>")
def hellostudents(name, position):
    #return "Welcome to class..." + name
    return "Hello {1} {0}. I am pleased to meet you".format(name, position)

if __name__ == "__main__":
    app.run(port=5005) # run on port 5006
