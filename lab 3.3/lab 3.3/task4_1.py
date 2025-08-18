def login_user(username, password):
    """
    Simulates user login by checking username and password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    # Example: hardcoded user credentials for demonstration
    valid_users = {
        "admin": "admin123",
        "user": "userpass",
        "guest": "guest"
    }
    if username in valid_users and valid_users[username] == password:
        return True
    else:
        return False

# Example usage
if __name__ == "__main__":
    uname = input("Enter username: ")
    pwd = input("Enter password: ")
    if login_user(uname, pwd):
        print("Login successful!")
    else:
        print("Invalid username or password.")