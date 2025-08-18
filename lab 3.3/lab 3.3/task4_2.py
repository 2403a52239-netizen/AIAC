def register_user(username, password, users_db):
    """
    Registers a new user by adding the username and password to the users_db dictionary.

    Args:
        username (str): The username to register.
        password (str): The password for the user.
        users_db (dict): The dictionary storing user credentials.

    Returns:
        bool: True if registration is successful, False if username already exists.
    """
    if username in users_db:
        return False  # Username already exists
    users_db[username] = password
    return True
    # Example usage
if __name__ == "__main__":
    users_db = {
        "admin": "admin123",
        "user": "userpass"
    }
    username = input("Enter a username to register: ")
    password = input("Enter a password: ")
    if register_user(username, password, users_db):
        print("Registration successful!")
    else:
        print("Username already exists. Please choose a different username.")
