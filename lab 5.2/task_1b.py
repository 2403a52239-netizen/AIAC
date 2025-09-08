import os
import bcrypt

# Simulated user database with hashed passwords
# In a real app, this would come from a secure database
users = {
    "admin": bcrypt.hashpw(os.environ["ADMIN_PASSWORD"].encode(), bcrypt.gensalt()),
    "user": bcrypt.hashpw(os.environ["USER_PASSWORD"].encode(), bcrypt.gensalt())
}

def login(username, password):
    if username in users:
        stored_hash = users[username]
        if bcrypt.checkpw(password.encode(), stored_hash):
            print("✅ Login successful!")
            return
    print("❌ Login failed.")

# 👇 User input section
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    login(username, password)