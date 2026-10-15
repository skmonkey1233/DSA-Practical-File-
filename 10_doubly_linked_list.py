"""
================================================================================
EXPERIMENT 10: DOUBLY LINKED LIST OPERATIONS (INSERT, DELETE, DISPLAY)
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To implement a Doubly Linked List with operations: inserting a node at the end, deleting a node by value, and displaying nodes in forward sequence.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Doubly Linked List
    - Time Complexity           : Insert End: O(n), Delete: O(n), Display: O(n)
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Experiment 10: Doubly Linked List (Insert, Delete, Display)
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = None

while True:
    print("\n--- DOUBLY LINKED LIST MENU ---")
    print("1. Insert at end")
    print("2. Delete by value")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter value to insert: "))
        new_node = Node(x)
        if head is None:
            head = new_node
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        print(f"Node {x} inserted at end.")

    elif choice == 2:
        x = int(input("Enter value to delete: "))
        temp = head
        while temp is not None and temp.data != x:
            temp = temp.next

        if temp is None:
            print("Value not found in list!")
        else:
            if temp.prev is None:
                head = temp.next
                if head is not None:
                    head.prev = None
            else:
                temp.prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
            print(f"Deleted {x} from doubly linked list.")

    elif choice == 3:
        if head is None:
            print("List is empty.")
        else:
            print("Doubly Linked List:", end=" ")
            temp = head
            while temp is not None:
                print(temp.data, end=" <-> ")
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
--- DOUBLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 1
Enter value to insert: 2
Node 2 inserted at end.

--- DOUBLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 1
Enter value to insert: 4
Node 4 inserted at end.

--- DOUBLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 1
Enter value to insert: 6
Node 6 inserted at end.

--- DOUBLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 3
Doubly Linked List: 2 <-> 4 <-> 6 <-> None

--- DOUBLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 2
Enter value to delete: 4
Deleted 4 from doubly linked list.

--- DOUBLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 3
Doubly Linked List: 2 <-> 6 <-> None

--- DOUBLY LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 4
Exiting...
================================================================================
"""
