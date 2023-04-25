import requests
from bs4 import BeautifulSoup

def get_connectors():
    import re
    response = requests.get("https://learn.microsoft.com/en-us/azure/data-factory/connector-overview")
    # Parse the HTML content of the webpage using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the table containing the data store names
    table = soup.find('table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    data_stores = []
    for row in rows:
        cols = row.find_all('td')
        if cols[1].find('a'):
            data_stores.append(cols[1].find('a').string)
    
    final_list = []
    for i in data_stores:
        # Search for the pattern in the text using regex and return the match object
        final_list.append(i.replace(' (Preview)', ''))