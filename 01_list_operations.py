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

# Experiment 1: List Operations (Insertion, Deletion and Display)
a = []

n = int(input("How many elements? "))
for i in range(n):
    x = int(input(f"Enter element {i + 1}: "))
    a.append(x)

while True:
    print("\n--- MENU ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        pos = int(input("Enter position (1-based): "))
        value = int(input("Enter value: "))
        if 1 <= pos <= len(a) + 1:
            a.insert(pos - 1, value)
            print(f"Inserted {value} at position {pos}.")
        else:
            print("Invalid position!")

    elif choice == 2:
        pos = int(input("Enter position to delete (1-based): "))
        if 1 <= pos <= len(a):
            removed = a.pop(pos - 1)
            print(f"Deleted {removed} from position {pos}.")
        else:
            print("Invalid position!")

    elif choice == 3:
        print("Current List:", a)

    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please select 1-4.")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
How many elements? 2
Enter element 1: 1
Enter element 2: 2

--- MENU ---
1. Insert
2. Delete
3. Display
4. Exit
Enter choice: 1
Enter position (1-based): 1
Enter value: 2
Inserted 2 at position 1.

--- MENU ---
1. Insert
2. Delete
3. Display
4. Exit
Enter choice: 1
Enter position (1-based): 2
Enter value: 1
Inserted 1 at position 2.

--- MENU ---
1. Insert
2. Delete
3. Display
4. Exit
Enter choice: 1
Enter position (1-based): 3
Enter value: 4
Inserted 4 at position 3.

--- MENU ---
1. Insert
2. Delete
3. Display
4. Exit
Enter choice: 3
Current List: [2, 1, 4, 1, 2]

--- MENU ---
1. Insert
2. Delete
3. Display
4. Exit
Enter choice: 2
Enter position to delete (1-based): 1
Deleted 2 from position 1.

--- MENU ---
1. Insert
2. Delete
3. Display
4. Exit
Enter choice: 3
Current list: [1, 4, 1, 2]

--- MENU ---
1. Insert
2. Delete
3. Display
4. Exit
Enter choice: 4
Exiting...
================================================================================
"""
