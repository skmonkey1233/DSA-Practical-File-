"""
================================================================================
EXPERIMENT 1: LIST OPERATIONS (INSERTION, DELETION AND DISPLAY)
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To write and execute a Python program to perform basic operations on a list: inserting an element at a specified position, deleting an element by position, and displaying the list contents.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Dynamic Array / Python List
    - Time Complexity           : Insert: O(n), Delete: O(n), Display: O(n)
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Simple program for list operations: Insertion, Deletion, Display

my_list = []

def insert():
    value = input("Enter value to insert: ")
    pos = input("Enter position (press Enter to add at end): ")
    if pos == "":
        my_list.append(value)
    else:
        my_list.insert(int(pos), value)
    print("Inserted successfully.")

def delete():
    if not my_list:
        print("List is empty. Nothing to delete.")
        return
    value = input("Enter value to delete: ")
    if value in my_list:
        my_list.remove(value)
        print("Deleted successfully.")
    else:
        print("Value not found in the list.")

def display():
    if not my_list:
        print("List is empty.")
    else:
        print("List elements:", my_list)

while True:
    print("\n--- LIST OPERATIONS ---")
    print("1. Insertion")
    print("2. Deletion")
    print("3. Display")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        insert()
    elif choice == "2":
        delete()
    elif choice == "3":
        display()
    elif choice == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Try again.")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
--- LIST OPERATIONS ---
1. Insertion
2. Deletion
3. Display
4. Exit
Enter your choice: 1
Enter value to insert: 4
Enter position (press Enter to add at end): 1
Inserted successfully.

--- LIST OPERATIONS ---
1. Insertion
2. Deletion
3. Display
4. Exit
Enter your choice: 1
Enter value to insert: 5
Enter position (press Enter to add at end): 2
Inserted successfully.

--- LIST OPERATIONS ---
1. Insertion
2. Deletion
3. Display
4. Exit
Enter your choice: 1
Enter value to insert: 7
Enter position (press Enter to add at end): 3
Inserted successfully.

--- LIST OPERATIONS ---
1. Insertion
2. Deletion
3. Display
4. Exit
Enter your choice: 3
List elements: ['4', '5', '7']

--- LIST OPERATIONS ---
1. Insertion
2. Deletion
3. Display
4. Exit
Enter your choice: 2
Enter value to delete: 5
Deleted successfully.

--- LIST OPERATIONS ---
1. Insertion
2. Deletion
3. Display
4. Exit
Enter your choice: 3
List elements: ['4', '7']

--- LIST OPERATIONS ---
1. Insertion
2. Deletion
3. Display
4. Exit
Enter your choice: 4
Program ended.
================================================================================
"""
