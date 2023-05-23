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
def get_lang(country_name):
    name = country_name
  #  res = request.get(f'https://restcountries.com/v3.1/name/{name}?fullText=true')
    data = urllib.request.urlopen(f'https://restcountries.com/v3.1/name/{name}?fullText=true')
    country_json = json.load(data)
    #print(country_json)
    currency = country_json[0]["languages"].values()
    currency = list(currency)
    return (currency[0])

#gets the country's gini coefficient based off its name 
def get_gini(country_name):
    name = country_name
    data = urllib.request.urlopen(f'https://restcountries.com/v3.1/name/{name}?fullText=true')
    country_json = json.load(data)
    gini = country_json[0]["gini"].values()
    gini = list(gini)
    return (gini[0])

#gets the country's capital based off its name 
def get_capital(country_name):
    name = country_name
    data = urllib.request.urlopen(f'https://restcountries.com/v3.1/name/{name}?fullText=true')
    country_json = json.load(data)
    gini = country_json[0]["capital"][0]
    return gini

#gets the country's common name based off its name 
def get_common_name(country_name):
    name = country_name
    data = urllib.request.urlopen(f'https://restcountries.com/v3.1/name/{name}?fullText=true')
    country_json = json.load(data)
    common_name = country_json[0]["name"]["common"]
    return common_name

#gets the country's official name based off its name 
def get_official_name(country_name):
    name = country_name
    data = urllib.request.urlopen(f'https://restcountries.com/v3.1/name/{name}?fullText=true')
    country_json = json.load(data)
    official_name = country_json[0]["name"]["official"]
    return official_name

#gets the country's flag based off its name
def get_flag(country_name):
    name = country_name
    data = urllib.request.urlopen(f'https://restcountries.com/v3.1/name/{name}?fullText=true')
    country_json = json.load(data)
    flag_url = country_json[0]["flags"].values()
    flag_url = list(flag_url)
    return (flag_url[1])

#print(get_lang('China'))
#print(get_gini('China'))
#print(get_capital('China'))print(get_common_name('China'))
#print(get_official_name('China'))

#print(get_lang('sweden'))
#print(get_gini('sweden'))
#print(get_capital('sweden'))
#print(get_common_name('sweden'))
#print(get_official_name('sweden'))