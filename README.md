# Contact Book CLI Application

A command-line contact management system that allows you to add, search, update, and delete contacts using **only fundamental Python data structures**: lists, tuples, dictionaries, sets, and comprehensions.

## Features

✨ **Core Features:**
- **Add Contacts** - Add new contacts with name, phone, email, and address
- **Search Contacts** - Search by name or phone number
- **Update Contacts** - Modify existing contact information including phone numbers
- **Delete Contacts** - Remove contacts with confirmation
- **List All Contacts** - View all contacts at once
- **View Details** - See complete information for a specific contact
- **Statistics** - View contact book statistics

🛡️ **Duplicate Detection:**
- Uses Python **sets** to track phone numbers
- Prevents duplicate phone numbers from being added
- Warns users if they try to create a duplicate entry
- O(1) lookup time for duplicate checking

📚 **Data Structures Used:**
- **Dictionaries**: Store contact data and manage contact collection
- **Sets**: Detect and prevent duplicate phone numbers
- **Lists**: Return search results and all contacts
- **Tuples**: Convert contacts for compact storage
- **Comprehensions**: Filter and transform data efficiently

## Project Structure

```
Contact Book/
├── contact_book.py       # Main CLI application (functions-based)
├── contacts.py           # Core functions using data structures only
├── demo.py               # Demonstration with examples
├── test_contact_book.py  # Unit tests (35+ test cases)
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

## How to Run

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Running the Application

1. Open a terminal/command prompt
2. Navigate to the project directory:
   ```bash
   cd "c:\Users\harsh\Documents\4 th lab manual\New folder"
   ```

3. Run the application:
   ```bash
   python contact_book.py
   ```

4. Follow the on-screen menu to manage your contacts

### Running the Demo

See examples of how the contact book works:
```bash
python demo.py
```

### Running Tests

Execute all unit tests:
```bash
python -m unittest test_contact_book.py -v
```

## Usage Examples

### Adding a Contact
1. Select option **1** from the menu
2. Enter contact name: `John Doe`
3. Enter phone number: `555-1234`
4. Enter email (optional): `john@example.com`
5. Enter address (optional): `123 Main St`

### Searching for a Contact
1. Select option **2** from the menu
2. Enter search term (name or phone): `John` or `555-1234`
3. View all matching results

### Updating a Contact
1. Select option **3** from the menu
2. Enter the phone number of the contact to update
3. Leave fields blank to keep existing values
4. Enter new values for fields you want to change

### Deleting a Contact
1. Select option **4** from the menu
2. Enter the phone number of the contact to delete
3. Confirm the deletion

## Data Structure Design

### Core Structure: Tuple of (Dictionary, Set)
```python
contacts_dict, phone_set = create_contact_book()
```

**Contacts Dictionary:**
```python
contacts_dict = {
    "555-1234": {
        "name": "John Doe",
        "phone": "555-1234",
        "email": "john@example.com",
        "address": "123 Main St"
    },
    # ... more contacts
}
```

**Phone Set:**
```python
phone_set = {"555-1234", "555-5678", "555-9999"}  # For O(1) lookup
```

### Duplicate Detection Algorithm
```python
if phone in phone_set:
    return False, "Error: Phone number already exists!"
```

The set-based approach ensures:
- O(1) average lookup time for duplicate checking
- Memory-efficient storage
- Fast additions and deletions
- Automatic uniqueness enforcement

## Data Structures Explained

### 1. Dictionaries
Used for:
- **Contact storage**: `{phone: contact_dict}`
- **Contact data**: `{name, phone, email, address}`
- **Mappings**: `{phone: name}`, `{phone: [list of properties]}`

Example:
```python
contact = {
    "name": "Alice",
    "phone": "555-1111",
    "email": "alice@example.com",
    "address": "123 St"
}
```

### 2. Sets
Used for:
- **Duplicate phone detection**: `phone_set`
- **Unique values extraction**: `{contact['phone'] for contact in contacts}`
- **Finding differences**: Set operations (union, intersection, etc.)

Example:
```python
phone_set = {"555-1111", "555-2222", "555-3333"}
if "555-1111" in phone_set:  # O(1) check
    print("Already exists")
```

### 3. Lists
Used for:
- **Search results**: `[contact1, contact2, ...]`
- **All contacts**: `list(contacts_dict.values())`
- **Return values**: Most functions return lists

Example:
```python
results = [c for c in contacts if "john" in c["name"].lower()]
```

### 4. Tuples
Used for:
- **Immutable contact data**: `(name, phone, email, address)`
- **Return multiple values**: `(success, message)`
- **Batch data input**: `[(name, phone, email, address), ...]`

Example:
```python
contact_tuple = ("John", "555-1234", "john@example.com", "123 St")
```

### 5. Comprehensions

**List Comprehension:**
```python
# Search results
[c for c in contacts.values() 
 if query in c["name"].lower() or query in c["phone"]]

