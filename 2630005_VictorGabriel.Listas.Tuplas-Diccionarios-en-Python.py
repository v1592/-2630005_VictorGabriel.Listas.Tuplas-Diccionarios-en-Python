# =============================================================================
# COVER PAGE
# =============================================================================
# Name:      VICTOR GABRIEL HERNANDEZ LUGO
# Student ID: 263005
# Topic:     Collections in Python: lists, tuples and dictionaries
# GitHub:    https://github.com/v1592/2630005_VictorGabriel_strings.py
# =============================================================================

# =============================================================================
# EXECUTIVE SUMMARY
# =============================================================================
# A list is an ordered and mutable collection: items can be added, removed or
# changed after it is created. A tuple is also ordered but immutable, so it
# is used for data that must not change, such as coordinates. A dictionary
# (dict) stores key-value pairs and finds a value quickly by its key, for
# example a product name -> its price. Mutable means the object can be
# modified in place (append(), pop()); immutable means any change requires
# creating a new object. This document contains 6 problems: shopping list
# (list), points and distances (tuple), product catalog (dict), student
# grades (dict of lists), word frequency counter (list + dict) and a contact
# book (dict CRUD). Each one documents its inputs, outputs, validations and 3
# test cases (normal, border, error).

# =============================================================================
# PRINCIPLES AND GOOD PRACTICES
# =============================================================================
# - Use lists when items must be added or removed frequently.
# - Use tuples for data that should not change (coordinates, dates, settings).
# - Use dictionaries when information must be searched by a key (name, id).
# - Avoid modifying a list while looping over it with a for loop.
# - Use descriptive dictionary keys and variable names.
# - Write readable code and clear messages for the user.

import math

# Constants (UPPER_SNAKE_CASE)
ERROR_MESSAGE = "Error: invalid input"
PASSING_GRADE = 70.0
PUNCTUATION_MARKS = ".,;:!?"

# Product catalog for Problem 3 (key: product name, value: unit price)
PRODUCT_PRICES = {
    "apple": 10.0,
    "banana": 5.5,
    "orange": 8.0,
    "milk": 22.0,
}

# Student grades for Problem 4 (key: student name, value: list of grades)
STUDENT_GRADES = {
    "Alice": [90.0, 85.0, 100.0],
    "Bob": [60.0, 70.0, 65.0],
    "Carlos": [60.0, 80.0],
    "Dana": [],  # student with no grades yet (used to test an empty list)
}

# Initial contacts for Problem 6 (key: contact name, value: phone string)
INITIAL_CONTACTS = {
    "Alice": "1234567890",
    "Bob": "5559876543",
}


# -----------------------------------------------------------------------------
# Helper functions (shared by all problems)
# -----------------------------------------------------------------------------
def parse_float(value):
    """Convert value to a finite float, or return None if it is not possible."""
    try:
        number = float(str(value).strip())
    except ValueError:
        return None
    if not math.isfinite(number):  # rejects nan and inf
        return None
    return number


def parse_int(value):
    """Convert value to int, or return None. '3.5' is NOT a valid integer."""
    try:
        return int(str(value).strip())
    except ValueError:
        return None


def bool_text(flag):
    """Show a bool as 'true' or 'false' (lowercase)."""
    return str(flag).lower()


# =============================================================================
# Problem 1: Shopping list basics (list operations)
# =============================================================================
# Description: Builds a list of products from a comma-separated text, adds a
#   new product at the end, shows the total of items and checks if a product
#   is in the list (boolean is_in_list).
#
# Inputs:
# - initial_items_text (string, e.g. "apple,banana,orange")
# - new_item (string), search_item (string)
#
# Outputs:
# - "Items list: <items_list>", "Total items: <n>", "Found item: true|false"
#
# Validations:
# - initial_items_text not empty after strip().
# - Each item is cleaned with strip() and lower(); empty pieces (such as the
#   one between "a,,b") are ignored.
# - new_item and search_item not empty.
# - Design decision: an initial list with NO valid items is an error.
#
# Test cases:
# 1) Normal: " apple, banana ,orange", "grape", "banana" ->
#            Items list: ['apple', 'banana', 'orange', 'grape'],
#            Total items: 4, Found item: true
# 2) Border: "apple,,banana", "pear", "kiwi" -> the extra comma is ignored:
#            ['apple', 'banana', 'pear'], Total items: 3, Found item: false
# 3) Error:  "   ", "grape", "apple" -> Error: invalid input

