import requests

host = "https://api.jsonbin.io/b/"
api_key = ""

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

    print("Menu:")
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
    global api_key

    print("Welcome to this private API Demo. Good luck!")
    api_key = input("Enter your Key API: ")

    if api_key:
        o = 1
        while o != 0:
            o = menu()
    else:
        print("Sorry, you cannot use this API tool without an API KEY. (Made by ISC School and CodeNoShool")

if __name__ == "__main__":
    main()

