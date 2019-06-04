#!/usr/bin/python3
"""author: ACAGatela | learning about NASA APIs and DEV Keys"""

import requests

# creating alias for the pprint function (pprint.pprint)
from pprint import pprint as pp


MYAPI = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key="

def getkey():
    # harvest our key from /home/student/saan.susi
    with open("/home/student/saan.susi", "r") as keyfile:
        mykey = keyfile.read()
        return mykey.rstrip('\n')


def main():
    # harvest our key from /home/student/saan.susi
    nasakey = getkey()

    # append our key to MYAPI
    # call the API
    # pull json off response
    asteroidz = requests.get(MYAPI + nasakey).json()

    # parse json - loop across "near_earth_objects" to reveal asteroids
    #print(asteroidz["near_earth_objects"])
    #pp(asteroidz["near_earth_objects"])  # pretty print output to make it more readable

    for bigrock in asteroidz["near_earth_objects"]:
        if bigrock["is_potentially_hazardous_asteroid"]:
            print(bigrock["name"] + " POTENTIALLY HAZARDOUS")
            print("Proximity - ", bigrock["close_approach_data"])
            print("Size - ", bigrock["estimated_diameter"], end="\n*******\n")
        else:
            print(bigrock["name"] + " This asteroid is not a concern")

if __name__ == "__main__":
    main()

    # only display those that may pose a danger to Earth
