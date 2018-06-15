import requests


"""
If you want to know more about how to use this app,
you can find more info on this link:
    https://github.com/codenoschool/restapis-course
"""


host = "https://jsonplaceholder.typicode.com"
"""
Make sure to visit: https://jsonplaceholder.typicode.com
to know more about this API functions.
"""

# GET MANY
def get_posts():
    r = requests.get(host + "/posts")

    for p in r.json():
        post = "userId: {}\nid: {}\nTitle: {}\nPost: {}\n\n".format(p["userId"], p["id"], p["title"], p["body"])

        print(post)


# GET ONE
def get_post():
    id = input("Introduce the ID post: ")
    r = requests.get(host + "/posts/" + id)

    p = r.json()
    post = "userId: {}\nid: {}\nTitle: {}\nPost: {}\n\n".format(p["userId"], p["id"], p["title"], p["body"])

    print(post)


# POST
def add_post():
    userId = input("Enter your userId: ")
    title = input("Title: ")
    body = input("Content: ")

    payload = {"userId": userId, "title": title, "body": body}
    r = requests.post(host + "/posts", json=payload)

    p = r.json()
    post = "userId: {}\nid: {}\nTitle: {}\nPost: {}\n\n".format(p["userId"], p["id"], p["title"], p["body"])

    print("\nHere is your new post:")
    print(post)


# PUT
def edit_post():
    id = input("Enter the ID of the post you want to edit: ")
    userId = input("userId: ")
    title = input("Title: ")
    body = input("Content: ")

    payload = {"userId": userId, "title": title, "body": body}
    r = requests.put(host + "/posts/" + id, json=payload)

    p = r.json()
    post = "userId: {}\nid: {}\nTitle: {}\nPost: {}\n\n".format(p["userId"], p["id"], p["title"], p["body"])

    print("\nHere is the post:")
    print(post)


# DELETE
def delete_post():
    id = input("Enter the ID of the post you want to delete: ")

    r = requests.delete(host + "/posts/" + id)

    print(r.json())
    print("The post was deleted successfully.")


# App Menu
def menu():
    o = 0
    print("\nMenu:")
    print("0: Exit")
    print("1: Get all Posts (100)")
    print("2: Get one post")
    print("3: Add a new post")
    print("4: Edit an existent post")
    print("5: Delete an existent post")
    o = int(input("Enter an option: "))
    print("\n")

    return o
    
def main():
    o = 1

    print("Hello! Good luck using this requests sample tool.")

    while o != 0:
        o = menu()
        if o == 1:
            get_posts()
        elif o == 2:
            get_post()
        elif o == 3:
            add_post()
        elif o == 4:
            edit_post()
        elif o == 5:
            delete_post()
        else:
            print("Thank you for using this tool to make simple requests. Made by CodeNoSchool")

if __name__ == "__main__":
    main()

