import requests, os
import json, urllib.request

def key_Geoapify():
    try:
        wd = os.path.dirname(os.path.realpath(__file__))
        file = open(wd + "/keys/key_Geoapify.txt", "r")
        key = file.read()
        return key
    except: 
        return 'False'

#gets the country's currency based off its name 
def get_currency(country_name):
    name = country_name
  #  res = request.get(f'https://restcountries.com/v3.1/name/{name}?fullText=true')
    data = urllib.request.urlopen(f'https://restcountries.com/v3.1/name/{name}?fullText=true')
    country_json = json.load(data)
    #print(country_json)
    currency = country_json[0]["currencies"]["CNY"]["name"]
    return currency

print(get_currency('China'))

#gets the country's gini coefficient based off its name 
def get_gini(country_name):
    name = country_name
    url = 'https://restcountries.com/v3.1/name/{name}?fullText=true'
    res = requests.get(url) 
    json = res.json() 
    gini = json["gini"][0]
    return gini

#gets the country's capital based off its name 
def get_capital(country_name):
    name = country_name
    url = 'https://restcountries.com/v3.1/name/{name}?fullText=true'
    res = requests.get(url) 
    json = res.json() 
    capital = json["capital"][0]
    return capital