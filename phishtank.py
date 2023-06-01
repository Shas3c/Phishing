#@cc - Sahil Sharma
"""
Below program takes an user input and write all possible 
phishing sites available in phishtank database gives output as JSON file.
(eg, JSON file generate : phishtank_output.json)
"""

import json
import os
import requests

def phishtank(target):
    # initialize an empty dictionary
    mydict = {}
    count = 1

    # fetch phishtank database 
    if os.path.exists('phishtank.json'):
        print('already exist')
        pass
    else:
        url = f"http://data.phishtank.com/data/online-valid.json"

        response = requests.get(url)
        
        # writing above fetched data in a json file
        if response.status_code == 200:
            with open("phishtank.json", "wb") as f:
                f.write(response.content)
                print("PhishTank database downloaded successfully!")
        else:
            print("Error downloading PhishTank database")

    # read json file downloaded from (http://data.phishtank.com/data/online-valid.json)
    f = open('phishtank.json')
    data = json.load(f)

    # Iterate over the JSON formatted data
    for i in data:

        # add all those urls in the dictionary upon matches the target attribute in data with the user input. 
        if (i['target'].lower()) == (target.lower()):
            mydict[count] = (i['url'])
            count = count + 1

    return mydict

# Write output to JSON file.
with open('phishtank_output.json', 'w') as f:
    inp = input('enter company name:')
    output = phishtank(inp)
    json.dump(output, f, indent=1)
f.close()
