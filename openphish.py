# @cc - Sahil Sharma
"""
Below program takes an user input and write all possible phishing sites
available in Openphish community version(text file) into given JSON file.
(eg, JSON file generate : url.json)
"""

import re
import json
import os
import requests


def phish(string):

    # fetch Openphish database
    if os.path.exists('url.txt'):
        pass
    else:
        response = requests.get('https://openphish.com/feed.txt')

        # writing above fetched data in a json file
        if response.status_code == 200:
            with open('url.txt','wb') as f:
                f.write(response.content)
        else:
            print('error')

    """
    This regex searches the complete url contains in text file of given string (e.g, brand name (paypal)) 
    """
    regex = r'(https?://[^/\s]*' + string + r'[^/\s]*)'
    #initialize an empty dictionary
    data = {}
    count = 1

    """
    read text file containing reported phishing url from Openphish community feeds
    https://openphish.com/phishing_feeds.html
    https://openphish.com/feed.txt
    """
    with open('url.txt', 'r') as f:
        for line in f:
            #using regular expression function match the url with the declared regex expression above
            match = re.search(regex, line)
            if match:
                data[count] = line.strip('\n')
                count = count+1
    return data

# User input (e.g, paypal or amazon, etc)
inp = input('brand name: ')
string = str(inp.lower())
 
output = phish(string)

# write to the JSON file
with open('url.json','w') as f:
    json.dump(output, f, indent=1)
f.close()
