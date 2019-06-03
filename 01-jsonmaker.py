#!/usr/bin/python3
"""Author: ACAGatela | Email: cagatela@hotmail.com | learning json with python"""

# with python, the jsonbatteries are in the box, but you need to plug them in
import json

def main():
    # create a list of dictionaries
    mlbteams = [{"baltimore": "orioles", "newyork": "yankees", "boston": "redsox", "washington": "nationals"}, {"florida": "marlins", "toronto": "bluejays"}]

    # show the values of mlbteams
    print(mlbteams)

    #create a local file
    with open("mlbteams.json", "w") as bballfile: # "w" = write, "r" = read, "a" = append
        json.dump(mlbteams, bballfile)


if __name__ == "__main__":
    main()

