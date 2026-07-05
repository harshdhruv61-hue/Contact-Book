"""
Contact Book CLI Application
A command-line interface using only dictionaries, lists, tuples, sets, and comprehensions.
"""

from contacts import (
    create_contact_book, add_contact, search_contact, get_contact_by_phone,
    update_contact, delete_contact, list_all_contacts, sort_contacts_by_name,
    get_contact_statistics, format_contact
)
import os


def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("         CONTACT BOOK - MAIN MENU")
    print("="*50)
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. List all contacts")
    print("6. View contact details")
    print("7. Statistics")
    print("8. Exit")
    print("="*50)


def add_contact_ui(contacts_dict, phone_set):
    """UI for adding a contact"""
    print("\n--- ADD NEW CONTACT ---")
    name = input("Enter contact name: ").strip()
    
    if not name:
        print("Error: Name cannot be empty!")
        return
    
    phone = input("Enter phone number: ").strip()
    
    if not phone:
        print("Error: Phone number cannot be empty!")
        return
    
    email = input("Enter email (optional): ").strip()
    address = input("Enter address (optional): ").strip()
    
    success, message = add_contact(contacts_dict, phone_set, name, phone, email, address)
    print(f"\n{'✓' if success else '✗'} {message}")


def search_contact_ui(contacts_dict):
    """UI for searching contacts"""
    print("\n--- SEARCH CONTACT ---")
    query = input("Enter name or phone number to search: ").strip()
    
    if not query:
        print("Error: Search query cannot be empty!")
        return
    
    results = search_contact(contacts_dict, query)
    
    if not results:
        print(f"No contacts found for '{query}'")
        return
    
    print(f"\nFound {len(results)} contact(s):")
    for i, contact in enumerate(results, 1):
        print(f"\n--- Contact {i} ---")
        print(format_contact(contact))


def update_contact_ui(contacts_dict, phone_set):
    """UI for updating a contact"""
    print("\n--- UPDATE CONTACT ---")
    phone = input("Enter phone number of contact to update: ").strip()
    
    contact = get_contact_by_phone(contacts_dict, phone)
    if not contact:
        print(f"Error: Contact with phone {phone} not found!")
        return
    
    print(f"\nCurrent contact: {contact['name']}")
    print("(Leave blank to keep current value)\n")
    
    new_name = input(f"New name [{contact['name']}]: ").strip()
    new_email = input(f"New email [{contact['email']}]: ").strip()
    new_address = input(f"New address [{contact['address']}]: ").strip()
    new_phone = input("New phone number (optional): ").strip()
    
    success, message = update_contact(
        contacts_dict,
        phone_set,
        phone,
        name=new_name if new_name else None,
        email=new_email if new_email else None,
        address=new_address if new_address else None,
        new_phone=new_phone if new_phone else None
    )
    print(f"\n{'✓' if success else '✗'} {message}")


def delete_contact_ui(contacts_dict, phone_set):
    """UI for deleting a contact"""
    print("\n--- DELETE CONTACT ---")
    phone = input("Enter phone number of contact to delete: ").strip()
    
    contact = get_contact_by_phone(contacts_dict, phone)
    if not contact:
        print(f"Error: Contact with phone {phone} not found!")
        return
    
    confirm = input(f"Are you sure you want to delete '{contact['name']}'? (yes/no): ").strip().lower()
    
    if confirm != 'yes':
        print("Deletion cancelled.")
        return
    
    success, message = delete_contact(contacts_dict, phone_set, phone)
    print(f"\n{'✓' if success else '✗'} {message}")


def list_all_contacts_ui(contacts_dict):
    """UI for listing all contacts"""
    print("\n--- ALL CONTACTS ---")
    contacts = list_all_contacts(contacts_dict)
    
    if not contacts:
        print("No contacts in the contact book.")
        return
    
    print(f"Total contacts: {len(contacts)}\n")
    # Using comprehension to display contacts
    [print(f"{i}. {contact['name']} - {contact['phone']}") 
     for i, contact in enumerate(sorted(contacts, key=lambda x: x['name']), 1)]


def view_contact_details_ui(contacts_dict):
    """UI for viewing detailed contact information"""
    print("\n--- VIEW CONTACT DETAILS ---")
    phone = input("Enter phone number: ").strip()
    
    contact = get_contact_by_phone(contacts_dict, phone)
    if not contact:
        print(f"Error: Contact with phone {phone} not found!")
        return
    
    print(f"\n--- CONTACT DETAILS ---")
    print(format_contact(contact))


def show_statistics_ui(contacts_dict):
    """UI for displaying contact book statistics"""
    print("\n--- CONTACT BOOK STATISTICS ---")
    stats = get_contact_statistics(contacts_dict)
    
    print(f"Total Contacts: {stats['total_contacts']}")
    print(f"Contacts with Email: {stats['contacts_with_email']}")
    print(f"Contacts with Address: {stats['contacts_with_address']}")
    
    if stats['names']:
        print(f"\nAll Names: {', '.join(stats['names'])}")


def run_contact_book_app():
    """Run the main CLI loop"""
    contacts_dict, phone_set = create_contact_book()
    
    print("\n" + "="*50)
    print("   Welcome to Contact Book CLI Application!")
    print("="*50)
    
    menu_options = {
        '1': ('add', add_contact_ui),
        '2': ('search', search_contact_ui),
        '3': ('update', update_contact_ui),
        '4': ('delete', delete_contact_ui),
        '5': ('list', list_all_contacts_ui),
        '6': ('details', view_contact_details_ui),
        '7': ('stats', show_statistics_ui),
        '8': ('exit', None)
    }
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice not in menu_options:
            print("Error: Invalid choice! Please enter a number between 1 and 8.")
            input("\nPress Enter to continue...")
            continue
        
        action_name, action_func = menu_options[choice]
        
        if choice == '8':
            print("\nThank you for using Contact Book CLI!")
            print("Goodbye!\n")
            break
        
        # Call appropriate function with required arguments
        if choice in ['1', '3', '4']:
            # Functions that need both dictionaries
            action_func(contacts_dict, phone_set)
        else:
            # Functions that need only contacts_dict
            action_func(contacts_dict)
        
        input("\nPress Enter to continue...")


def main():
    """Entry point for the application"""
    run_contact_book_app()


if __name__ == "__main__":
    main()
