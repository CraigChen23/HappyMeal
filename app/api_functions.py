import requests
import os
import json

def key_Geoapify():
    try:
        wd = os.path.dirname(os.path.realpath(__file__))
        file = open(wd + "/keys/key_Geoapify.txt", "r")
        key = file.read()
        return key
    except: 
        return 'False'

#gets the country's population based off its name 
def get_population(official_name):
    name = official_name
    url = 'https://restcountries.com/v3.1/name/{name}?fullText=true'

    

