"""
Demo Script - Contact Book Usage Examples
Using only: lists, tuples, dictionaries, sets, and comprehensions
"""

from contacts import (
    create_contact_book, add_contact, search_contact, get_contact_by_phone,
    update_contact, delete_contact, list_all_contacts, format_contact,
    find_duplicate_names, batch_create_contacts, get_contact_statistics,
    get_contacts_with_email, sort_contacts_by_name
)


def demo_contact_book():
    """Demonstrate Contact Book functionality using data structures"""
    
    print("="*60)
    print("CONTACT BOOK DEMO - Using Lists, Tuples, Dicts & Sets")
    print("="*60)
    
    # Initialize contact book
    contacts_dict, phone_set = create_contact_book()
    print("\n✓ Contact book initialized as (dict, set) tuple\n")
    
    # Demo 1: Add contacts using tuple list
    print("--- DEMO 1: Adding Contacts from Tuple List ---")
    contacts_data = [
        ("Alice Johnson", "555-1111", "alice@example.com", "123 Main St"),
        ("Bob Smith", "555-2222", "bob@example.com", "456 Oak Ave"),
        ("Charlie Brown", "555-3333", "charlie@example.com", "789 Pine Rd"),
        ("Diana Prince", "555-4444", "diana@example.com", "321 Elm St"),
    ]
    
    # Using comprehension implicitly (loop through tuples)
    for name, phone, email, address in contacts_data:
        success, msg = add_contact(contacts_dict, phone_set, name, phone, email, address)
        print(f"{'✓' if success else '✗'} {msg}")
    
    print(f"\nTotal contacts: {len(contacts_dict)}")
    print(f"Phone set: {phone_set}")
    
    # Demo 2: Duplicate detection with sets
    print("\n--- DEMO 2: Duplicate Phone Number Detection (SET-Based) ---")
    success, msg = add_contact(contacts_dict, phone_set, "Eve Wilson", "555-1111", "eve@example.com")
    print(f"{'✓' if success else '✗'} {msg} (Expected: Error - Duplicate in set)")
    
    # Demo 3: Search using list comprehension
    print("\n--- DEMO 3: Search Using List Comprehension ---")
    print("\nSearch 1: Find 'alice'")
    results = search_contact(contacts_dict, "alice")
    [print(f"  → {c['name']}: {c['phone']}") for c in results]
    
    print("\nSearch 2: Find '555-3333'")
    results = search_contact(contacts_dict, "555-3333")
    [print(f"  → {c['name']}: {c['phone']}") for c in results]
    
    # Demo 4: List comprehension for filtering
    print("\n--- DEMO 4: Contacts with Email (List Comprehension) ---")
    contacts_with_emails = get_contacts_with_email(contacts_dict)
    print(f"Contacts with email addresses: {len(contacts_with_emails)}")
    [print(f"  • {c['name']}: {c['email']}") for c in contacts_with_emails]
    
    # Demo 5: Dictionary comprehension for name mapping
    print("\n--- DEMO 5: Phone to Name Mapping (Dict Comprehension) ---")
    phone_to_name = {phone: contact['name'] for phone, contact in contacts_dict.items()}
    print("Phone → Name mapping:")
    [print(f"  {phone} → {name}") for phone, name in phone_to_name.items()]
    
    # Demo 6: Set comprehension for phone numbers
    print("\n--- DEMO 6: Extract Phone Numbers (Set Comprehension) ---")
    phones_set = {contact['phone'] for contact in contacts_dict.values()}
    print(f"Phone numbers as set: {phones_set}")
    
    # Demo 7: Sorted contacts using lambda
    print("\n--- DEMO 7: Sorted Contacts by Name ---")
    sorted_contacts = sort_contacts_by_name(contacts_dict)
    print("Sorted by name:")
    [print(f"  {i}. {c['name']:<20} | {c['phone']}") for i, c in enumerate(sorted_contacts, 1)]
    
    # Demo 8: Update contact
    print("\n--- DEMO 8: Update Contact ---")
    print("Before update:")
    contact = get_contact_by_phone(contacts_dict, "555-1111")
    print(f"  {contact['name']} - {contact['email']}")
    
    success, msg = update_contact(
        contacts_dict, phone_set, "555-1111",
        email="alice.j@newdomain.com",
        address="999 New Street"
    )
    print(f"\n{'✓' if success else '✗'} {msg}")
    print("After update:")
    contact = get_contact_by_phone(contacts_dict, "555-1111")
    print(f"  {contact['name']} - {contact['email']}")
    
    # Demo 9: Update phone number
    print("\n--- DEMO 9: Update Phone Number ---")
    print(f"Phone set before: {len(phone_set)} phones")
    success, msg = update_contact(contacts_dict, phone_set, "555-2222", new_phone="555-2222-NEW")
    print(f"{'✓' if success else '✗'} {msg}")
    print(f"Phone set after: {len(phone_set)} phones")
    contact = get_contact_by_phone(contacts_dict, "555-2222-NEW")
    print(f"  Updated: {contact['name']}: {contact['phone']}")
    
    # Demo 10: Get specific contact
    print("\n--- DEMO 10: View Contact Details ---")
    contact = get_contact_by_phone(contacts_dict, "555-3333")
    if contact:
        print(f"\nContact Details:")
        print(format_contact(contact))
    
    # Demo 11: Delete contact
    print("\n--- DEMO 11: Delete Contact ---")
    print(f"Total contacts before deletion: {len(contacts_dict)}")
    success, msg = delete_contact(contacts_dict, phone_set, "555-4444")
    print(f"{'✓' if success else '✗'} {msg}")
    print(f"Total contacts after deletion: {len(contacts_dict)}")
    print(f"Remaining phones in set: {phone_set}")
    
    # Demo 12: Statistics using comprehensions
    print("\n--- DEMO 12: Contact Book Statistics (Comprehensions) ---")
    stats = get_contact_statistics(contacts_dict)
    print(f"Total Contacts: {stats['total_contacts']}")
    print(f"Contacts with Email: {stats['contacts_with_email']}")
    print(f"Contacts with Address: {stats['contacts_with_address']}")
    print(f"All names (tuple): {stats['names']}")
    
    # Demo 13: Batch create contacts from tuples
    print("\n--- DEMO 13: Batch Create Contacts (Dict Comprehension) ---")
    new_contacts_data = [
        ("Frank Castle", "555-5555", "frank@example.com", "500 King St"),
        ("Grace Lee", "555-6666", "grace@example.com", "600 Queen Ave"),
    ]
    batch_dict = batch_create_contacts(new_contacts_data)
    print(f"Batch created {len(batch_dict)} contacts:")
    [print(f"  • {contact['name']}: {contact['phone']}") for contact in batch_dict.values()]
    
    # Demo 14: Find duplicate names
    print("\n--- DEMO 14: Find Duplicate Names (Nested Comprehension) ---")
    # Add duplicate name
    add_contact(contacts_dict, phone_set, "Alice New", "555-7777", "alice2@example.com")
    duplicates = find_duplicate_names(contacts_dict)
    if duplicates:
        print("Duplicate names found:")
        for name, phones in duplicates.items():
            print(f"  • '{name}' appears in: {phones}")
    else:
        print("No duplicate names found")
    
    # Demo 15: Final state
    print("\n--- DEMO 15: Final State Summary ---")
    all_contacts = list_all_contacts(contacts_dict)
    print(f"Final contact count: {len(all_contacts)}")
    print(f"Final phone set size: {len(phone_set)}")
    print("All contacts (using list comprehension):")
    [print(f"  {i}. {c['name']:<20} | {c['phone']}") for i, c in enumerate(sorted(all_contacts, key=lambda x: x['name']), 1)]
    
    print("\n" + "="*60)
    print("DEMO COMPLETED - All using Lists, Tuples, Dicts & Sets!")
    print("="*60)


if __name__ == "__main__":
    demo_contact_book()
