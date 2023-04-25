import requests
from bs4 import BeautifulSoup

def get_connectors():
    import re
    url = 'https://hub.meltano.com/extractors'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    # Find all the connectors
    connector_list = soup.find_all('div', {'class': 'rounded-md text-slate-800 h-48 hover:bg-white bg-white-07 p-2 md:p-4 overflow-hidden border border-purple/10'})
    # Extract the names of the connectors
    connector_names = [connector.text.strip() for connector in connector_list]
    # Print the list of connector names
    #print(connector_names)
    for i in range(2,6):
        url = 'https://hub.meltano.com/extractors/' + str(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup)
        # Find all the connectors
        connector_list = soup.find_all('div', {'class': 'rounded-md text-slate-800 h-48 hover:bg-white bg-white-07 p-2 md:p-4 overflow-hidden border border-purple/10'})
        # Extract the names of the connectors
        page_connector_names = [connector.text.strip() for connector in connector_list]
        connector_names = connector_names + page_connector_names
    #print(connector_names)
    url = 'https://hub.meltano.com/loaders'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
        # Find all the connectors
    connector_list = soup.find_all('div', {'class': 'rounded-md text-slate-800 h-48 hover:bg-white bg-white-07 p-2 md:p-4 overflow-hidden border border-purple/10'})
    # Extract the names of the connectors
    loaders = [connector.text.strip() for connector in connector_list]
    connector_names = connector_names + loaders
    #print(connector_names)
    url = 'https://hub.meltano.com/utilities'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
        # Find all the connectors
    connector_list = soup.find_all('div', {'class': 'rounded-md text-slate-800 h-48 hover:bg-white bg-white-07 p-2 md:p-4 overflow-hidden border border-purple/10'})
    # Extract the names of the connectors
    loaders = [connector.text.strip() for connector in connector_list]
    connector_names = connector_names + loaders
    print(len(connector_names))
    return connector_names

get_connectors()