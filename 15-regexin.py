#!/usr/bin/python3

import re ##regex library

def main():
    with open("testcap.txt", "r") as testcap:
        for line in testcap:
            regmatch = re.search(r"^Contact:\ssip:\+(\d+)@\[(.*)\]:?(\d+)?", line) ## r means raw string, avoids windows from converting the slashes into like "c:\"
            if regmatch:
                print(regmatch)          ## display match object
                print(regmatch.group())  ## display the full match
                print(regmatch.group(1)) ## display the digits of caller
                print(regmatch.group(2)) ## display the IPv6
                print(regmatch.group(3)) ## display the port

if __name__ == "__main__":
    main()

