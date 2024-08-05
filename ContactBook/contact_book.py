import json
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class ContactBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        print(Fore.CYAN + "===== Add a New Contact =====" + Style.RESET_ALL)
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email: ")
        address = input("Enter the address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        self.contacts.append(contact)
        self.save_contacts()
        print(Fore.GREEN + "Contact added!" + Style.RESET_ALL)

    def view_contacts(self):
        print("\n" + Fore.CYAN + "===== Contact List =====" + Style.RESET_ALL)
        if not self.contacts:
            print(Fore.RED + "No contacts available." + Style.RESET_ALL)
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")
        print(Style.RESET_ALL)

    def search_contacts(self):
        print(Fore.CYAN + "===== Search Contacts =====" + Style.RESET_ALL)
        search_term = input("Enter the name or phone number to search: ").lower()
        found_contacts = [contact for contact in self.contacts if search_term in contact["name"].lower() or search_term in contact["phone"]]
        if found_contacts:
            print("\n" + Fore.CYAN + "Found Contacts:" + Style.RESET_ALL)
            for index, contact in enumerate(found_contacts, start=1):
                print(f"{index}. {contact['name']} - {contact['phone']}")
                print(f"   Email: {contact['email']}")
                print(f"   Address: {contact['address']}\n")
        else:
            print(Fore.RED + "No contacts found." + Style.RESET_ALL)

    def update_contact(self):
        print(Fore.CYAN + "===== Update Contact =====" + Style.RESET_ALL)
        self.view_contacts()
        try:
            contact_index = int(input("Enter the contact number to update: ")) - 1
            if 0 <= contact_index < len(self.contacts):
                contact = self.contacts[contact_index]
                print(f"Updating contact: {contact['name']}")
                contact["name"] = input(f"Enter new name (leave blank to keep '{contact['name']}'): ") or contact["name"]
                contact["phone"] = input(f"Enter new phone number (leave blank to keep '{contact['phone']}'): ") or contact["phone"]
                contact["email"] = input(f"Enter new email (leave blank to keep '{contact['email']}'): ") or contact["email"]
                contact["address"] = input(f"Enter new address (leave blank to keep '{contact['address']}'): ") or contact["address"]
                self.save_contacts()
                print(Fore.GREEN + "Contact updated!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid contact number." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input." + Style.RESET_ALL)

    def delete_contact(self):
        print(Fore.CYAN + "===== Delete Contact =====" + Style.RESET_ALL)
        self.view_contacts()
        try:
            contact_index = int(input("Enter the contact number to delete: ")) - 1
            if 0 <= contact_index < len(self.contacts):
                del self.contacts[contact_index]
                self.save_contacts()
                print(Fore.GREEN + "Contact deleted!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid contact number." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input." + Style.RESET_ALL)

def main():
    contact_book = ContactBook("contacts.json")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        contact_book.view_contacts()
        print(Fore.CYAN + "\n===== Contact Book Menu =====" + Style.RESET_ALL)
        print(Fore.CYAN + "1. Add Contact" + Style.RESET_ALL)
        print(Fore.CYAN + "2. Search Contacts" + Style.RESET_ALL)
        print(Fore.CYAN + "3. Update Contact" + Style.RESET_ALL)
        print(Fore.CYAN + "4. Delete Contact" + Style.RESET_ALL)
        print(Fore.CYAN + "5. Exit" + Style.RESET_ALL)

        choice = input("Enter your choice: ")

        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.search_contacts()
        elif choice == '3':
            contact_book.update_contact()
        elif choice == '4':
            contact_book.delete_contact()
        elif choice == '5':
            print(Fore.GREEN + "Exiting the contact book. Thanks for using it!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
