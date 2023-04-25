import requests
from bs4 import BeautifulSoup

def get_connectors():
    import re
    url = "https://docs.aws.amazon.com/athena/latest/ug/connectors-prebuilt.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    connectors = soup.find_all('li')
    names = []
    for i in connectors:
         name = i.find_all('a')
         names.append(name)

    pattern = '>(.*)<'
    final_list = []
    for i in names:
        # Search for the pattern in the text using regex and return the match object
        match = re.findall(pattern, str(i))

        # If a match is found, print the matched pattern
        res = [*set(match)]
        if res != []:
            final_list.append(res[0])

    return final_list[3:]