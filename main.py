
import snowflake.connector
#from meltano import get_connectors

####################################################################################################################
# Instructions:
# 1) Add new python file with the name of the integration service and add the function get_connectors() to that file
# 3) import the function like so: from file_name import get_connectors
# 4) Make sure you fill out your credentials below

# Set up connection parameters 
account = 'strivepartner.east-us-2.azure'
user = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
database = 'ACCELERATOR'
schema = 'PUBLIC'
warehouse = 'adf_demo_wh'
role = 'sysadmin'

# Create connection object 
conn = snowflake.connector.connect(
    account=account,
    user=user,
    password=password,
    database=database,
    schema=schema,
    warehouse=warehouse,
    role=role
)

def add_new_connectors_and_map(lst, integrationid):
    # Create a cursor to execute queries
    cur = conn.cursor()
    for i in lst: 
    # Execute the procedure with the input parameter
        cur.callproc('add_connector_if_not_exists', [i])
    # Commit the transaction
        conn.commit()
    # Close the cursor and connection
    cur.close()
    
    cursor = conn.cursor()
    for i in lst:
        # Query the connectors table for the connectorid corresponding to the connectorname
        cursor = conn.cursor()
        query = f"SELECT connectorid FROM connector WHERE UPPER(connectorname) = UPPER('{i}')"
        cursor.execute(query)
        result = cursor.fetchone()
        connectorid = result[0]
        query = f"INSERT INTO IntegrationTool_Connector_Map (integrationtoolID, connectorid) VALUES ('{integrationid}', '{connectorid}')"
        cursor.execute(query)
        conn.commit()
    conn.close()


def add_new_security_features_and_map(lst, integrationid):
    # Create a cursor to execute queries
    cur = conn.cursor()
    for i in lst: 
    # Execute the procedure with the input parameter
        cur.callproc('add_security_if_not_exists', [i])
    # Commit the transaction
        conn.commit()
    # Close the cursor and connection
    cur.close()
    cursor = conn.cursor()
    for i in lst:
        # Query the connectors table for the connectorid corresponding to the connectorname
        cursor = conn.cursor()
        query = f"SELECT securityfeatureid FROM securityfeatures WHERE UPPER(securityfeaturename) = UPPER('{i}')"
        cursor.execute(query)
        result = cursor.fetchone()
        securityid = result[0]
        query = f"INSERT INTO IntegrationTool_security_feature_Map (integrationtoolID, securityfeatureid) VALUES ('{integrationid}', '{securityid}')"
        cursor.execute(query)
        conn.commit()
    conn.close()


def add_new_support_features_and_map(lst, integrationid):
    # Create a cursor to execute queries
    cur = conn.cursor()
    for i in lst: 
    # Execute the procedure with the input parameter
        cur.callproc('add_support_if_not_exists', [i])
    # Commit the transaction
        conn.commit()
    # Close the cursor and connection
    cur.close()
    cursor = conn.cursor()
    for i in lst:
        # Query the connectors table for the connectorid corresponding to the connectorname
        cursor = conn.cursor()
        query = f"SELECT supportfeatureid FROM supportfeatures WHERE UPPER(supportfeaturename) = UPPER('{i}')"
        cursor.execute(query)
        result = cursor.fetchone()
        supportid = result[0]
        query = f"INSERT INTO IntegrationTool_support_feature_Map (integrationtoolID, supportfeatureid) VALUES ('{integrationid}', '{supportid}')"
        cursor.execute(query)
        conn.commit()
    conn.close()


# 5) Fill out remaining code


connectors = [] #get_connectors() # replace [] with get_connectors()
intregrationid = #28 # replace integrationid with the intregationtoolid found in the snowflake table
add_new_connectors_and_map(connectors, intregrationid)