import requests
import sys

#take user input ip
IP = sys.argv[1]

url = "https://www.virustotal.com/api/v3/ip_addresses/"+IP

#header parameter to put in the get request ;; api key that identifies my request and content type.
headers = {
    "accept": "application/json",
    "x-apikey": "2242ec6316a20ed9e85b4bcf808603249a9f68abe94d38e3cba392c1a33fd16c"
}
response = requests.get(url, headers=headers)
responseJSON = response.json()
#print(response.text)
#check reponse code for any mistake
if response.status_code == 200: 
    #print the owner of ip 
    owner = responseJSON['data']['attributes']['as_owner']
    #print latest analyst on the ip
    analyData = responseJSON['data']['attributes']['last_analysis_stats']
    print(f"################ IP DATA ################ \n as owner = {owner}\n last_analysis_stats = {analyData}  ")

elif response.status_code == 401:
    errormsg = responseJSON['error']['message']
    print(f"Error {errormsg}" )