def build_shopping_list(initial_items_text, new_item, search_item):
    """Return (items_list, is_in_list) or None if the input is invalid."""
    if initial_items_text.strip() == "":
        return None
    new_item = new_item.strip().lower()
    search_item = search_item.strip().lower()
    if new_item == "" or search_item == "":
        return None
    items_list = []
    for piece in initial_items_text.split(","):
        clean_piece = piece.strip().lower()
        if clean_piece != "":
            items_list.append(clean_piece)
    if len(items_list) == 0:
        return None
    items_list.append(new_item)
    is_in_list = search_item in items_list
    return items_list, is_in_list


def run_problem_1(initial_items_text, new_item, search_item):
    print(f'Input: "{initial_items_text}", "{new_item}", "{search_item}"')
    result = build_shopping_list(initial_items_text, new_item, search_item)
    if result is None:
        print(ERROR_MESSAGE)
        return
    items_list, is_in_list = result
    print(f"Items list: {items_list}")
    print(f"Total items: {len(items_list)}")
    print(f"Found item: {bool_text(is_in_list)}")


# =============================================================================
# Problem 2: Points and distances with tuples
# =============================================================================
# Description: Represents two points of a 2D plane as tuples, calculates the
#   Euclidean distance between them and builds a new tuple with the midpoint.
#
# Inputs:
# - x1, y1, x2, y2 (float)
#
# Outputs:
# - "Point A: (x1, y1)", "Point B: (x2, y2)", "Distance: <distance>",
#   "Midpoint: (mx, my)"
#
# Validations:
# - The four values must be convertible to float (no extra range limits).
#
# Test cases:
# 1) Normal: (0, 0) and (3, 4) -> Distance: 5.00, Midpoint: (1.5, 2.0)
# 2) Border: (2, 2) and (2, 2) (same point) -> Distance: 0.00,
#            Midpoint: (2.0, 2.0)
# 3) Error:  x1 = "abc" -> Error: invalid input

def calculate_points(x1_text, y1_text, x2_text, y2_text):
    """Return (point_a, point_b, distance, midpoint) or None if invalid."""
    x1 = parse_float(x1_text)
    y1 = parse_float(y1_text)
    x2 = parse_float(x2_text)
    y2 = parse_float(y2_text)
    if x1 is None or y1 is None or x2 is None or y2 is None:
        return None
    point_a = (x1, y1)  # tuples: the coordinates must not change
    point_b = (x2, y2)
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
    return point_a, point_b, distance, midpoint


def run_problem_2(x1_text, y1_text, x2_text, y2_text):
    print(f"Input: ({x1_text}, {y1_text}) and ({x2_text}, {y2_text})")
    result = calculate_points(x1_text, y1_text, x2_text, y2_text)
    if result is None:
        print(ERROR_MESSAGE)
        return
    point_a, point_b, distance, midpoint = result
    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance:.2f}")
    print(f"Midpoint: {midpoint}")


