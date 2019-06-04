#!/usr/bin/python3
"""author: ACAGatela | learning about API requests """

import requests

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    try:
        # make a request --- 2 ways to do it, see below
        #resp = requests.get(MAJORTOM) # activate pyj
        pyj = requests.get(MAJORTOM).json()

        # convert string data to JSO
        #pyj = resp.json() # activate resp
    
        # parse out JSON we stripped off response
        astrocosmo = pyj.get("people")

        # display selected data on screen - names of people in space
        print("CURRENTLY IN SPACE")
        for spaceperson in astrocosmo:
            print(spaceperson["name"])
    except:
        print("API is unavailable at the moment")
        exit()
    
if __name__ == "__main__":
    main()
