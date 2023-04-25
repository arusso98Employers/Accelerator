import requests
from bs4 import BeautifulSoup

def get_connectors():
    url = "https://airflow.apache.org/docs/apache-airflow-providers/core-extensions/connections.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    connector_table = soup.find_all('ul')[70]
    names = []
    for a in connector_table.find_all('a'):
        names.append(a.text)
    return names