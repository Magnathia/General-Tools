# AD Automation

This project contains scripts to automate Active Directory (AD) user management tasks using Python and PowerShell.

## Files

- `AD_functions.py`: Contains Python functions for various AD user management tasks.
- `launch.ps1`: PowerShell script to set up the environment and run functions from `AD_functions.py`.

## Functions in `AD_functions.py`

1. **get_highest_uidNumber(users)**:
    - Finds the highest `uidNumber` attribute from a list of users.
    - Args: `users` (list): List of user dictionaries with 'uidNumber' attribute.
    - Returns: `int`: The highest `uidNumber` found.

2. **get_users_with_blank_uidNumber(users)**:
    - Finds users with a blank `uidNumber` attribute.
    - Args: `users` (list): List of user dictionaries with 'uidNumber' and 'username' attributes.
    - Returns: `list`: List of usernames with a blank `uidNumber`.

3. **create_ad_user()**:
    - Prompts for user details and creates a new AD user.
    - Prompts for: User First name, User Last name, User Logon Name, User Email, User Department.
    - Returns: `dict`: A dictionary representing the new AD user.

4. **add_user_to_ad(user_details)**:
    - Creates a new user in Active Directory.
    - Args: `user_details` (dict): A dictionary containing user details.
    - Returns: `bool`: True if user creation was successful, False otherwise.

## Instructions

1. **Ensure Python is installed**:
    - The `launch.ps1` script checks if Python is installed and installs it if not.

2. **Set up the virtual environment**:
    - The `launch.ps1` script sets up a virtual environment for the project.

3. **Run the PowerShell script**:
    - Open PowerShell and navigate to the project directory.
    - Run the script: `.\launch.ps1`
    - Follow the prompts to select and run a function from `AD_functions.py`.

4. **Select a function to run**:
    - The script will prompt you to select one of the following functions to run:
        1. `get_highest_uidNumber`
        2. `get_users_with_blank_uidNumber`
        3. `create_ad_user`
        4. `add_user_to_ad`

5. **Deactivate the virtual environment**:
    - The script will automatically deactivate the virtual environment after execution.

## Example Usage

```powershell
# Navigate to the project directory
cd "C:\Users\rsmith\Desktop\AD Automation"

# Run the PowerShell script
.\launch.ps1