"""
================================================================================
EXPERIMENT 8: CIRCULAR LINKED LIST: INSERTION, DELETION, DISPLAY
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To write and execute a Python program to implement a Circular Singly
    Linked List supporting insertion at the beginning and end, deletion of
    nodes by value, and traversing/displaying the circular chain.

TECHNICAL SPECIFICATIONS:
    - Data Structure           : Circular Singly Linked List (Ring Topology)
    - Node Pointers            : The last node's `next` pointer references `head`
    - Time Complexities        :
        * Insert at Beginning  : O(n) (traversal to update last node)
        * Insert at End        : O(n) (traversal to link last node to new node)
        * Deletion by Value    : O(n)
        * Traversal / Display  : O(n)
    - Auxiliary Space          : O(n)
================================================================================
"""

# Circular Linked List: Insertion, Deletion, Display

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        node = Node(data)
        if self.head is None:
            node.next = node                # points to itself
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            node.next = self.head
            last.next = node
        self.head = node
        print("Inserted at beginning.")

    def insert_end(self, data):
        node = Node(data)
        if self.head is None:
            node.next = node
            self.head = node
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = node
            node.next = self.head
        print("Inserted at end.")

    def delete(self, data):
        if self.head is None:
            print("List is empty.")
            return
        # only one node in the list
        if self.head.next == self.head:
            if self.head.data == data:
                self.head = None
                print("Deleted successfully.")
            else:
                print("Value not found.")
            return
        # deleting the head node
        if self.head.data == data:
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head
            print("Deleted successfully.")
            return
        # deleting any other node
        prev = self.head
        while prev.next != self.head and prev.next.data != data:
            prev = prev.next
        if prev.next == self.head:
            print("Value not found.")
        else:
            prev.next = prev.next.next
            print("Deleted successfully.")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

# Main program
cll = CircularLinkedList()

while True:
    print("\n--- CIRCULAR LINKED LIST OPERATIONS ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        cll.insert_begin(input("Enter value: "))
    elif choice == "2":
        cll.insert_end(input("Enter value: "))
    elif choice == "3":
        cll.delete(input("Enter value to delete: "))
    elif choice == "4":
        cll.display()
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Try again.")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
--- CIRCULAR LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 1
Enter value: 10
Inserted at beginning.

--- CIRCULAR LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 2
Enter value: 20
Inserted at end.

--- CIRCULAR LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 4
10 -> 20 -> (back to head)

--- CIRCULAR LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 3
Enter value to delete: 10
Deleted successfully.

--- CIRCULAR LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 4
20 -> (back to head)

--- CIRCULAR LINKED LIST OPERATIONS ---
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit
Enter your choice: 5
Program ended.
================================================================================
"""
