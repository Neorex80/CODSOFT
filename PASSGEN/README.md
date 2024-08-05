---

# Password Generator Application

This is a command-line Password Generator application written in Python. It allows users to generate strong and random passwords of specified lengths and complexities. Additionally, it can save the generated passwords along with associated usernames/emails and site/application names into a JSON file for easy retrieval.

## Features

- **Generate Password**: Generate a random password based on specified length and complexity.
- **Save Password**: Save the generated password along with the username/email and site/application name to a JSON file.
- **View Saved Passwords**: View all saved passwords from the JSON file.
- **Colored Output**: Uses the `colorama` library to provide a colored and user-friendly terminal output.

## Prerequisites

- Python 3.x
- `colorama` library for colored terminal output

You can install the `colorama` library using pip:

```bash
pip install colorama
```

## Usage

1. Clone the repository or download the `password_generator.py` file.

2. Open your terminal and navigate to the directory containing `passgen.py`.

3. Run the application:

```bash
python password_generator.py
```

## How to Use

### Main Menu

When you run the application, you will see the main menu with the following options:

```
===== Password Generator Menu =====
1. Generate a new password
2. View saved passwords
3. Exit
```

### Generating a Password

1. Choose option `1` from the main menu.
2. Enter the desired length of the password.
3. Enter the desired complexity of the password:
   - `1`: Letters only
   - `2`: Letters and digits
   - `3`: Letters, digits, and punctuation
4. The generated password will be displayed.
5. You will be prompted to save the password:
   - If you choose `yes`, you will be asked to enter the username/email and site/application name.
   - The password along with the entered details will be saved to `passwords.json`.

### Viewing Saved Passwords

1. Choose option `2` from the main menu.
2. The application will display all saved passwords from `passwords.json`.

### Exiting the Application

Choose option `3` from the main menu to exit the application.

## Example

```
Welcome to the Password Generator!

===== Password Generator Menu =====
1. Generate a new password
2. View saved passwords
3. Exit
Enter your choice: 1
Enter the desired length of the password: 12
Enter the desired complexity (1: letters, 2: letters and digits, 3: letters, digits, and punctuation): 3
Generated Password: aBcD1@#2eFgH
Do you want to save this password? (yes/no): yes
Enter the username/email: user@example.com
Enter the site/application name: example.com
Password saved successfully!

===== Password Generator Menu =====
1. Generate a new password
2. View saved passwords
3. Exit
Enter your choice: 2
Saved Passwords:
Username: user@example.com, Site: example.com, Password: aBcD1@#2eFgH

===== Password Generator Menu =====
1. Generate a new password
2. View saved passwords
3. Exit
Enter your choice: 3
Goodbye!
```

## Code Overview

Here is a brief overview of the code structure:

### Functions

- `generate_password(length, complexity)`: Generates a random password based on the specified length and complexity.
- `save_password(username, site, password)`: Saves the generated password along with the username/email and site/application name to a JSON file.
- `view_passwords()`: Displays all saved passwords from the JSON file.
- `main()`: Main function that handles the user interaction and menu navigation.

### JSON File

The generated passwords are saved in a JSON file named `passwords.json` in the following format:

```json
[
    {
        "username": "user@example.com",
        "site": "example.com",
        "password": "aBcD1@#2eFgH"
    }
]
```

## License

This project is licensed under the MIT License.

## Acknowledgements

This application was developed with the help of the `colorama` library for colorful terminal output.

---
