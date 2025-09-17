import getpass
import os
import json
from cryptography.fernet import Fernet
import hashlib

user_sessions = {}

def set_master_password(user_id="default_user"):
    """
    Prompt the user to set a master password and return its hash.
    """
    running_on_heroku = "DYNO" in os.environ
    if running_on_heroku:
        if user_id in user_sessions:
            return user_sessions[user_id]

        while True:
            master_password = getpass.getpass("Set your master password: ")
            confirm_password = getpass.getpass("Confirm your master password: ")

            if master_password != confirm_password:
                print("❌ Passwords do not match. Please try again.")
            elif not master_password.strip():
                print("❌ Master password cannot be empty. Please try again.")
            else:
                user_sessions[user_id] = master_password
                print("✅ Master password set successfully (Heroku session only).")
                return master_password
    else:
        if os.path.exists("master.key"):
            with open("master.key", "r") as file:
               return file.read().strip()
        
        
        while True:
            master_password = getpass.getpass("Set your master password: ")
            confirm_password = getpass.getpass("Confirm your master password: ")

            if master_password != confirm_password:
                print("❌ Passwords do not match. Please try again.")

            elif not master_password.strip():
                print("❌ Master password cannot be empty. Please try again.")
        
            else:
                hashed_password = hashlib.sha256(master_password.encode()).hexdigest()
                with open("master.key", "w") as file:
                    file.write(hashed_password)
                print("✅ Master password set successfully.")
                return hashed_password

def master_password():
    """
    Verify the master password entered by the user.
    """
    if not os.path.exists("master.key"):
        set_master_password()

    with open("master.key", "r") as f:
        stored_hash = f.read().strip()

    master = getpass.getpass("Enter master password: ").strip()
    hashed = hashlib.sha256(master.encode()).hexdigest()

    if hashed == stored_hash:
        print("🔓 Access granted.")
        return True
    else:
        print("❌ Incorrect master password. Exiting.")
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
    account = input("Enter the account you will be adding, e.g. google, twitter etc: ").strip().lower()
    username = input(f"Enter the username for your {account} account: ").strip()
    password = getpass.getpass(f"Enter the password for your {account} account: ").strip()

    if account in vault:
        print(f"❌ {account} already exists.")

    else:
        vault[account] = {"username": username, "password": password}
        print(f"✅ {account} added successfully.")



def get_password(vault):
    """
    Retrieve a password from the vault.
    """
    account = input("Enter the account you want to retrieve the password for: ").strip().lower()
    if account in vault:
        print(f"Username for your {account}: {vault[account]['username']}")
        print(f"Password for your {account}: {vault[account]['password']}")
    else:
        print(f"❌ No account found for {account}.")




def view_accounts(vault):
    """
    View all stored accounts in the vault.
    """
    if vault:
        print("🔑 Stored Accounts:")
        for account in vault:
            print(f"- {account}")
    else:
        print("❌ No accounts stored yet.")



def delete_account(vault):
    """
    Delete an account from the vault.
    """
    account = input("Enter the account you want to delete: ").strip().lower()
    if account in vault:
        del vault[account]
        save_vault(vault)
        print(f"✅ {account} deleted successfully.")
    else:
        print(f"❌ No account found for {account}.")



def main():
    """
    Main function to run the password manager.
    """
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
            print("❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n❌ Program interrupted by user. Exiting safely...")