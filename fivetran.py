import requests
from bs4 import BeautifulSoup

def get_connectors():
    url = 'https://fivetran.com/connectors'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    # find all connector names
    connectors = soup.find_all('div', {'class': 'card__json w-embed w-script'})
    names = []
    print(connectors)
    for connector in connectors:
        script = connector.find('script', {'type': 'application/json'})
        name = script.text.split('\n')[2][8:].replace(',','')
        names.append(name.replace('"', ''))
    
    file = open("html_txts/fivetran.txt")
    # read the file as a list
    data = file.readlines()
    # close the file
    file.close()
    final = []
    count = 0
    for i in data:
        if (len(i) < 40) and (i != '\n') and (i != 'Lite\n'):
            final.append(i)
        count+=1

    res = [sub[: -1] for sub in final]

    return res[0:len(res) - 1]