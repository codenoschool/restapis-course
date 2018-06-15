import requests

host = "https://api.jsonbin.io"
api_key = "$2a$10$q0l.Q65.t7okoY5GYuvGR.Tq1T6g5/UiuLW5JiMdPALRckgE58lF2"

def get_bins():
    b = "5b231b394e1aee358ec705ed"
    headers = {"secret-key": api_key}
    r = requests.get(host + "/b/" + b, headers=headers)

    users = r.json()

    for u in users:
        print(f"ID: {u['id']}, Email: {u['email']}, Username: {u['username']}, Lat: {u['address']['geo']['lat']}")

def get_bin():
    headers = {"secret-key": api_key}
    r = requests.get(host + "/b/" + b, headers=headers)

    print(r.json())

def create_bin():
    a_bin = {
            "id": 1,
            "name": "Flask"
            }
    headers = {"secret-key": api_key, "private": "true"}
    r = requests.post(host + "/b", headers=headers, json=a_bin)

    print(r.json())

def edit_bin():
    b = "5b23208213af2335beed3f5a"
    a_bin = {
            "id": 3,
            "name": "MaterializeCSS"
            }
    headers = {"secret-key": api_key}
    r = requests.put(host + "/b/" + b, headers=headers, json=a_bin)

    print(r.json())

def delete_bin():
    b = "5b23208213af2335beed3f5a"
    headers = {"secret-key": api_key}
    r = requests.delete(host + "/b/" + b, headers=headers)

    print(r.json())

def main():
    delete_bin()

if __name__ == "__main__":
    main()

