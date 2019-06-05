#!/usr/bin/python3

from flask import Flask

app = Flask(__name__) #Always do this in your flask script

@app.route("/") # to goto the ROOT of your server
def endoftheday(): # function to trigger at ROOT
    return "Class is nearing the end for Wednesday" # Return this if you goto ROOT

if __name__ == "__main__":
    app.run(port=5006) # run on port 5006
