import requests
from bs4 import BeautifulSoup


def get_connectors():
    url = "https://docs.databricks.com/data/data-sources/index.html#data-sources"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Find all connector names within <span> tags with class "doc"
    connector_names = [span.text for span in soup.find_all("span", class_="doc")]
    return ['Python', 'Scala', 'Delta Lake', 'Delta Sharing', 'Parquet', 'ORC', 'JSON', 'CSV', 'Avro', 'JDBC', 'PostgreSQL', 
            'MySQL', 'MariaDB', 'SQL Server', 'Amazon Redshift', 
            'Google BigQuery', 'MongoDB', 'Cassandra', 'Couchbase', 'ElasticSearch', 'Snowflake', 'Azure Cosmos DB', 'Azure Synapse Analytics', 
            'LZO']

