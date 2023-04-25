import requests
from bs4 import BeautifulSoup

def get_connectors():
    url = "https://help.salesforce.com/s/articleView?id=sf.ms_composer_reference.htm&type=5"
    return ['Asana', 'Box', 'Gmail', 'Google Calendar', 'Google Sheets', 'HTTP', 'HubSpot', 
            'Jira', 'Marketo', 'Microsoft Dynamics 365 Business Central', 'Microsoft Teams', 
            'NetSuite', 'QuickBooks Online', 'MuleSoft RPA', 'Sage Intacct', 'Salesforce', 
            'Salesforce Marketing Cloud', 'ServiceNow', 'Slack', 'Snowflake', 'Stripe', 'Tableau', 
            'Twilio', 'Workday', 'Xero', 'Zendesk', 'Zuora']