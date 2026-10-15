"""
================================================================================
EXPERIMENT 6: SINGLY LINKED LIST OPERATIONS (INSERT, DELETE, DISPLAY)
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To implement a Singly Linked List with operations: inserting a node at the end, deleting a node by value, and displaying all nodes.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Singly Linked List
    - Time Complexity           : Insert End: O(n), Delete: O(n), Display: O(n)
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Experiment 6: Singly Linked List (Insert, Delete, Display)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

while True:
    print("\n--- SINGLY LINKED LIST MENU ---")
    print("1. Insert at end")
    print("2. Delete by value")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        new_node = Node(value)
        if head is None:
            head = new_node
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        print(f"Node {value} inserted at end.")

    elif choice == 2:
        value = int(input("Enter value to delete: "))
        if head is None:
            print("List is empty!")
        elif head.data == value:
            head = head.next
            print(f"Deleted {value} from head.")
        else:
            temp = head
            while temp.next is not None and temp.next.data != value:
                temp = temp.next
            if temp.next is not None:
                temp.next = temp.next.next
                print(f"Deleted {value} from list.")
            else:
                print("Value not found in list!")

    elif choice == 3:
        if head is None:
            print("List is empty.")
        else:
            print("Linked List:", end=" ")
            temp = head
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
--- SINGLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 1
Enter value to insert: 7
Node 7 inserted at end.

--- SINGLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 1
Enter value to insert: 9
Node 9 inserted at end.

--- SINGLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 1
Enter value to insert: 5
Node 5 inserted at end.

--- SINGLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 3
Linked List: 7 -> 9 -> 5 -> None

--- SINGLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 2
Enter value to delete: 9
Deleted 9 from list.

--- SINGLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 3
Linked List: 7 -> 5 -> None

--- SINGLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 4
Exiting...

** Process exited - Return Code: 0 **
================================================================================
"""
