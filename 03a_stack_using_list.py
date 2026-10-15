"""
================================================================================
EXPERIMENT 3A: STACK IMPLEMENTATION USING LIST
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To implement the Stack data structure (Last In First Out - LIFO) using a Python list supporting Push, Pop, and Display operations.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Stack (LIFO) / List
    - Time Complexity           : Push: O(1), Pop: O(1), Peek: O(1)
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Experiment 3A: Stack using List
stack = []

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter value: "))
        stack.append(x)
        print(f"{x} pushed onto stack.")
    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty (Underflow)!")
        else:
            print("Popped element:", stack.pop())
    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack (top to bottom):", stack[::-1])
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
--- STACK MENU ---
1. Push
2. Pop
3. Display
4. Exit
Enter choice: 1
Enter value: 2
2 pushed onto stack.

--- STACK MENU ---
1. Push
2. Pop
3. Display
4. Exit
Enter choice: 1
Enter value: 3
3 pushed onto stack.

--- STACK MENU ---
1. Push
2. Pop
3. Display
4. Exit
Enter choice: 1
Enter value: 4
4 pushed onto stack.

--- STACK MENU ---
1. Push
2. Pop
3. Display
4. Exit
Enter choice: 3
Stack (top to bottom): [4, 3, 2]

--- STACK MENU ---
1. Push
2. Pop
3. Display
4. Exit
Enter choice: 2
Popped element: 4

--- STACK MENU ---
1. Push
2. Pop
3. Display
4. Exit
Enter choice: 3
Stack (top to bottom): [3, 2]
================================================================================
"""
