import random
import string
import json
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def generate_password(length, complexity):
    """
    Generate a random password.
    
    :param length: Length of the password
    :param complexity: Complexity of the password (1: letters, 2: letters and digits, 3: letters, digits, and punctuation)
    :return: Generated password
    """
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Complexity level must be 1, 2, or 3.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(username, site, password):
    """
    Save the password to a JSON file.
    
    :param username: Username or email
    :param site: Site or application name
    :param password: Generated password
    """
    data = {
        "username": username,
        "site": site,
        "password": password
    }

    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    else:
        passwords = []

    passwords.append(data)

    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

def view_passwords():
    """
    View all saved passwords.
    """
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
        
        print(Fore.CYAN + "Saved Passwords:")
        for entry in passwords:
            print(Fore.YELLOW + f"Username: {entry['username']}, Site: {entry['site']}, Password: {entry['password']}")
    else:
        print(Fore.RED + "No passwords saved yet.")

def main():
    print(Fore.CYAN + "==== Welcome to the Password Generator! ====")

    while True:
        print(Fore.GREEN + "\nMenu:")
        print(Fore.GREEN + "1. Generate a new password")
        print(Fore.GREEN + "2. View saved passwords")
        print(Fore.GREEN + "3. Exit")
        
        choice = input(Fore.YELLOW + "Enter your choice: ").strip()
        
        if choice == '1':
            while True:
                try:
                    length = int(input(Fore.YELLOW + "Enter the desired length of the password: "))
                    if length <= 0:
                        raise ValueError("Password length must be greater than 0.")
                    break
                except ValueError as e:
                    print(Fore.RED + f"Invalid input: {e}. Please try again.")
            
            while True:
                try:
                    complexity = int(input(Fore.YELLOW + "Enter the desired complexity (1: letters, 2: letters and digits, 3: letters, digits, and punctuation): "))
                    if complexity not in [1, 2, 3]:
                        raise ValueError("Complexity level must be 1, 2, or 3.")
                    break
                except ValueError as e:
                    print(Fore.RED + f"Invalid input: {e}. Please try again.")
            
            password = generate_password(length, complexity)
            print(Fore.GREEN + f"Generated Password: {password}")

            save = input(Fore.YELLOW + "Do you want to save this password? (yes/no): ").strip().lower()
            if save == 'yes':
                username = input(Fore.YELLOW + "Enter the username/email: ").strip()
                site = input(Fore.YELLOW + "Enter the site/application name: ").strip()
                save_password(username, site, password)
                print(Fore.CYAN + "Password saved successfully!")
        
        elif choice == '2':
            view_passwords()
        
        elif choice == '3':
            print(Fore.CYAN + "Goodbye!")
            break
        
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
