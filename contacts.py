"""
Contact Book Module
Manages contacts using dictionaries, sets, and comprehensions.
Uses only: lists, tuples, dictionaries, sets, and comprehensions.
"""


def create_contact(name, phone, email="", address=""):
    """
    Create a contact dictionary
    
    Args:
        name: Contact's name
        phone: Contact's phone number
        email: Contact's email (optional)
        address: Contact's address (optional)
        
    Returns:
        dict: Contact data as dictionary {name, phone, email, address}
    """
    return {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }


def format_contact(contact):
    """Format contact dictionary for display"""
    return f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}"


def create_contact_book():
    """
    Create a new contact book with tracking structures
    
    Returns:
        tuple: (contacts_dict, phone_set) where:
            - contacts_dict: {phone: contact_dict}
            - phone_set: set of all phone numbers for duplicate detection
    """
    return {}, set()


def add_contact(contacts_dict, phone_set, name, phone, email="", address=""):
    """
    Add a new contact to the contact book
    
    Returns:
        tuple: (success: bool, message: str)
    """
    if phone in phone_set:
        return False, f"Error: Phone number {phone} already exists!"
    
    contact = create_contact(name, phone, email, address)
    contacts_dict[phone] = contact
    phone_set.add(phone)
    return True, f"Contact '{name}' added successfully!"


def search_contact(contacts_dict, query):
    """
    Search for contacts by name or phone number
    
    Uses list comprehension to filter matching contacts
    
    Returns:
        list: Matching contact dictionaries
    """
    return [
        contact for contact in contacts_dict.values()
        if query.lower() in contact["name"].lower() or query in contact["phone"]
    ]


def get_contact_by_phone(contacts_dict, phone):
    """Get a contact by phone number"""
    return contacts_dict.get(phone)


def update_contact(contacts_dict, phone_set, phone, name=None, email=None, address=None, new_phone=None):
    """
    Update an existing contact
    
    Returns:
        tuple: (success: bool, message: str)
    """
    if phone not in contacts_dict:
        return False, f"Error: Contact with phone {phone} not found!"
    
    if new_phone and new_phone != phone and new_phone in phone_set:
        return False, f"Error: Phone number {new_phone} already exists!"
    
    contact = contacts_dict[phone]
    
    # Update fields if provided
    if name:
        contact["name"] = name
    if email:
        contact["email"] = email
    if address:
        contact["address"] = address
    
    # Handle phone number change
    if new_phone and new_phone != phone:
        contact["phone"] = new_phone
        contacts_dict[new_phone] = contact
        del contacts_dict[phone]
        phone_set.remove(phone)
        phone_set.add(new_phone)
    
    return True, f"Contact updated successfully!"


def delete_contact(contacts_dict, phone_set, phone):
    """
    Delete a contact by phone number
    
    Returns:
        tuple: (success: bool, message: str)
    """
    if phone not in contacts_dict:
        return False, f"Error: Contact with phone {phone} not found!"
    
    contact_name = contacts_dict[phone]["name"]
    del contacts_dict[phone]
    phone_set.remove(phone)
    return True, f"Contact '{contact_name}' deleted successfully!"


def list_all_contacts(contacts_dict):
    """Get all contacts as a list using dict values"""
    return list(contacts_dict.values())


def get_all_names(contacts_dict):
    """Get all contact names using dict comprehension"""
    return {phone: contact["name"] for phone, contact in contacts_dict.items()}


def get_contacts_with_email(contacts_dict):
    """Get only contacts that have email addresses using comprehension"""
    return [contact for contact in contacts_dict.values() if contact["email"]]


def get_phone_numbers_set(contacts_dict):
    """Get all phone numbers as a set using set comprehension"""
    return {contact["phone"] for contact in contacts_dict.values()}


def find_duplicate_names(contacts_dict):
    """
    Find contacts with duplicate names using comprehensions and sets
    
    Returns:
        dict: {name: [list of phone numbers]}
    """
    all_names = [contact["name"] for contact in contacts_dict.values()]
    duplicate_names = {name for name in all_names if all_names.count(name) > 1}
    return {
        name: [phone for phone, contact in contacts_dict.items() if contact["name"] == name]
        for name in duplicate_names
    }


def get_contacts_by_name_prefix(contacts_dict, prefix):
    """Get contacts whose name starts with given prefix using comprehension"""
    return [
        contact for contact in contacts_dict.values()
        if contact["name"].lower().startswith(prefix.lower())
    ]


def sort_contacts_by_name(contacts_dict):
    """
    Get sorted list of contacts by name
    
    Returns:
        list: Contacts sorted by name
    """
    return sorted(contacts_dict.values(), key=lambda x: x["name"])


def get_contact_info_tuple(contact):
    """
    Convert contact dictionary to tuple for compact storage
    
    Returns:
        tuple: (name, phone, email, address)
    """
    return (contact["name"], contact["phone"], contact["email"], contact["address"])


def batch_create_contacts(contact_data_tuples):
    """
    Create multiple contacts from tuples using dict comprehension
    
    Args:
        contact_data_tuples: List of tuples (name, phone, email, address)
        
    Returns:
        dict: {phone: contact_dict}
    """
    return {
        phone: create_contact(name, phone, email, address)
        for name, phone, email, address in contact_data_tuples
    }


def get_contact_statistics(contacts_dict):
    """
    Get statistics about contacts using comprehensions
    
    Returns:
        dict: Statistics dictionary
    """
    contacts_list = list(contacts_dict.values())
    return {
        "total_contacts": len(contacts_dict),
        "contacts_with_email": len([c for c in contacts_list if c["email"]]),
        "contacts_with_address": len([c for c in contacts_list if c["address"]]),
        "names": tuple(c["name"] for c in contacts_list),
        "phones": tuple(c["phone"] for c in contacts_list),
    }
