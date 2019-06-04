#!/usr/bin/python3
"""author: ACAGatela | learning about API requests """

import json
import urllib.request

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    # make a request
    resp = urllib.request.urlopen(MAJORTOM)

    # make python strip json data from the 200 response
    jstring = resp.read()
    
    # convert string data to JSO
    pyj = json.loads(jstring.decode('utf-8'))
    
    # parse out JSON we stripped off response
    astrocosmo = pyj.get("people")

    # display selected data on screen - names of people in space
    print("CURRENTLY IN SPACE")
    for spaceperson in astrocosmo:
        print(spaceperson["name"])
    
    
if __name__ == "__main__":
    main()
