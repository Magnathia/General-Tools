# ...existing code...

import subprocess

def get_highest_uidNumber():
    """
    Function to find the highest uidNumber attribute below 3500 from Active Directory users.
    
    Returns:
        int: The highest uidNumber found below 3500.
    """
    try:
        # PowerShell command to import the Active Directory module and get all users and their uidNumber
        command = (
            "if (-not (Get-Module -ListAvailable -Name ActiveDirectory)) { "
            "Install-WindowsFeature RSAT-AD-PowerShell; "
            "Import-Module ActiveDirectory; "
            "} "
            "Get-ADUser -Filter * -Property uidNumber | "
            "Where-Object { $_.uidNumber -ne $null -and $_.uidNumber -lt 3500 } | "
            "Select-Object -ExpandProperty uidNumber"
        )
        
        # Execute the PowerShell command and capture the output
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Failed to retrieve uidNumbers: {result.stderr}")
            return -1
        
        uid_numbers = [int(uid) for uid in result.stdout.split() if uid.isdigit()]
        
        if uid_numbers:
            return max(uid_numbers)
        else:
            return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

def get_users_with_blank_uidNumber(users):
    """
    Function to find users with a blank uidNumber attribute.
    
    Args:
        users (list): List of user dictionaries with 'uidNumber' and 'username' attributes.
        
    Returns:
        list: List of usernames with a blank uidNumber.
    """
    users_with_blank_uid = []
    for user in users:
        if 'uidNumber' not in user or user['uidNumber'] == '':
            users_with_blank_uid.append(user['username'])
    return users_with_blank_uid

def create_ad_user():
    """
    Function to prompt for user details and create a new AD user.
    
    Prompts for:
        - User First name
        - User Last name
        - User Logon Name
        - User Email
        - User Department
        
    Returns:
        dict: A dictionary representing the new AD user.
    """
    first_name = input("Enter user's first name: ")
    last_name = input("Enter user's last name: ")
    logon_name = input("Enter user's logon name: ")
    email = input("Enter user's email: ")
    department = input("Enter user's department: ")
    
    new_user = {
        'first_name': first_name,
        'last_name': last_name,
        'logon_name': logon_name,
        'email': email,
        'department': department
    }
    
    # Here you would add the code to actually create the user in AD.
    # This is a placeholder for the AD creation logic.
    print(f"Creating user: {new_user}")
    add_user_to_ad(new_user)
    
    return new_user

def add_user_to_ad(user_details):
    """
    Function to create a new user in Active Directory.
    
    Args:
        user_details (dict): A dictionary containing user details.
        
    Returns:
        bool: True if user creation was successful, False otherwise.
    """
    try:
        # Construct the PowerShell command to create a new AD user
        command = [
            "New-ADUser",
            "-Name", f"{user_details['first_name']} {user_details['last_name']}",
            "-GivenName", user_details['first_name'],
            "-Surname", user_details['last_name'],
            "-SamAccountName", user_details['logon_name'],
            "-UserPrincipalName", f"{user_details['logon_name']}@yourdomain.com",
            "-EmailAddress", user_details['email'],
            "-Department", user_details['department'],
            "-AccountPassword", "(ConvertTo-SecureString 'P@ssw0rd' -AsPlainText -Force)",
            "-Enabled", "True"
        ]
        
        # Execute the PowerShell command
        subprocess.run(["powershell", "-Command"] + command, check=True)
        print(f"User {user_details['logon_name']} created successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to create user: {e}")
        return False

# ...existing code...
