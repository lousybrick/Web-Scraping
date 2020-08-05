import pandas as pd
import requests
import json

df = pd.read_csv('ID.csv')
IDlist = list(df.ID)

titles = ["ID","Joke"]
with open('chuck_norris.csv','w',encoding = 'UTF-8') as file:
    header = ",".join(titles)
    header += '\n'
    file.write(header)
    
    for row in IDlist:
        joke = ""
        joke += str(row)
        url = "http://api.icndb.com/jokes/{}".format(row)
        response = requests.get(url)
        json_string = json.loads(response.content)
        string = json_string['value']['joke']
        if ',' in string:
            joke = joke + ',' + '"' + string + '"' + '\n'
        else:
            joke = joke + ',' + string + '\n'
        file.write(joke)