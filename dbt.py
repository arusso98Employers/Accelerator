import requests
from bs4 import BeautifulSoup

def get_connectors():
    import re
    url = 'https://docs.getdbt.com/docs/supported-data-platforms'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    connectors = soup.find_all('td')
    names = []
    for i in connectors:
        names.append(i.text)
    return ['AlloyDB', 'Azure Synapse', 'BigQuery','Databricks',  'Dremio', 'Postgres',  'Redshift', 'Snowflake', 'Spark', 'Starburst & Trino',  'Athena',
             'Greenplum', 'Oracle', 'Clickhouse', 'Hive', 'Rockset', 'IBM DB2', 'Impala', 'SingleStore', 'Doris & SelectDB', 'Infer', 'SQLite', 'DuckDB', 
             'iomete', 'SQL Server',  'Layer', 'Teradata', 'Exasol Analytics', 'Materialize', 'TiDB', 'Firebolt', 'MindsDB', 'Vertica', 'AWS Glue', 'MySQL', 
               'Databend Cloud']