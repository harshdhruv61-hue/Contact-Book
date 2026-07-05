"""
Unit Tests for Contact Book
Tests using only: lists, tuples, dictionaries, sets, and comprehensions
"""

import unittest
from contacts import (
    create_contact_book, create_contact, add_contact, search_contact,
    get_contact_by_phone, update_contact, delete_contact, list_all_contacts,
    get_contact_info_tuple, batch_create_contacts, find_duplicate_names
)


class TestContactCreation(unittest.TestCase):
    """Test creating contacts as dictionaries"""
    
    def test_create_contact_dict(self):
        """Test creating a contact as a dictionary"""
        contact = create_contact("John Doe", "555-1234", "john@example.com", "123 Main St")
        self.assertIsInstance(contact, dict)
        self.assertEqual(contact["name"], "John Doe")
        self.assertEqual(contact["phone"], "555-1234")
        self.assertEqual(contact["email"], "john@example.com")
        self.assertEqual(contact["address"], "123 Main St")
    
    def test_create_contact_to_tuple(self):
        """Test converting contact to tuple"""
        contact = create_contact("John Doe", "555-1234", "john@example.com", "123 Main St")
        contact_tuple = get_contact_info_tuple(contact)
        self.assertIsInstance(contact_tuple, tuple)
        self.assertEqual(len(contact_tuple), 4)
        self.assertEqual(contact_tuple[0], "John Doe")


