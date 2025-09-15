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

def add_new_password():






def get_password():




def view_accounts():



def delete_account():


