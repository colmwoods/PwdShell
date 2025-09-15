import getpass
import os
import json

def load_vault():
    """
    Load the password vault from a JSON file.
    """
    if os.path.exists("vault.json"):
        with open("vault.json", "r") as file:
            return json.load(file)
    return {}


def add_new_password(vault, account, username, password):
    """
    Add a new password to the vault.
    """
    account = input("Enter the account you will be adding, e.g. google, twitter etc: ").strip()
    username = input(f"Enter the username for your {account} account: ").strip()
    password = getpass.getpass(f"Enter the password for your{account} account: ").strip()

    if account in vault:
        print(f"❌ {account} already exists.")

    else:
        vault[account] = {"username": username, "password": password}
        print(f"✅ {account} added successfully.")



def get_password(username, password, vault, account):
    """
    Retrieve a password from the vault.
    """
    account = input("Enter the account you want to retrieve the password for: ").strip()
    if account in vault:
        print(f"Username for your {account}: {username}")
        print(f"Password for your {account}: {password}")

    else:
        print(f"❌ No account found for {account}.")




def view_accounts(vault, account):
    """
    View all stored accounts in the vault.
    """
    if vault:
        print("🔑 Stored Accounts:")
        for account in vault:
            print(f"- {account}")
    else:
        print("❌ No accounts stored yet.")



def delete_account(vault, account):
    """
    Delete an account from the vault.
    """
    account = input("Enter the account you want to delete: ").strip()
    if account in vault:
        del vault[account]
        print(f"✅ {account} deleted successfully.")
    else:
        print(f"❌ No account found for {account}.")



def main(vault, account, username, password):
    """
    Main function to run the password manager.
    """

    print("🔐 Welcome to PwdShell")
    master = getpass.getpass("Enter master password: ")

    if not master.strip():
        print("❌ Invalid master password.")
        return


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
            add_new_password(vault, account, username, password)

        elif choice == '2':
            get_password(username, password, vault, account)

        elif choice == '3':
            view_accounts(vault, account)

        elif choice == '4':
            delete_account(vault, account)

        elif choice == '5':
            print("Exiting PwdShell. Stay secure!")
            break

        else:
            print("❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main(vault={}, account="", username="", password="")