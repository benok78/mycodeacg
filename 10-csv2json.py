#!/usr/bin/python3

import csv
import json

def main ():
    # open a file to dump json to
    jsonf = open('superbirths.json', 'w')

    # open our csv file to read in csv to python format
    with open('superbirths.csv') as csvf:
        reader = csv.DictReader(csvf)
        json.dump(list(reader), jsonf)

    jsonf.close() # close the superbirths.json file 

if __name__ == '__main__':
    main()

