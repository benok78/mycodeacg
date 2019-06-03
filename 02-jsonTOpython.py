#!/usr/bin/python3
"""Author:ACAGatela | Learning json to python"""

# pull in json lib so we can parse out json
import json

def main():
    # open the jonsnow.json file in read mode
    with open("jonsnow.json", "r") as gotdata:
        jonsnow = gotdata.read() # create a STRING of all the json
        GOTpy = json.loads(jonsnow) # convert STRING to pythonic LISTs and DISCTs
    #print(GOTpy) # print GOTpy data 
    print(GOTpy["url"]) # print GOTpy url
    #print(GOTpy["titles"][0]) # print GOTpy titles
    print(GOTpy["aliases"])  # print GOTpy aliases
    
    # create 
    with open("aliases.txt", "w") as jsaliases:
        for gotalias in GOTpy["aliases"]:
           print(gotalias, file=jsaliases)
    
    #print(jonsnow["url"]
    # parse the jonsnow.json file for...
    # display character name
    # display character aliases / titles
    # display the API for ???



if __name__ == "__main__":
    main()

