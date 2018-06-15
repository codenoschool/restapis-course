import requests
import os

host = "https://api.jsonbin.io/b/"

"""
This app will ask for your API Key,
if you don't have one,
you can check out this link https://jsonbin.io
and get one, otherwise you won't be able to use this script.
"""
api_key = os.environ["BIN_APIKEY"]
"""
In order the set the environment variable with your API KEY,
you need to do the following:

    * GNU/LINUX OS, Unix Like, MAC OS:
        Open a terminal window a enter the follow line:
        export BIN_APIKEY='yourapikeyhere'
    * Windows:
        - Open a CMD window and enter this line:
            set BIN_APIKEY="yourapikeyhere"
        - Open a POWERSHELL window and enter this line:
            $env:BIN_APIKEY = "yourapikeyhere"
"""

def get_bin():
    b = input("Introduce the Bin ID: ")
    headers = {"secret-key": api_key}
    r = requests.get(host + b, headers=headers)

    print(r.json())

def add_bin():
    one_bin = {
            "id": 1,
            "name": "Flask"
            }
    headers = {"secret-key": api_key, "private": "true"}
    r = requests.post(host, headers=headers, json=one_bin)

    print(r.json())

def edit_bin():
    b = input("Introduce the Bin ID: ")
    another_bin = {
            "id": 2,
            "name": "ExpressJS"
            }
    headers = {"secret-key": api_key}
    r = requests.put(host + b, headers=headers, json=another_bin)

    print(r.json())

def delete_bin():
    b = input("Introduce the Bin ID: ")
    headers = {"secret-key": api_key}
    r = requests.delete(host + b, headers=headers)

    print(r.json())

def menu():
    o = 0

    print("\nMenu:")
    print("0: Exit")
    print("1: Get a Bin")
    print("2: Add a Bin (it has values by default)")
    print("3: Edit an existent Bin (the values are replaced by other default values)")
    print("4: Delete a Bin")

    o = int(input("Enter an option: "))
    if o == 1:
        get_bin()
    elif o == 2:
        add_bin()
    elif o == 3:
        edit_bin()
    elif o == 4:
        delete_bin()
    else:
        print("Thanks for using this private API demo. Made by ISC School and CodeNoSchool")

    return o

def main():
    print("Welcome to this private API Demo. Good luck!")

    if api_key:
        o = 1
        while o != 0:
            o = menu()
    else:
        print("Sorry, you cannot use this API tool without an API KEY.")
        print("Make sure to have an environment variable set with your apikey called BIN_APIKEY")
        print("Script made by ISC School and CodeNoSchool")

if __name__ == "__main__":
    main()

