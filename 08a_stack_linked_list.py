"""
================================================================================
EXPERIMENT 8A: STACK IMPLEMENTATION USING LINKED LIST
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To implement a dynamically allocated Stack data structure using a Singly Linked List supporting Push, Pop, and Display operations.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Stack (LIFO) / Linked List
    - Time Complexity           : Push: O(1), Pop: O(1), Peek: O(1)
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Experiment 8A: Stack using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

top = None

while True:
    print("\n--- LINKED STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter value to push: "))
        new_node = Node(x)
        new_node.next = top
        top = new_node
        print(f"Pushed {x} onto stack.")

    elif choice == 2:
        if top is None:
            print("Stack Underflow (empty stack)!")
        else:
            print("Popped value:", top.data)
            top = top.next

    elif choice == 3:
        if top is None:
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):", end=" ")
            temp = top
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
--- LINKED STACK MENU ---
1. Push
2. Pop
3. Display
4. Exit
Enter choice: 1
Enter value to push: 4
Pushed 4 onto stack.

--- LINKED STACK MENU ---
1. Push
2. Pop
3. Display
4. Exit
Enter choice: 1
Enter value to push: 5
Pushed 5 onto stack.

--- LINKED STACK MENU ---
1. Push
2. Pop
3. Display
4. Exit
Enter choice: 1
Enter value to push: 6
Pushed 6 onto stack.

--- LINKED STACK MENU ---
1. Push
2. Pop
3. Display
4. Exit
Enter choice: 3
Stack elements (top to bottom): 6 -> 5 -> 4 -> None

--- LINKED STACK MENU ---
1. Push
2. Pop
3. Display
4. Exit
Enter choice: 2
Popped value: 6

--- LINKED STACK MENU ---
1. Push
2. Pop
3. Display
4. Exit
Enter choice: 3
Stack elements (top to bottom): 5 -> 4 -> None

--- LINKED STACK MENU ---
1. Push
2. Pop
3. Display
4. Exit
Enter choice: 4
Exiting...

** Process exited - Return Code: 0 **
================================================================================
"""
