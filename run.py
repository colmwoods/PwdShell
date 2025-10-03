import getpass
import os
import json
from cryptography.fernet import Fernet
import hashlib
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize Colorama

SUCCESS = Fore.GREEN + Style.BRIGHT  # Bright Green
ERROR = Fore.RED + Style.BRIGHT  # Bright Red
RESET = Style.RESET_ALL  # Reset to default


def clear():
    """
    Function to clear terminal through the game.
    """
    print("\033c")  # ANSI Escape Code To Clear Terminal


class PwdShell:
    """
    Class to manage user sessions for Heroku deployment.
    """
    user_sessions = {}  # Dictionary To Store User Sessions


def startup_message():
    """
    Display the startup message.
    """
    if "DYNO" in os.environ:  # Check If Running On Heroku
        print("🔐 Welcome to PwdShell - Your Secure Password Manager 🔐")
        print("---------------------------------------------------------")
        print("⚠️  Important Notice (Deployed Version)")
        print("This is a demo environment. Data is NOT saved permanently.")
        print()
        print("• You must set a master password each time you visit.")
        print(
            "• Passwords and vault data are cleared when the page "
            "is closed or refreshed."
        )
        print(
            "• No 'master.key' or 'vault.json' file is stored "
            "in this deployment."
        )
        print("👉 Want to use PwdShell locally with full features?")
        print(
            "   Clone the project here: "
            "https://github.com/colmwoods/PwdShell"
        )
        print("---------------------------------------------------------")
    else:  # If Running Locally
        print("🔐 Welcome to PwdShell - Your Secure Password Manager 🔐")
        print("---------------------------------------------------------")
        print("⚠️  Important Notice (Local Version)")
        print()
        print("Your master password will be saved locally in 'master.key")
        print("Your passwords will be saved locally in 'vault.json'")
        print("---------------------------------------------------------")


def set_master_password(user_id="default_user"):
    """
    Prompt the user to set a master password and return its hash.
    """
    running_on_heroku = "DYNO" in os.environ
    if running_on_heroku:  # Check If Running On Heroku
        if user_id in PwdShell.user_sessions:
            # Return Existing Session Password
            return PwdShell.user_sessions[user_id]
        while True:
            master_password = getpass.getpass(
                "Set your master password: ")  # Prompt For Password
            confirm_password = getpass.getpass(
                "Confirm your master password: ")

            if master_password != confirm_password:  # If Passwords Don't Match
                print(
                    ERROR +
                    "Passwords do not match. Please try again." +
                    RESET)
            elif not master_password.strip():  # If Password Is Empty
                print(
                    ERROR +
                    "Master password cannot be empty. Please try again." +
                    RESET)
            else:  # Valid Password
                PwdShell.user_sessions[user_id] = master_password
                print(SUCCESS + "Master password set successfully." + RESET)
                return master_password
    else:  # If Running Locally
        if os.path.exists("master.key"):  # Check If Master Key File Exists
            with open("master.key", "r") as file:  # Read Existing Master Key
                return file.read().strip()  # Return Existing Master Key

        while True:  # Prompt For New Master Password
            master_password = getpass.getpass(
                "Set your master password: ")  # Prompt For Password
            confirm_password = getpass.getpass(
                "Confirm your master password: ")

            if master_password != confirm_password:  # If Passwords Don't Match
                print(
                    ERROR +
                    "Passwords do not match. Please try again." +
                    RESET)

            elif not master_password.strip():  # If Password Is Empty
                print(
                    ERROR +
                    "Master password cannot be empty. Please try again." +
                    RESET)

            else:  # Valid Password
                hashed_password = hashlib.sha256(
                    master_password.encode()).hexdigest()
                with open("master.key", "w") as file:
                    file.write(hashed_password)
                print(SUCCESS + "Master password set successfully.")
                return hashed_password


def master_password(user_id="default_user"):
    """
    Verify the master password entered by the user.
    """
    running_on_heroku = "DYNO" in os.environ
    max_attempts = 3

    if running_on_heroku:  # Check If Running On Heroku
        if user_id not in PwdShell.user_sessions:  # If No Session Exists
            set_master_password(user_id)  # Prompt To Set Master Password

        for attempt_num in range(max_attempts): # Allow Limited Attempts
            attempt = getpass.getpass("Enter master password: ").strip()
            if attempt == PwdShell.user_sessions[user_id]:  # Verify Password
                print("🔓 Access granted.")
                return True
            else: # Incorrect Password
                remaining = max_attempts - (attempt_num + 1) # Remaining Attempts
                if remaining > 0: # If Can Retry
                    print(ERROR + f"Incorrect. {remaining} attempts left." + RESET)
                else: # No More Attempts
                    print(ERROR + "Too many failed attempts. Exiting." + RESET)
                    return False
            

    else: # If Running Locally
        if not os.path.exists("master.key"):  # If No Master Key File Exists
            set_master_password(user_id)  # Prompt To Set Master Password

        with open("master.key", "r") as f:  # Read Stored Master Key
            stored_hash = f.read().strip()  # Get Stored Hash
        
        for attempt_num in range(max_attempts): # Allow Limited Attempts
            attempt = getpass.getpass(
                "Enter master password: ").strip()  # Prompt For Password
            attempt_hash = hashlib.sha256(
                attempt.encode()).hexdigest()  # Hash Attempt

            if attempt_hash == stored_hash:  # Verify Password
                print("🔓 Access granted.")
                return True
        
            remaining = max_attempts - (attempt_num + 1) # Remaining Attempts
            if remaining > 0: # If Can Retry
                print(ERROR + f"Incorrect. {remaining} attempts left." + RESET)
            else: # No More Attempts
                print(ERROR + "Too many failed attempts. Exiting." + RESET)
                return False

