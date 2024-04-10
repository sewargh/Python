import requests
import time
import hashlib

#taking user input
id = input("Enter the id of the joke you want: ")
#url of the 10 jokes.
url = 'https://official-joke-api.appspot.com/random_ten'
flag = True ;c=0

while flag:
    print("\nTRIAL ***********\t" + str(c) + "\t***********")
    #requesting the url
    content = requests.get(url);    contentjson = content.json();   c+=1
    #check return value status
    if (content.status_code) != 200 :
        #We might get " rate_limit_exceeded " after trying too much at once :D
        if (content.status_code) == 429:
            print('rate_limit_exceeded : Try again in 15 minute(s).')
        else:
            print("Invalid")
        quit()
    else:
        #loop through every joke individually to check it's id
        for i in range(len(contentjson)):
            print (contentjson[i]['id'],end=" ")
            #if it is not the id entered by the user continue looping             
            if int(contentjson[i]['id']) != int(id) :
                continue
            else:
                #if id is found set flag to false end exit the while loop
                print("!! \nIn Trial #" + str(c) )
                print("Found " + str(contentjson[i]['id'])  + "!! Congratulation!  " )
                flag = False
                print(contentjson[i]['setup'])
                if (len(input("Guess the answer:\n ") )!= 0):
                    punchline = hashlib.md5(contentjson[i]['punchline'].encode('utf-8')).hexdigest()
                    print(punchline + '\t:3')
                else: 
                    print("Try again, and try to guess!")
quit()
