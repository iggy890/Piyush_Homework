import argparse

users = {}

def register(username, password):
    if username in users:
        print(f"{username} already exists.")
    else:
        users[username] = password
        print(f"{username} successfully registered.")

def login(username, password):
    if username not in users or users[username] != password:
        print("Invalid username or password.")
        return False
    else:
        print(f"Welcome, {username}!")
        return True

def add_task(task):
    if not current_user:
        print("You must be logged in to add a task.")
    else:
        tasks.append((current_user, task))
        print(f"Task '{task}' added for user {current_user}.")

def list_tasks():
    if not current_user:
        print("You must be logged in to list tasks.")
    else:
        user_tasks = [task for task in tasks if task[0] == current_user]
        if user_tasks:
            print(f"Tasks for user {current_user}:")
            for task in user_tasks:
                print(f" - {task[1]}")
        else:
            print(f"No tasks found for user {current_user}.")

def parse_args():
    parser = argparse.ArgumentParser(description="Task management tool")
    subparsers = parser.add_subparsers(dest="command")

    register_parser = subparsers.add_parser("register", help="Register a new user")
    register_parser.add_argument("username", type=str, help="Username to register")
    register_parser.add_argument("password", type=str, help="Password for new user")

    login_parser = subparsers.add_parser("login", help="Log in an existing user")
    login_parser.add_argument("username", type=str, help="Username to log in")
    login_parser.add_argument("--password", type=str, help="Password for user (will prompt if not provided)")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="Task to add")

    list_parser = subparsers.add_parser("list", help="List all tasks")

    return parser.parse_args()

tasks = []

current_user = None

args = parse_args()

if args.command == "register":
    register(args.username, args.password)

elif args.command == "login":
    password = args.password
    if login(args.username, password):
        current_user = args.username

elif args.command == "add":
    add_task(args.task)

elif args.command == "list":
    list_tasks()
