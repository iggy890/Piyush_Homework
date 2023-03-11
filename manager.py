# Finish this
from sys import argv
FILE = "logins.txt"

def encrypt(message: str, key: str) -> str:
    return message

def decrypt(message: str, key: str) -> str:
    return message

args = argv
args.remove("manager.py")
usernames = []
passwords = []

def write_to_file(l, l2):
    with open(FILE, "w") as f:
        d = {}
        for i, j in zip(usernames, passwords):
            d[i] = j

        f.write(str(d))

def read_from_file():
    with open(FILE, "r") as f:
        contents = dict(f.read())
        

if args == []:
    print("Usage: python3 Shell.py [login]")

def find_str_in_list(s: str, l: list):
    for i in l:
        if i == l:
            return True
    return False

if args[0] == "login":
    username = input("Username: ")
    if not find_str_in_list(username, usernames):
        option = input("You don't have an account, would you like to create one? Y/N ")
        if option == "Y":
            print("Creating Account...")
            usernames.append(username)
            password = input("$ Password: ")
            passwords.append(encrypt(password, username))
            print("Finalizing...")
            print("Complete!")

    print(f"Welcome {username} what would you like to do? ")
    command = input("")