# Filter contacts with email
[c for c in contacts.values() if c["email"]]
```

**Dictionary Comprehension:**
```python
# Create phone-to-name mapping
{phone: contact["name"] for phone, contact in contacts.items()}

# Batch create contacts
{phone: create_contact(name, phone, email, addr) 
 for name, phone, email, addr in data}
```

**Set Comprehension:**
```python
# Extract all phone numbers
{contact["phone"] for contact in contacts.values()}

# Extract unique names
{contact["name"] for contact in contacts.values()}
```

**Tuple Comprehension:**
```python
# Get all names as tuple
tuple(c["name"] for c in contacts.values())
```

## Core Functions

### Data Structure Creation
- `create_contact_book()` - Returns `(dict, set)` tuple
- `create_contact()` - Returns contact dictionary

### CRUD Operations
- `add_contact()` - Add new contact with duplicate detection
- `search_contact()` - Search using list comprehension
- `get_contact_by_phone()` - Retrieve single contact
- `update_contact()` - Modify contact fields
- `delete_contact()` - Remove contact

### Data Queries
- `list_all_contacts()` - Get all contacts as list
- `get_all_names()` - Dict comprehension for names
- `get_contacts_with_email()` - List comprehension filter
- `get_phone_numbers_set()` - Set comprehension
- `find_duplicate_names()` - Nested comprehensions

## Sample Workflow

1. **Start application** → See main menu
2. **Add contact** → "John Doe" with phone "555-1234"
3. **Try to add duplicate** → Receives error message
4. **Search contacts** → Find by name or phone
5. **Update contact** → Change email or address
6. **View all contacts** → See summary list
7. **Delete contact** → Remove with confirmation
8. **View statistics** → See contact book stats
9. **Exit** → Close application

## Error Handling

The application handles:
- Empty input validation
- Duplicate phone number detection (using sets)
- Contact not found errors
- Invalid menu choices
- Confirmation for destructive operations
- Field-specific updates

## Performance Characteristics

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Add Contact | O(1) | Set insertion + dict assignment |
| Check Duplicate | O(1) | Set membership test |
| Search by Phone | O(1) | Dict lookup |
| Search by Name | O(n) | Linear scan through values |
| Update Contact | O(1) | Dict update |
| Delete Contact | O(1) | Set & dict removal |
| List All | O(n) | Iterate through values |

## Testing

The project includes **35+ unit tests** covering:
- Dictionary operations
- Set-based duplicate detection
- List comprehension searches
- Dict comprehension mappings
- Set comprehension extraction
- Tuple conversions
- Batch operations
- Error handling

Run tests:
```bash
python -m unittest test_contact_book.py -v
python -m unittest test_contact_book.py::TestComprehensions -v
```

## Key Concepts Demonstrated

✅ **Lists** - Dynamic sequences for search results
✅ **Tuples** - Immutable data storage and return values
✅ **Dictionaries** - Primary data structure for contacts
✅ **Sets** - Duplicate prevention and O(1) lookups
✅ **List Comprehensions** - Filtering and transformation
✅ **Dict Comprehensions** - Create mappings efficiently
✅ **Set Comprehensions** - Extract unique values
✅ **Tuple Unpacking** - Destructure contact data
✅ **Dictionary Methods** - `get()`, `items()`, `values()`
✅ **Set Operations** - `add()`, `remove()`, membership

## Future Enhancements

Potential improvements:
- Save/load from JSON or CSV (using comprehensions)
- Export contacts (using comprehensions)
- Contact grouping (nested dicts/lists)
- Advanced search filters (chained comprehensions)
- Batch operations (comprehensions)
- Data persistence (pickle, JSON)
- Contact history as list of tuples
- Statistics using aggregation comprehensions

## Learning Value

This project demonstrates:
- **No OOP required** - Solve problems with basic data structures
- **Functional programming** - Functions working with data
- **Data structure design** - Choosing right structures
- **Comprehensions** - Powerful and Pythonic transformations
- **Set operations** - Efficient duplicate detection
- **Dictionary patterns** - Key-value data management
- **Algorithm efficiency** - O(1) vs O(n) operations

## Notes

- **No classes used** - Only functions and basic data structures
- **Set-based efficiency** - O(1) duplicate checks vs O(n)
- **Pythonic code** - Uses comprehensions effectively
- **Error handling** - Returns (success, message) tuples
- **Type hints optional** - Can be added for clarity
- **Pure functions** - No side effects (except mutations of passed data structures)

## License

Open source - feel free to modify and use!

## Author

Created as a Python fundamentals project demonstrating effective use of lists, tuples, dictionaries, sets, and comprehensions.