# =============================================================================
# Problem 3: Product catalog with dictionary
# =============================================================================
# Description: Uses the dictionary PRODUCT_PRICES (name -> unit price). Given
#   a product name and a quantity, it calculates the total to pay if the
#   product exists; otherwise it shows an error.
#
# Inputs:
# - product_name (string), quantity (int)
#
# Outputs:
# - If it exists: "Unit price: ...", "Quantity: ...", "Total: ..."
# - If it does not exist: "Error: product not found"
#
# Validations:
# - quantity > 0 and product_name not empty after strip().
# - The name is normalized with strip() and lower() before using the key.
# - The key is checked with "in" before accessing the dictionary.
#
# Test cases:
# 1) Normal: "apple", 3 -> Unit price: 10.00, Quantity: 3, Total: 30.00
# 2) Border: "  MILK ", 1 (spaces, capitals and the minimum quantity) ->
#            Unit price: 22.00, Quantity: 1, Total: 22.00
# 3) Error:  "pizza", 2 -> Error: product not found;
#            "apple", 0 -> Error: invalid input

def calculate_purchase(product_name, quantity_text):
    """Return (unit_price, quantity, total) or an error string."""
    product_key = product_name.strip().lower()
    quantity = parse_int(quantity_text)
    if product_key == "" or quantity is None or quantity <= 0:
        return ERROR_MESSAGE
    if product_key not in PRODUCT_PRICES:
        return "Error: product not found"
    unit_price = PRODUCT_PRICES[product_key]
    return unit_price, quantity, unit_price * quantity


def run_problem_3(product_name, quantity_text):
    print(f'Input: "{product_name}", {quantity_text}')
    result = calculate_purchase(product_name, quantity_text)
    if isinstance(result, str):  # an error message
        print(result)
        return
    unit_price, quantity, total_price = result
    print(f"Unit price: {unit_price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total_price:.2f}")


# =============================================================================
# Problem 4: Student grades with dict and list
# =============================================================================
# Description: Uses the dictionary STUDENT_GRADES (name -> list of grades).
#   Given a student name, it shows the grades, the average and the boolean
#   is_passed (average >= 70.0).
#
# Inputs:
# - student_name (string)
#
# Outputs:
# - If it exists: "Grades: [...]", "Average: ...", "Passed: true|false"
# - If it does not exist: "Error: student not found"
#
# Validations:
# - student_name not empty after strip(); it is normalized with title().
# - The name must be a key of the dictionary.
# - The grades list must not be empty before calculating the average.
#
# Test cases:
# 1) Normal: "alice" -> Grades [90.0, 85.0, 100.0], Average 91.67,
#            Passed: true; "Bob" -> Average 65.00, Passed: false
# 2) Border: "Carlos" -> Grades [60.0, 80.0], Average 70.00 (exactly the
#            limit), Passed: true; "Dana" (empty list) -> Error: no grades
# 3) Error:  "Zoe" -> Error: student not found; "  " -> Error: invalid input

def calculate_student_average(student_name):
    """Return (grades_list, average, is_passed) or an error string."""
    student_key = student_name.strip().title()
    if student_key == "":
        return ERROR_MESSAGE
    if student_key not in STUDENT_GRADES:
        return "Error: student not found"
    grades_list = STUDENT_GRADES[student_key]
    if len(grades_list) == 0:  # avoids dividing by zero
        return "Error: no grades available"
    average = sum(grades_list) / len(grades_list)
    is_passed = average >= PASSING_GRADE
    return grades_list, average, is_passed


def run_problem_4(student_name):
    print(f'Input: "{student_name}"')
    result = calculate_student_average(student_name)
    if isinstance(result, str):
        print(result)
        return
    grades_list, average, is_passed = result
    print(f"Grades: {grades_list}")
    print(f"Average: {average:.2f}")
    print(f"Passed: {bool_text(is_passed)}")


