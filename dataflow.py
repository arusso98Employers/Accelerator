import requests
from bs4 import BeautifulSoup

def get_connectors():
    import re
    url = 'https://learn.microsoft.com/en-us/connectors/connector-reference/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    connectors = soup.find_all('b')
    #print(connectors)
    pattern = '>(.*)<'
    final_list = []
    for i in connectors:
        # Search for the pattern in the text using regex and return the match object
        match = re.findall(pattern, str(i))

        # If a match is found, print the matched pattern
        res = [*set(match)]
        if res != []:
            final_list.append(res[0].replace(' (Independent Publisher)', ''))

    return final_list
