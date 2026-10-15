"""
================================================================================
EXPERIMENT 7: CIRCULAR LINKED LIST OPERATIONS (INSERT, DELETE, DISPLAY)
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To implement a Circular Singly Linked List with operations: inserting a node at the end, deleting a node by value, and displaying the circular structure.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Circular Singly Linked List
    - Time Complexity           : Insert End: O(n), Delete: O(n), Display: O(n)
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Experiment 7: Circular Linked List (Insert, Delete, Display)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

last = None

while True:
    print("\n--- CIRCULAR LINKED LIST MENU ---")
    print("1. Insert at end")
    print("2. Delete by value")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        new_node = Node(value)
        if last is None:
            last = new_node
            new_node.next = new_node
        else:
            new_node.next = last.next
            last.next = new_node
            last = new_node
        print(f"Node {value} inserted at end.")

    elif choice == 2:
        value = int(input("Enter value to delete: "))
        if last is None:
            print("List is empty!")
        else:
            current = last.next
            previous = last
            found = False
            while True:
                if current.data == value:
                    found = True
                    if current == last and current.next == current:
                        last = None
                    else:
                        previous.next = current.next
                        if current == last:
                            last = previous
                    print(f"Deleted {value} from circular list.")
                    break
                previous = current
                current = current.next
                if current == last.next:
                    break
            if not found:
                print("Value not found in circular list!")

    elif choice == 3:
        if last is None:
            print("Circular Linked List is empty.")
        else:
            print("Circular Linked List:", end=" ")
            temp = last.next
            while True:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == last.next:
                    break
            print("(head)")

    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
--- CIRCULAR LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 1
Enter value to insert: 8
Node 8 inserted at end.

--- CIRCULAR LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 1
Enter value to insert: 7
Node 7 inserted at end.

--- CIRCULAR LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 1
Enter value to insert: 4
Node 4 inserted at end.

--- CIRCULAR LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 3
Circular Linked List: 8 -> 7 -> 4 -> (head)

--- CIRCULAR LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 2
Enter value to delete: 8
Deleted 8 from circular list.

--- CIRCULAR LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 3
Circular Linked List: 7 -> 4 -> (head)

--- CIRCULAR LINKED LIST MENU ---
1. Insert at end
2. Delete by value
3. Display
4. Exit
Enter choice: 4
Exiting...

** Process exited - Return Code: 0 **
================================================================================
"""