# =============================================================================
# Problem 5: Word frequency counter (list + dict)
# =============================================================================
# Description: Converts a sentence to lowercase, removes simple punctuation,
#   splits it into a list of words and builds a dictionary of frequencies.
#   It also finds the most common word.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - "Words list: [...]", "Frequencies: {...}", "Most common word: <word>"
#
# Validations:
# - sentence not empty after strip().
# - Design decision: the marks . , ; : ! ? are removed with replace().
# - The list of words must not be empty (e.g. a sentence with only marks).
# - In a tie, the word that appeared first is shown.
#
# Test cases:
# 1) Normal: "The cat and the hat and the bat" -> the: 3, and: 2, cat: 1,
#            hat: 1, bat: 1; Most common word: the
# 2) Border: "Hello, hello! HELLO." -> {'hello': 3} (case and punctuation
#            ignored), Most common word: hello
# 3) Error:  "   " or "?!.," (no words left) -> Error: invalid input

def count_word_frequencies(sentence):
    """Return (words_list, freq_dict, most_common_word) or None if invalid."""
    clean_sentence = sentence.strip().lower()
    if clean_sentence == "":
        return None
    for mark in PUNCTUATION_MARKS:
        clean_sentence = clean_sentence.replace(mark, "")
    words_list = clean_sentence.split()
    if len(words_list) == 0:
        return None
    freq_dict = {}
    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    most_common_word = words_list[0]
    for word in freq_dict:  # dicts keep insertion order
        if freq_dict[word] > freq_dict[most_common_word]:
            most_common_word = word
    return words_list, freq_dict, most_common_word


def run_problem_5(sentence):
    print(f'Input: "{sentence}"')
    result = count_word_frequencies(sentence)
    if result is None:
        print(ERROR_MESSAGE)
        return
    words_list, freq_dict, most_common_word = result
    print(f"Words list: {words_list}")
    print(f"Frequencies: {freq_dict}")
    print(f"Most common word: {most_common_word}")


# =============================================================================
# Problem 6: Simple contact book (dictionary CRUD)
# =============================================================================
# Description: A contact book stored in a dictionary (name -> phone).
#   Depending on the action it adds/updates (ADD), searches (SEARCH) or
#   deletes (DELETE) a contact and shows the result.
#
# Inputs:
# - action_text ("ADD", "SEARCH" or "DELETE"), name (string),
#   phone (string, only for ADD)
#
# Outputs:
# - ADD: "Contact saved: <name>, <phone>"
# - SEARCH: "Phone: <phone>" or "Error: contact not found"
# - DELETE: "Contact deleted: <name>" or "Error: contact not found"
#
# Validations:
# - action_text is normalized with strip() and upper(), and must be one of
#   the three actions.
# - name not empty after strip(); it is normalized with title().
# - For ADD, phone not empty after strip().
#
# Test cases (they run in order on the same contact book):
# 1) Normal: ADD "bob smith" "5551234567" -> Contact saved: Bob Smith, ...;
#            SEARCH "Bob Smith" -> Phone: 5551234567
# 2) Border: ADD "Alice" "0000000000" (the name already exists, so the
#            phone is UPDATED); DELETE "Bob Smith" -> Contact deleted
# 3) Error:  "UPDATE" (invalid action) / SEARCH "Zed" (not found) /
#            ADD "Eve" with an empty phone -> error messages

def contact_action(contacts, action_text, name, phone=""):
    """Run one action on the contacts dict and return the message to show."""
    action = action_text.strip().upper()
    contact_name = name.strip().title()
    contact_phone = phone.strip()
    if action not in ("ADD", "SEARCH", "DELETE"):
        return ERROR_MESSAGE
    if contact_name == "":
        return ERROR_MESSAGE
    if action == "ADD":
        if contact_phone == "":
            return ERROR_MESSAGE
        contacts[contact_name] = contact_phone  # adds or updates
        return f"Contact saved: {contact_name}, {contact_phone}"
    if action == "SEARCH":
        found_phone = contacts.get(contact_name)
        if found_phone is None:
            return "Error: contact not found"
        return f"Phone: {found_phone}"
    # Only DELETE is left here
    if contact_name not in contacts:
        return "Error: contact not found"
    contacts.pop(contact_name)
    return f"Contact deleted: {contact_name}"


