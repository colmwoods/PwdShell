import getpass
import os
import json
from cryptography.fernet import Fernet
import hashlib
from colorama import Fore, Style, init

init(autoreset=True)

SUCCESS = Fore.GREEN + Style.BRIGHT
ERROR = Fore.RED + Style.BRIGHT
RESET = Style.RESET_ALL


def clear():
    """
    Function to clear terminal through the game.
    """
    print("\033c")

class PwdShell:
    """ 
    Class to manage user sessions for Heroku deployment.
    """
    user_sessions = {}


def startup_message():
    """
    Display the startup message.
    """
    if "DYNO" in os.environ:  # Check if running on Heroku
        print("🔐 Welcome to PwdShell - Your Secure Password Manager 🔐")
        print("---------------------------------------------------------")
        print("⚠️  Important Notice (Deployed Version)")
        print("This is a demo environment. Data is NOT saved permanently.")
        print()
        print("• You must set a master password each time you visit.")
        print("• Passwords and vault data are cleared when the page is closed or refreshed.")
        print("• No 'master.key' or 'vault.json' file is stored in this deployment.")
        print()
        print("👉 Want to use PwdShell locally with full features?")
        print("   Clone the project here: https://github.com/colmwoods/PwdShell")
        print("---------------------------------------------------------")
    else:
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
    if running_on_heroku:
        if user_id in PwdShell.user_sessions:
            return PwdShell.user_sessions[user_id]
        while True:
            master_password = getpass.getpass("Set your master password: ")
            confirm_password = getpass.getpass(
                "Confirm your master password: ")

            if master_password != confirm_password:
                print(ERROR + "Passwords do not match. Please try again." + RESET)
            elif not master_password.strip():
                print(ERROR + "Master password cannot be empty. Please try again." + RESET)
            else:
                PwdShell.user_sessions[user_id] = master_password
                print(SUCCESS + "Master password set successfully." + RESET)
                return master_password
    else:
        if os.path.exists("master.key"):
            with open("master.key", "r") as file:
                return file.read().strip()

        while True:
            master_password = getpass.getpass("Set your master password: ")
            confirm_password = getpass.getpass(
                "Confirm your master password: ")

            if master_password != confirm_password:
                print(ERROR + "Passwords do not match. Please try again." + RESET)

            elif not master_password.strip():
                print(ERROR + "Master password cannot be empty. Please try again." + RESET)

            else:
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

    if running_on_heroku:
        # Heroku session-only check
        if user_id not in PwdShell.user_sessions:
            set_master_password(user_id)

        attempt = getpass.getpass("Enter master password: ").strip()
        if attempt == PwdShell.user_sessions[user_id]:
            print("🔓 Access granted.")
            return True
        else:
            print(ERROR + "Incorrect master password. Exiting." + RESET)
            return False

    else:
        if not os.path.exists("master.key"):
            set_master_password(user_id)

        with open("master.key", "r") as f:
            stored_hash = f.read().strip()

        attempt = getpass.getpass("Enter master password: ").strip()
        attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()

        if attempt_hash == stored_hash:
            print("🔓 Access granted.")
            return True
        else:
            print(ERROR + "Incorrect master password. Exiting." + RESET)
            return False


def load_key():
    """
    Load the encryption key from file, or generate a new one.
    """
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key


def load_vault():
    """
    Load the password vault from a JSON file.
    """
    if os.path.exists("vault.json"):
        try:
            with open("vault.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}


def save_vault(vault):
    """
    Save the password vault to a JSON file.
    """
    with open("vault.json", "w") as file:
        json.dump(vault, file)


def add_new_password(vault):
    """
    Add a new password to the vault.
    """
    account = input(
        "Enter the account you will be adding, e.g. google, twitter etc: "
    ).strip().lower()
    clear()

    if not account:
        print(ERROR + "Account name cannot be blank." + RESET)
        return

    if account in vault:
        print(ERROR + f"{account} already exists." + RESET)
        return

    username = input(
        f"Enter the username for your {account} account: "
    ).strip()
    clear()

    password = getpass.getpass(
        f"Enter the password for your {account} account: "
    ).strip()

    if not username or not password:
        print(ERROR + "Username and password cannot be blank." + RESET)
        return

    vault[account] = {"username": username, "password": password}
    print(SUCCESS+ f"{account} added successfully." + RESET)



def get_password(vault):
    """
    Retrieve a password from the vault.
    """
    account = input(
        "Enter the account you want to retrieve the password for: "
        ).strip().lower()
    clear()
    if account in vault:
        print(f"Username for your {account}: {vault[account]['username']}")
        print(f"Password for your {account}: {vault[account]['password']}")
    else:
        print(ERROR + f"No account found for {account}." + RESET)


def view_accounts(vault):
    """
    View all stored accounts in the vault.
    """
    if vault:
        print("🔑 Stored Accounts:")
        for account in vault:
            print(f"- {account}")
    else:
        print(ERROR + "No accounts stored yet." + RESET)


def delete_account(vault):
    """
    Delete an account from the vault.
    """
    account = input("Enter the account you want to delete: ").strip().lower()
    clear()
    if account in vault:
        del vault[account]
        save_vault(vault)
        print(SUCCESS + f"{account} deleted successfully." + RESET)
    else:
        print(ERROR + f"No account found for {account}." + RESET)


def main():
    """
    Main function to run the password manager.
    """
    set_master_password()

    if not master_password():
        return

    vault = load_vault()

    while True:
        # Menu Options
        print("\nOptions:")
        print("1. Add New Password")
        print("2. Get Password")
        print("3. View All Accounts")
        print("4. Delete An Account")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        clear()

        if choice == '1':
            add_new_password(vault)
            save_vault(vault)

        elif choice == '2':
            get_password(vault)

        elif choice == '3':
            view_accounts(vault)

        elif choice == '4':
            delete_account(vault)

        elif choice == '5':
            print("Exiting PwdShell. Stay secure!")
            break

        else:
            print(ERROR + f"User typed {choice} Invalid choice. Please select a valid option." + RESET)


if __name__ == "__main__":
    clear()
    startup_message()
    try:
        main()
    except KeyboardInterrupt:
        print(ERROR + "\nProgram interrupted by user. Exiting safely..." + RESET)
