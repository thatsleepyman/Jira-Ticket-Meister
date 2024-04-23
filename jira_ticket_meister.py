def create_jira_ticket(jira_project_key, Jira_priority, jira_issuetype, jira_team, jira_summary, jira_description):
# To use this function, pass the required Jira fields to this function.
# For example;
    # jira_project_key = 'DEVOPS'
    # Jira_priority = 'Prioriteit 3'
    # jira_summary = 'Just a summary'
    # jira_description = 'Beautiful description :)'
    # jira_issuetype = '[System] Incident'
    # jira_team = 'Team DevOps'


    ##########################
    # IMPORT NECESSARY MODULES
    ##########################
    from jira import JIRA
    from dotenv import load_dotenv
    from cryptography.fernet import Fernet
    import os


    #######################
    # READ .ENV CREDENTIALS
    #######################
    # Load environment variables from .env file
    load_dotenv()
    # Get the encryption key from the environment
    encryption_key = os.getenv('ENCRYPTION_KEY')
    # Convert the base64-encoded string to bytes
    key = encryption_key.encode('utf-8')
    cipher_suite = Fernet(key)
    # Access the variables
    JIRA_SERVER = os.getenv('JIRA_SERVER')
    JIRA_USERNAME = os.getenv('JIRA_USERNAME')
    JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN')


    ##########################
    # DECRYPT .ENV CREDENTIALS
    ##########################
    # Decrypt credentials
    if JIRA_SERVER and JIRA_USERNAME and JIRA_API_TOKEN:
        JIRA_SERVER = cipher_suite.decrypt(JIRA_SERVER.encode('utf-8')).decode('utf-8')
        JIRA_USERNAME = cipher_suite.decrypt(JIRA_USERNAME.encode('utf-8')).decode('utf-8')
        JIRA_API_TOKEN = cipher_suite.decrypt(JIRA_API_TOKEN.encode('utf-8')).decode('utf-8')
    else:
        print("Decryption failed...")


    ####################################
    # SPECIFY JIRA CONNECTION PARAMETERS
    ####################################
    # Specify Jira endpoint
    jira_endpoint = {'server': JIRA_SERVER}
    # Define Jira connection parameters
    jira_conn = JIRA(options=jira_endpoint, basic_auth=(JIRA_USERNAME, JIRA_API_TOKEN))

    # Define the fields for creating the Jira ticket
    fields = {
        'project': {'key': jira_project_key},
        'priority': {'name': Jira_priority},
        'issuetype': {'name': jira_issuetype},
        'reporter': {'id': JIRA_USERNAME},
        'customfield_10129': {'value': jira_team},
        'summary': jira_summary,
        'description': jira_description,
    } # You can find your Jira Fields by using the Jira Fields script in this repository


    ####################
    # CREATE JIRA TICKET
    ####################
    # Check if description is provided before creating the Jira ticket
    if jira_description.strip():
        # Create the Jira ticket
        created_issue = jira_conn.create_issue(fields=fields)
        # Print details of the created issue
        print(f'Created issue {created_issue.key} - {created_issue.fields.summary}')
    else:
        print("Description is empty. Skipping ticket creation.")


    #######################
    # CLOSE JIRA CONNECTION
    #######################
    jira_conn.close()