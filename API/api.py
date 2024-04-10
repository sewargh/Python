import sys
import requests
import hashlib

################TASK0################

#descriptor for the file to read from
f = open("name.txt","r")
try:
    name = f.read()
    print("Task 0 => " + name)
    f.close()
except IOError:
    print("could not open file")

################TASK1################

urlcurrencies = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"
#requesting all currencies using get method in http
currencies = requests.get(urlcurrencies)
if(currencies.status_code != 200):
    print('something wrong happened')
else:
    #serializing returned data 
    currenciesjs = currencies.json() 
    print("Task 1 => XRP currecy is " + currenciesjs['xrp'] + " : " + hashlib.md5(currenciesjs['xrp'].encode('utf-8')).hexdigest())

################TASK2################

#to get a specific currency append it at the ed with .json 
urlEURexchangerate  = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur.json"
EURexchCurr  =  requests.get(urlEURexchangerate)
if(EURexchCurr.status_code != 200):
    print('something wrong happened')
else:
    print("\nTask 2 => ", end  = "eur to usd = ")
    print(EURexchCurr.json()['eur']['usd'] , end = "/ eur to rub = ")
    print(EURexchCurr.json()['eur']['rub'])

################TASK3################

#to get the exchange rate between to contries put the first conutry then the other country with.json
urljodtorub = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/jod/rub.json"
jodtorub = requests.get(urljodtorub)
if(jodtorub.status_code != 200):
    print('something wrong happened')
else:
    print("\nTask 3 => Status Code is ", end = " ")
    print(jodtorub.status_code, end="\nwhole response is :")
    print(jodtorub.json())

################TASK4################

#the exact date can be specified in the url 
urldatetcTOusd = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/2023-01-01/currencies/btc/usd.json")
#the latest available currency up to now can be accessed with latest 
urlnowtcTOusd = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/btc/usd.json")
if(urldatetcTOusd.status_code != 200 or urlnowtcTOusd.status_code != 200):
    print('something wrong happened')
else:
    print("\nTask 4 => " , end = "btc to usd in 2023-01-01 = ")
    print(urldatetcTOusd.json()['usd']  , end = " \nbtc to usd in latest (now) = ")
    print(urlnowtcTOusd.json()['usd'])

#findig the difference 
exchRateDiff = float(urldatetcTOusd.json()['usd']  - urlnowtcTOusd.json()['usd'])
print("exchange rate differece = "  + str(abs(exchRateDiff)) )

try:
    #writing to a file
    fwrite = open("output.txt","w")
    fwrite.write("btc to usd in latest (now) = " + str(urlnowtcTOusd.json()['usd']))
    fwrite.write("\nbtc to usd in 2023-01-01 = " + str(urldatetcTOusd.json()['usd']))
    fwrite.write("\nexchange rate differece between btc and usd now = "  + str(abs(exchRateDiff)))
    fwrite.close()
except IOError:
    print("could not open file")
