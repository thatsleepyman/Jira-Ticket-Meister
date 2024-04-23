from datetime import datetime
from jira_ticket_meister import create_jira_ticket


def main():
    
    # Get the current timestamp
    timestamp = datetime.now()

    # Variables to create the Jira ticket
    jira_project_key = 'DEVOPS'
    Jira_priority = 'PRIO 3'
    jira_summary = f'Just a summary created at {timestamp}'
    jira_description = 'Beautiful description :)'
    jira_issuetype = '[System] Incident'
    jira_team = 'Team DevOps'

    # Pass the variables to the function, and create the Jira ticket
    try:
        create_jira_ticket(jira_project_key, Jira_priority, jira_issuetype, jira_team, jira_summary, jira_description)
    except Exception as e:
        print(f'Error creating Jira ticket: {e}')


if __name__ == "__main__":
    main()