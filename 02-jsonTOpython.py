#!/usr/bin/python3
"""Author:ACAGatela | Learning json to python"""

# pull in json lib so we can parse out json
import json

def main():
    # open the jonsnow.json file in read mode
    with open("jonsnow.json", "r") as gotdata:
        jonsnow = gotdata.read() # create a STRING of all the json
        GOTpy = json.loads(jonsnow) # convert STRING to pythonic LISTs and DISCTs
    #print(GOTpy) 
    print(GOTpy["url"])
    #print(GOTpy["titles"][0])
    print(GOTpy["aliases"])
    for gotalias in GOTpy["aliases"]:
        print(gotalias)
    #print(jonsnow["url"]
    # parse the jonsnow.json file for...
    # display character name
    # display character aliases / titles
    # display the API for ???



if __name__ == "__main__":
    main()

