"""
================================================================================
EXPERIMENT 3C: CIRCULAR QUEUE IMPLEMENTATION USING LIST
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To implement a fixed-size Circular Queue using a Python list with modular arithmetic to prevent memory wastage.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Circular Queue (FIFO) / Fixed Array
    - Time Complexity           : Enqueue: O(1), Dequeue: O(1)
    - Auxiliary Space Complexity: O(k) fixed capacity
================================================================================
"""

# Experiment 3C: Circular Queue using List
size = 5
queue = [None] * size
front = -1
rear = -1

while True:
    print("\n--- CIRCULAR QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        if (rear + 1) % size == front:
            print("Queue is full (Overflow)!")
        else:
            x = int(input("Enter value: "))
            if front == -1:
                front = 0
            rear = (rear + 1) % size
            queue[rear] = x
            print(f"Inserted {x} at index {rear}.")

    elif choice == 2:
        if front == -1:
            print("Queue is empty (Underflow)!")
        else:
            print("Deleted element:", queue[front])
            queue[front] = None
            if front == rear:
                front = rear = -1
            else:
                front = (front + 1) % size

    elif choice == 3:
        if front == -1:
            print("Queue is empty.")
        else:
            print("Circular Queue elements:", end=" ")
            i = front
            while True:
                print(queue[i], end=" ")
                if i == rear:
                    break
                i = (i + 1) % size
            print()

    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
--- CIRCULAR QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 1
Enter value: 2
Inserted 2 at index 0.

--- CIRCULAR QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 1
Enter value: 3
Inserted 3 at index 1.

--- CIRCULAR QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 3
Circular Queue elements: 2 3 

--- CIRCULAR QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 2
Deleted element: 2
================================================================================
"""
