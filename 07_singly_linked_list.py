"""
================================================================================
EXPERIMENT 7: SINGLY LINKED LIST: INSERTION, DELETION, DISPLAY
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To write and execute a Python program to implement a Singly Linked List
    supporting insertion at the beginning and end, deletion of a node by value,
    and displaying the contents of the list.

TECHNICAL SPECIFICATIONS:
    - Data Structure           : Singly Linked List (Dynamic Node Structure)
    - Node Fields              : `data` (payload), `next` (pointer to succeeding node)
    - Time Complexities        :
        * Insert at Beginning  : O(1)
        * Insert at End        : O(n)
        * Deletion by Value    : O(n)
        * Traversal / Display  : O(n)
    - Auxiliary Space          : O(n)
================================================================================
"""

# Singly Linked List: Insertion, Deletion, Display

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        print("Inserted at beginning.")

    def insert_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        print("Inserted at end.")

    def delete(self, data):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.data == data:
            self.head = self.head.next
            print("Deleted successfully.")
            return
        temp = self.head
        while temp.next and temp.next.data != data:
            temp = temp.next
        if temp.next is None:
            print("Value not found.")
        else:
            temp.next = temp.next.next
            print("Deleted successfully.")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Main program
ll = LinkedList()

while True:
    print("\n--- LINKED LIST OPERATIONS ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        ll.insert_begin(input("Enter value: "))
    elif choice == "2":
        ll.insert_end(input("Enter value: "))
    elif choice == "3":
        ll.delete(input("Enter value to delete: "))
    elif choice == "4":
        ll.display()
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Try again.")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
--- LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 1
Enter value: 45
Inserted at beginning.

--- LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 2
Enter value: 68
Inserted at end.

--- LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 4
45 -> 68 -> None

--- LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 1
Enter value: 58
Inserted at beginning.

--- LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 2
Enter value: 97
Inserted at end.

--- LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 3
Enter value to delete: 0
Value not found.

--- LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 4
58 -> 45 -> 68 -> 97 -> None

--- LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 3
Enter value to delete: 68
Deleted successfully.

--- LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 4
58 -> 45 -> 97 -> None

--- LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 5
Program ended.
================================================================================
"""