def load_key():
    """
    Load the encryption key from file, or generate a new one.
    """
    if not os.path.exists("key.key"):  # If No Key File Exists
        key = Fernet.generate_key()  # Generate New Key
        with open("key.key", "wb") as key_file:  # Save New Key To File
            key_file.write(key)
    else:  # If Key File Exists
        with open("key.key", "rb") as key_file:  # Read Existing Key
            key = key_file.read()  # Load Key From File
    return key


def load_vault():
    """
    Load the password vault from a JSON file.
    """
    if os.path.exists("vault.json"):  # If Vault File Exists
        try:
            with open("vault.json", "r") as file:  # Read Vault File
                return json.load(file)  # Load Vault Data
        except json.JSONDecodeError:  # If File Is Corrupted
            print(
                ERROR +
                "Vault file is corrupted. Starting with an empty vault." +
                RESET)
            return {}  # Return Empty Vault
    return {}


def save_vault(vault):
    """
    Save the password vault to a JSON file.
    """
    with open("vault.json", "w") as file:  # Write Vault File
        json.dump(vault, file)  # Save Vault Data


def add_new_password(vault):
    """
    Add a new password to the vault.
    """
    account = input(
        "Enter the account you will be adding, e.g. google, twitter etc: "
    ).strip().lower()
    clear()

    if not account:  # If Account Name Is Empty
        print(ERROR + "Account name cannot be blank." + RESET)
        return

    if account in vault:  # If Account Already Exists
        print(ERROR + f"{account} already exists." + RESET)
        return

    username = input(
        f"Enter the username for your {account} account: "
    ).strip()
    clear()

    password = getpass.getpass(
        f"Enter the password for your {account} account: "
    ).strip()

    if not username or not password:  # If Username Or Password Is Empty
        print(ERROR + "Username and password cannot be blank." + RESET)
        return

    vault[account] = {
        "username": username,
        "password": password}  # Add To Vault
    print(SUCCESS + f"{account} added successfully." + RESET)


def get_password(vault):
    """
    Retrieve a password from the vault.
    """
    account = input(
        "Enter the account you want to retrieve the password for: "
    ).strip().lower()
    clear()
    if account in vault:  # If Account Exists
        print(f"Username for your {account}: {vault[account]['username']}")
        print(f"Password for your {account}: {vault[account]['password']}")
    else:  # If Account Does Not Exist
        print(ERROR + f"No account found for {account}." + RESET)


def view_accounts(vault):
    """
    View all stored accounts in the vault.
    """
    if vault:  # If Vault Is Not Empty
        print("🔑 Stored Accounts:")
        for account in vault:  # List All Accounts
            print(f"- {account}")
    else:  # If Vault Is Empty
        print(ERROR + "No accounts stored yet." + RESET)


def delete_account(vault):
    """
    Delete an account from the vault.
    """
    account = input("Enter the account you want to delete: ").strip().lower()
    clear()
    if account in vault:  # If Account Exists
        del vault[account]  # Delete Account
        save_vault(vault)  # Save Updated Vault
        print(SUCCESS + f"{account} deleted successfully." + RESET)
    else:  # If Account Does Not Exist
        print(
            ERROR + f"No account found for {account}." + RESET
        )


def main():
    """
    Main function to run the password manager.
    """
    set_master_password()  # Ensure Master Password Is Set

    if not master_password():  # Verify Master Password
        return  # Exit If Verification Fails

    vault = load_vault()  # Load Existing Vault

    while True:
        # Menu Options
        print("\nOptions:")
        print("1. Add New Password")
        print("2. Get Password")
        print("3. View All Accounts")
        print("4. Delete An Account")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()  # Get User Choice
        clear()

        if choice == '1':  # Add New Password
            add_new_password(vault)
            save_vault(vault)

        elif choice == '2':  # Get Password
            get_password(vault)

        elif choice == '3':  # View All Accounts
            view_accounts(vault)

        elif choice == '4':  # Delete An Account
            delete_account(vault)

        elif choice == '5':  # Exit
            print("Exiting PwdShell. Stay secure!")
            break

        else:  # Invalid Choice
            print(
                ERROR
                + f"User typed {choice} Invalid choice. "
                "Please select a valid option."
                + RESET
            )


if __name__ == "__main__":
    clear()  # Clear Terminal On Start
    startup_message()  # Display Startup Message
    try:  # Run Main Program
        main()
    except KeyboardInterrupt:  # Handle Ctrl+C Gracefully
        print(
            ERROR
            + "\nProgram interrupted by user. "
            "Exiting safely..."
            + RESET
        )
