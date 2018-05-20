import requests

url = "http://127.0.0.1:5000/api"

"""
This code works only in python >= 3.6 versions,
either way you can pretty small changes to format strings in
a different way, so you can get this code working correctly.
"""


# GET MANY
def get_frameworks():
    print("List of available frameworks:")
    frameworks = requests.get(url + "/frameworks/")
    result = frameworks.json()
    for f in result:
        print(f"ID: {f['id']} | Name: {f['name']}")

# GET ONE
def get_framework_by_name():
    framework_name = input("Enter the name of framework to search: ")
    framework = requests.get(url + "/frameworks/" + framework_name)
    result = framework.json()
    print(f"Result | ID: {result['id']} Name: {result['name']}")

# POST
def add_framework():
    print("Now you'll submit a new framework.")
    new_framework = input("Enter the name for the new framework: ")
    payload = { "name": new_framework }
    new_framework_request = requests.post(url + "/frameworks/", json=payload)
    result = new_framework_request.json()
    print(f"The framework with ID: {result['id']} and Name: {result['name']} has been added.") 

# PUT
def edit_framework():
    print("Let's modify an existant framework.")
    framework_id = input("Enter the ID of the framework to modify: ")
    new_framework_name = input("Enter the new name for the framework: ")
    payload = { "name": new_framework_name }
    framework = requests.put(url + "/frameworks/" + framework_id, json=payload)
    result = framework.json()
    print(f"Now the name of the framework with ID {result['id']} is: {result['name']}")

# DELETE
def delete_framework():
    print("Warning: Now it is time to delete a framework")
    framework_id = input("Enter the ID of the framework to delete: ")
    request = requests.delete(url + "/frameworks/" + framework_id)
    result = request.json()
    print("The result of the delete request was: " + result["message"])

def menu():
    print("Menu:")
    print("""
    0 | Exit
    1 | Get frameworks
    2 | Get a framework
    3 | Add a framework
    4 | Modifiy a framework
    5 | Delete a framework
    """)

def execute_options(option):
    if option == 0:
        print("\nThank you for using this demo, don't forget to check out ISC School and CodeNoSchool YouTube channels.")

    elif option == 1:
        get_frameworks()

    elif option == 2:
        get_framework_by_name()

    elif option == 3:
        add_framework()

    elif option == 4:
        edit_framework()

    elif option == 5:
        delete_framework()

def main():
    print("Hello, this is a demo to consume a REST API through Req&Res")
    print("You'll need a local Flask REST API active from the REST APIS course by CodeNoShool")

    print("Let's start...\n")

    menu()
    option = int(input("Enter an option: "))
    print("\n")
    execute_options(option)
    print("\n")
    while option != 0:
        menu()
        option = int(input("Enter an option: "))
        print("\n")
        execute_options(option)
        print("\n")

if __name__ == "__main__":
    main()
