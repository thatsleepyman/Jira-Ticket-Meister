from jira import JIRA
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import os


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

# Decrypt credentials
if JIRA_SERVER and JIRA_USERNAME and JIRA_API_TOKEN:
    JIRA_SERVER = cipher_suite.decrypt(JIRA_SERVER.encode('utf-8')).decode('utf-8')
    JIRA_USERNAME = cipher_suite.decrypt(JIRA_USERNAME.encode('utf-8')).decode('utf-8')
    JIRA_API_TOKEN = cipher_suite.decrypt(JIRA_API_TOKEN.encode('utf-8')).decode('utf-8')
else:
    print("Decryption failed...")


# Specify Jira connection parameters
jira_conn = JIRA(options={'server': JIRA_SERVER}, basic_auth=(JIRA_USERNAME, JIRA_API_TOKEN))

# Get an existing issue
issue = jira_conn.issue('ISSUE_KEY') # Add your issue key here

# Print all fields
print(issue.fields())