---

# Contact Book

This is a command-line Contact Book application written in Python. It allows users to manage their contacts efficiently with features like adding, viewing, searching, updating, and deleting contacts. The contacts are saved in a JSON file for persistence.

## Features

- **Add Contact**: Add a new contact with name, phone number, email, and address.
- **View Contacts**: Display a list of all saved contacts with names and phone numbers.
- **Search Contacts**: Find contacts by name or phone number.
- **Update Contact**: Update the details of a selected contact.
- **Delete Contact**: Delete a selected contact.

## Prerequisites

- Python 3.x
- `colorama` library for colored terminal output

You can install the `colorama` library using pip:

```bash
pip install colorama
```

## Usage

1. Clone the repository or download the `contact_book.py` file.
2. Open your terminal and navigate to the directory containing `contact_book.py`.
3. Run the application:

```bash
python contact_book.py
```

## Example

```
===== Contact List =====
1. John Doe - 1234567890
2. Jane Smith - 9876543210

===== Contact Book Menu =====
1. Add Contact
2. Search Contacts
3. Update Contact
4. Delete Contact
5. Exit
Enter your choice: 1
===== Add a New Contact =====
Enter the name: Alice Johnson
Enter the phone number: 5551234567
Enter the email: alice@example.com
Enter the address: 456 Oak St
Contact added!
Press Enter to continue...
```

## License

This project is licensed under the MIT License.

---