def run_problem_6(contacts, action_text, name, phone=""):
    print(f'Input: action="{action_text}", name="{name}", phone="{phone}"')
    print(contact_action(contacts, action_text, name, phone))


# =============================================================================
# TEST RUNNER
# =============================================================================
def print_title(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main():
    print_title("Problem 1: Shopping list basics")
    run_problem_1(" apple, banana ,orange", "grape", "banana")  # normal
    run_problem_1("apple,,banana", "pear", "kiwi")              # border
    run_problem_1("   ", "grape", "apple")                      # error

    print_title("Problem 2: Points and distances with tuples")
    run_problem_2("0", "0", "3", "4")      # normal
    run_problem_2("2", "2", "2", "2")      # border (same point)
    run_problem_2("-1", "-1", "1", "1")    # border (negative coordinates)
    run_problem_2("abc", "0", "3", "4")    # error

    print_title("Problem 3: Product catalog with dictionary")
    run_problem_3("apple", "3")            # normal
    run_problem_3("  MILK ", "1")          # border
    run_problem_3("pizza", "2")            # error (not found)
    run_problem_3("apple", "0")            # error (quantity)

    print_title("Problem 4: Student grades with dict and list")
    run_problem_4("alice")                 # normal (passed)
    run_problem_4("Bob")                   # normal (not passed)
    run_problem_4("Carlos")                # border (average exactly 70)
    run_problem_4("Dana")                  # border (empty grades list)
    run_problem_4("Zoe")                   # error (not found)
    run_problem_4("  ")                    # error (empty)

    print_title("Problem 5: Word frequency counter")
    run_problem_5("The cat and the hat and the bat")  # normal
    run_problem_5("Hello, hello! HELLO.")             # border
    run_problem_5("   ")                              # error
    run_problem_5("?!.,")                             # error (only marks)

    print_title("Problem 6: Simple contact book")
    contacts = dict(INITIAL_CONTACTS)  # copy, so the constant is not changed
    run_problem_6(contacts, "add", "bob smith", "5551234567")  # normal
    run_problem_6(contacts, "SEARCH", "Bob Smith")             # normal
    run_problem_6(contacts, "ADD", "Alice", "0000000000")      # border (update)
    run_problem_6(contacts, "DELETE", "Bob Smith")             # border
    run_problem_6(contacts, "UPDATE", "Alice")                 # error (action)
    run_problem_6(contacts, "SEARCH", "Zed")                   # error (missing)
    run_problem_6(contacts, "ADD", "Eve", "  ")                # error (phone)
    print(f"Final contacts: {contacts}")


if __name__ == "__main__":
    main()


# =============================================================================
# CONCLUSIONS
# =============================================================================
# Lists are the best option when items must be added or removed, because
# methods like append() make that easy. Tuples are useful for data that must
# not change, such as the coordinates of a point. Dictionaries make searches
# fast: instead of looping through everything, the key gives the value
# directly, as in the catalog and the contact book. A common pattern I found
# was combining them, for example a dictionary whose values are lists
# (student -> grades). I also learned to validate before using an index or a
# key, and to check for empty lists before dividing to calculate an average.

# =============================================================================
# REFERENCES
# =============================================================================
# References:
# 1) Python documentation - Built-in Types: list, tuple, dict
#    https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# 2) Python documentation - Mapping Types - dict
#    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# 3) Python Tutorial - Data Structures (lists, tuples, dictionaries)
#    https://docs.python.org/3/tutorial/datastructures.html
# 4) Python documentation - Built-in Functions: sum(), min(), max(), sorted()
#    https://docs.python.org/3/library/functions.html
# 5) Real Python - Lists and Tuples in Python
#    https://realpython.com/python-lists-tuples/
# 6) Real Python - Dictionaries in Python
#    https://realpython.com/python-dicts/
