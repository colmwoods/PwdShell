import getpass
import os
import json

def main():

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

def add_new_password(vault, account, username, password):
    account = input("Enter the account you will be adding, e.g. google, twitter etc: ").strip()
    username = input(f"Enter the username for your {account} account: ").strip()
    password = getpass.getpass(f"Enter the password for your{account} account: ").strip()

    if account in vault:
        print(f"❌ {account} already exists.")

    else:
        vault[account] = {"username": username, "password": password}
        print(f"✅ {account} added successfully.")



def get_password(username, password, vault, account):
    account = input("Enter the account you want to retrieve the password for: ").strip()
    if account in vault:
        print(f"Username for your {account}: {username}")
        print(f"Password for your {account}: {password}")

    else:
        print(f"❌ No account found for {account}.")




def view_accounts(vault, account):
    if vault:
        print("🔑 Stored Accounts:")
        for account in vault:
            print(f"- {account}")
    else:
        print("❌ No accounts stored yet.")



def delete_account(vault, account):
    account = input("Enter the account you want to delete: ").strip()
    if account in vault:
        del vault[account]
        print(f"✅ {account} deleted successfully.")
    else:
        print(f"❌ No account found for {account}.")



