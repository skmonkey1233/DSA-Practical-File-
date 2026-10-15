"""
================================================================================
EXPERIMENT 3B: QUEUE IMPLEMENTATION USING LIST
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To implement the Linear Queue data structure (First In First Out - FIFO) using a Python list supporting Enqueue, Dequeue, and Display operations.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Linear Queue (FIFO) / List
    - Time Complexity           : Enqueue: O(1), Dequeue: O(n)
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Experiment 3B: Queue using List
queue = []

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter value: "))
        queue.append(x)
        print(f"{x} enqueued successfully.")
    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty (Underflow)!")
        else:
            print("Deleted element:", queue.pop(0))
    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue (front to rear):", queue)
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
--- QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 1
Enter value: 2
2 enqueued successfully.

--- QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 1
Enter value: 3
3 enqueued successfully.

--- QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 3
Queue (front to rear): [2, 3]

--- QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 2
Deleted element: 2
================================================================================
"""