class TestContactBook(unittest.TestCase):
    """Test the Contact Book using data structures"""
    
    def setUp(self):
        """Create a fresh contact book for each test"""
        self.contacts_dict, self.phone_set = create_contact_book()
    
    def test_create_contact_book(self):
        """Test creating an empty contact book"""
        self.assertIsInstance(self.contacts_dict, dict)
        self.assertIsInstance(self.phone_set, set)
        self.assertEqual(len(self.contacts_dict), 0)
        self.assertEqual(len(self.phone_set), 0)
    
    def test_add_contact_success(self):
        """Test successfully adding a contact"""
        success, msg = add_contact(self.contacts_dict, self.phone_set, "John Doe", "555-1234")
        self.assertTrue(success)
        self.assertEqual(len(self.contacts_dict), 1)
        self.assertEqual(len(self.phone_set), 1)
    
    def test_add_duplicate_phone(self):
        """Test that duplicate phone numbers are rejected"""
        add_contact(self.contacts_dict, self.phone_set, "John Doe", "555-1234")
        success, msg = add_contact(self.contacts_dict, self.phone_set, "Jane Doe", "555-1234")
        self.assertFalse(success)
        self.assertEqual(len(self.contacts_dict), 1)
        self.assertEqual(len(self.phone_set), 1)
    
    def test_phone_set_integrity(self):
        """Test that phone set remains consistent with contacts dict"""
        phones = ["555-1111", "555-2222", "555-3333"]
        for i, phone in enumerate(phones):
            add_contact(self.contacts_dict, self.phone_set, f"Contact{i}", phone)
        
        # Verify set and dict are synchronized
        dict_phones = {contact["phone"] for contact in self.contacts_dict.values()}
        self.assertEqual(dict_phones, self.phone_set)
    
    def test_search_by_name_comprehension(self):
        """Test searching by name using list comprehension"""
        add_contact(self.contacts_dict, self.phone_set, "John Doe", "555-1234")
        add_contact(self.contacts_dict, self.phone_set, "Jane Doe", "555-5678")
        
        results = search_contact(self.contacts_dict, "John")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "John Doe")
    
    def test_search_by_phone(self):
        """Test searching by phone number"""
        add_contact(self.contacts_dict, self.phone_set, "John Doe", "555-1234")
        results = search_contact(self.contacts_dict, "555-1234")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["phone"], "555-1234")
    
    def test_search_case_insensitive(self):
        """Test that search is case-insensitive"""
        add_contact(self.contacts_dict, self.phone_set, "John Doe", "555-1234")
        results = search_contact(self.contacts_dict, "john")
        self.assertEqual(len(results), 1)
    
    def test_search_no_results(self):
        """Test search with no matching results"""
        add_contact(self.contacts_dict, self.phone_set, "John Doe", "555-1234")
        results = search_contact(self.contacts_dict, "xyz")
        self.assertEqual(len(results), 0)
        self.assertIsInstance(results, list)
    
    def test_get_contact_by_phone(self):
        """Test retrieving a contact by phone"""
        add_contact(self.contacts_dict, self.phone_set, "John Doe", "555-1234")
        contact = get_contact_by_phone(self.contacts_dict, "555-1234")
        self.assertIsNotNone(contact)
        self.assertEqual(contact["name"], "John Doe")
        self.assertIsInstance(contact, dict)
    
    def test_get_contact_not_found(self):
        """Test retrieving a non-existent contact"""
        contact = get_contact_by_phone(self.contacts_dict, "555-9999")
        self.assertIsNone(contact)
    
    def test_update_contact(self):
        """Test updating a contact"""
        add_contact(self.contacts_dict, self.phone_set, "John Doe", "555-1234", "old@example.com")
        success, msg = update_contact(self.contacts_dict, self.phone_set, "555-1234", email="new@example.com")
        self.assertTrue(success)
        
        contact = get_contact_by_phone(self.contacts_dict, "555-1234")
        self.assertEqual(contact["email"], "new@example.com")
    
    def test_update_phone_number(self):
        """Test updating a contact's phone number"""
        add_contact(self.contacts_dict, self.phone_set, "John Doe", "555-1234")
        success, msg = update_contact(self.contacts_dict, self.phone_set, "555-1234", new_phone="555-5678")
        self.assertTrue(success)
        
        # Old phone should not exist
        old_contact = get_contact_by_phone(self.contacts_dict, "555-1234")
        self.assertIsNone(old_contact)
        
        # New phone should exist
        new_contact = get_contact_by_phone(self.contacts_dict, "555-5678")
        self.assertIsNotNone(new_contact)
        self.assertEqual(new_contact["name"], "John Doe")
        
        # Phone set should be updated
        self.assertNotIn("555-1234", self.phone_set)
        self.assertIn("555-5678", self.phone_set)
    
    def test_update_duplicate_phone(self):
        """Test that updating to duplicate phone is rejected"""
        add_contact(self.contacts_dict, self.phone_set, "John Doe", "555-1234")
        add_contact(self.contacts_dict, self.phone_set, "Jane Doe", "555-5678")
        
        success, msg = update_contact(self.contacts_dict, self.phone_set, "555-1234", new_phone="555-5678")
        self.assertFalse(success)
    
    def test_update_non_existent(self):
        """Test updating a non-existent contact"""
        success, msg = update_contact(self.contacts_dict, self.phone_set, "555-9999", name="New Name")
        self.assertFalse(success)
    
    def test_delete_contact(self):
        """Test deleting a contact"""
        add_contact(self.contacts_dict, self.phone_set, "John Doe", "555-1234")
        success, msg = delete_contact(self.contacts_dict, self.phone_set, "555-1234")
        self.assertTrue(success)
        self.assertEqual(len(self.contacts_dict), 0)
        self.assertEqual(len(self.phone_set), 0)
        self.assertNotIn("555-1234", self.phone_set)
    
    def test_delete_non_existent(self):
        """Test deleting a non-existent contact"""
        success, msg = delete_contact(self.contacts_dict, self.phone_set, "555-9999")
        self.assertFalse(success)
    
    def test_list_all_contacts_as_list(self):
        """Test listing all contacts returns a list"""
        add_contact(self.contacts_dict, self.phone_set, "John Doe", "555-1234")
        add_contact(self.contacts_dict, self.phone_set, "Jane Doe", "555-5678")
        
        all_contacts = list_all_contacts(self.contacts_dict)
        self.assertIsInstance(all_contacts, list)
        self.assertEqual(len(all_contacts), 2)
        # Each item should be a dictionary
        self.assertTrue(all(isinstance(c, dict) for c in all_contacts))


