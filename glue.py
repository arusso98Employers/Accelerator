import requests
from bs4 import BeautifulSoup

def get_connectors():
    url = "https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    connectors = soup.find_all('td')
    pattern = '>(.*)<'
    final_list = []
    for i in connectors:
        # Search for the pattern in the text using regex and return the match object
        #match = re.findall(pattern, str(i))
        final_list.append(i.text)
        # If a match is found, print the matched pattern
        #res = [*set(match)]
        #if res != []:
            #final_list.append(res[0])

    return ['Spark', 'Athena', 'JDBC', 'DocumentDB',  'DynamoDB', 'Kafka', 'Kinesis', 'MongoDB', 'MySQL', 'Oracle', 'Amazon S3',
             'Apache Hive', 'Parquet',  'PostgreSQL', 'Amazon Redshift', 'Microsoft SQL Server']
