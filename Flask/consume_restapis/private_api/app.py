import requests

host = "https://api.jsonbin.io/b/"
api_key = "$2a$10$q0l.Q65.t7okoY5GYuvGR.Tq1T6g5/UiuLW5JiMdPALRckgE58lF2"

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
    print("Welcome to this private API Demo. Good luck!")
    o = 1
    while o != 0:
        o = menu()

if __name__ == "__main__":
    main()