class TestComprehensions(unittest.TestCase):
    """Test using list/dict/set comprehensions"""
    
    def setUp(self):
        self.contacts_dict, self.phone_set = create_contact_book()
        # Add sample contacts
        sample_data = [
            ("Alice Johnson", "555-1111", "alice@example.com", "123 Main St"),
            ("Bob Smith", "555-2222", "bob@example.com", "456 Oak Ave"),
            ("Charlie Brown", "555-3333", "", "789 Pine Rd"),
        ]
        for name, phone, email, address in sample_data:
            add_contact(self.contacts_dict, self.phone_set, name, phone, email, address)
    
    def test_dict_comprehension_mapping(self):
        """Test dict comprehension for phone-to-name mapping"""
        mapping = {phone: contact["name"] for phone, contact in self.contacts_dict.items()}
        self.assertIsInstance(mapping, dict)
        self.assertEqual(len(mapping), 3)
        self.assertEqual(mapping["555-1111"], "Alice Johnson")
    
    def test_set_comprehension_phones(self):
        """Test set comprehension for extracting phones"""
        phones = {contact["phone"] for contact in self.contacts_dict.values()}
        self.assertIsInstance(phones, set)
        self.assertEqual(len(phones), 3)
        self.assertEqual(phones, self.phone_set)
    
    def test_list_comprehension_with_filter(self):
        """Test list comprehension with filtering"""
        with_email = [c for c in self.contacts_dict.values() if c["email"]]
        self.assertEqual(len(with_email), 2)
    
    def test_nested_comprehension_names(self):
        """Test tuple comprehension for names"""
        names = tuple(c["name"] for c in self.contacts_dict.values())
        self.assertIsInstance(names, tuple)
        self.assertEqual(len(names), 3)


class TestDuplicateDetection(unittest.TestCase):
    """Test the set-based duplicate detection mechanism"""
    
    def setUp(self):
        self.contacts_dict, self.phone_set = create_contact_book()
    
    def test_set_based_duplicate_prevention(self):
        """Test that set-based duplicate prevention works"""
        success1, _ = add_contact(self.contacts_dict, self.phone_set, "Alice", "555-1111")
        self.assertTrue(success1)
        self.assertIn("555-1111", self.phone_set)
        
        success2, msg = add_contact(self.contacts_dict, self.phone_set, "Bob", "555-1111")
        self.assertFalse(success2)
        self.assertEqual(len(self.phone_set), 1)
    
    def test_phone_set_uniqueness(self):
        """Test that phone_set maintains uniqueness"""
        phones = ["555-1111", "555-2222", "555-3333"]
        for i, phone in enumerate(phones):
            add_contact(self.contacts_dict, self.phone_set, f"Contact{i}", phone)
        
        # Verify set has no duplicates
        self.assertEqual(len(self.phone_set), len(phones))
        self.assertEqual(len(self.phone_set), len(set(self.phone_set)))


class TestBatchOperations(unittest.TestCase):
    """Test batch operations using comprehensions"""
    
    def test_batch_create_dict_comprehension(self):
        """Test batch creating contacts using dict comprehension"""
        data = [
            ("Alice", "555-1111", "alice@example.com", "123 St"),
            ("Bob", "555-2222", "bob@example.com", "456 Ave"),
        ]
        batch_dict = batch_create_contacts(data)
        self.assertEqual(len(batch_dict), 2)
        self.assertIn("555-1111", batch_dict)
        self.assertEqual(batch_dict["555-1111"]["name"], "Alice")
    
    def test_find_duplicate_names(self):
        """Test finding duplicate names using nested comprehensions"""
        contacts_dict, phone_set = create_contact_book()
        add_contact(contacts_dict, phone_set, "John", "555-1111")
        add_contact(contacts_dict, phone_set, "John", "555-2222")
        add_contact(contacts_dict, phone_set, "Alice", "555-3333")
        
        duplicates = find_duplicate_names(contacts_dict)
        self.assertIn("John", duplicates)
        self.assertEqual(len(duplicates["John"]), 2)


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()
