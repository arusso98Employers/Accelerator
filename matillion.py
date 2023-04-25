def get_connectors():
    #url = 'https://www.matillion.com/technology/integrations/#pricingTabs'
    #page = requests.get(url)
    #soup = BeautifulSoup(page.content, 'html.parser')
    #titles = [title.text for title in soup.find_all('span', class_='title')]
    titles = ['Amazon Aurora', 'Amazon Aurora (Unload)', 'Amazon DynamoDB', 
              'Amazon RDS', 'Amazon S3', 'Amazon S3 (Unload)', 'Amplitude', 'AOL Email', 
              'Apache Hive', 'Apache Spark', 'Azure Blob Storage', 
              'Azure Blob Storage (Unload)', 'Azure Cosmos DB', 'Azure SQL', 'Box', 
              'Dropbox', 'Dynamics', 'Dynamics 365 Sales', 'Dynamics CRM', 'Dynamics NAV', 
              'ElasticSearch', 'Email', 'Facebook', 'FTP', 'Gmail', 'Google Analytics', 
              'Google BigQuery', 'Google Cloud Storage', 'Google Custom Search', 
              'Google Sheets', 'HDFS', 'HTTP', 'HTTPS', 'HubSpot', 'IBM DB2', 
              'IBM DB2 for i', 'Instagram', 'Intercom', 'JIRA', 'LDAP', 'LinkedIn', 
              'LinkedIn Ads', 'Mailchimp', 'Mandrill', 'MariaDB', 'MariaDB (Unload)', 
              'Marketo', 'Microsoft Azure SQL (Output)', 'Microsoft Excel', 
              'Microsoft SharePoint', 'Microsoft SQL Server', 'MindSphere', 'Mixpanel', 
              'MongoDB', 'MySQL', 'MySQL (Unload)', 'Netezza', 'NetSuite', 'OData', 
              'Open Exchange Rates', 'Oracle', 'Oracle Eloqua', 'Outlook Email', 'Pardot', 
              'PayPal', 'PostGreSQL', 'PostgreSQL (Unload)', 'QuickBooks', 'Recurly', 
              'Redis', 'REST API', 'Sage Intacct', 'Salesforce', 'Salesforce (Output)', 
              'Salesforce Marketing Cloud', 'SAP', 'SAP Hana', 'SAP NetWeaver', 'SendGrid',
              'ServiceNow', 'SFTP', 'Shopify', 'Snapchat', 'Splunk', 'Square', 'Stripe', 
              'Sugar CRM', 'SurveyMonkey', 'Sybase ASE', 'Teradata', 'Twilio', 'Twitter', 
              'Twitter Ads', 'Webhook', 'Windows Fileshare', 'Xero', 'Yahoo Email', 
              'YouTube', 'YouTube Analytics', 'Zendesk', 'Zoho', 'Zoho Email']
    return titles