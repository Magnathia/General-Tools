# AD Automation

This project contains scripts to automate Active Directory (AD) user management tasks using Python and PowerShell.

## Files

- `AD_functions.py`: Contains Python functions for various AD user management tasks.
- `launch.ps1`: PowerShell script to set up the environment, update the repository, and run functions from `AD_functions.py`.
- `variables.py`: Contains environment-specific information such as Domain and OUs.

## Functions in `AD_functions.py`

1. **get_highest_uidNumber()**:
    - Finds the highest `uidNumber` attribute below 3500 from Active Directory users.
    - Returns: `int`: The highest `uidNumber` found below 3500.

2. **get_users_with_blank_uidNumber()**:
    - Finds users with a blank `uidNumber` attribute from the "PMEL Users" OU, excluding the "SysAdmin" and "Supplementary" OUs.
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

1. **Clone the repository**:
    - Open a terminal or PowerShell window.
    - Navigate to the directory where you want to clone the repository.
    - Run the command: `git clone https://github.com/Magnathia/General-Tools.git`

2. **Ensure Python is installed**:
    - The `launch.ps1` script checks if Python is installed and installs it if not.

3. **Set up the virtual environment**:
    - The `launch.ps1` script sets up a virtual environment for the project.

4. **Run the PowerShell script**:
    - Open PowerShell and navigate to the project directory.
    - Run the script: `.\launch.ps1`
    - The script will update the repository and prompt you to select and run a function from `AD_functions.py`.

5. **Select a function to run**:
    - The script will prompt you to select one of the following functions to run:
        1. `get_highest_uidNumber`
        2. `get_users_with_blank_uidNumber`
        3. `create_ad_user`
        4. `add_user_to_ad`

6. **Deactivate the virtual environment**:
    - The script will automatically deactivate the virtual environment after execution.

## Example Usage

```powershell
# Navigate to the project directory
cd "C:\Users\Desktop\AD Automation"

# Run the PowerShell script
.\launch.ps1