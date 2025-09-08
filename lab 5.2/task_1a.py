import getpass

# Sample user database
users = {
    "alice": "password123",
    "bob": "securepass",
    "charlie": "mypassword"
}

def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    login()