"""
================================================================================
EXPERIMENT 8B: QUEUE IMPLEMENTATION USING LINKED LIST
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To implement a Queue data structure using a Singly Linked List with front and rear pointers supporting Enqueue, Dequeue, and Display.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Linear Queue (FIFO) / Linked List
    - Time Complexity           : Enqueue: O(1), Dequeue: O(1)
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Experiment 8B: Queue using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

front = None
rear = None

while True:
    print("\n--- LINKED QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter value to enqueue: "))
        new_node = Node(x)
        if rear is None:
            front = rear = new_node
        else:
            rear.next = new_node
            rear = new_node
        print(f"Enqueued {x} into queue.")

    elif choice == 2:
        if front is None:
            print("Queue Underflow (empty queue)!")
        else:
            print("Dequeued value:", front.data)
            front = front.next
            if front is None:
                rear = None

    elif choice == 3:
        if front is None:
            print("Queue is empty.")
        else:
            print("Queue elements (front to rear):", end=" ")
            temp = front
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
--- LINKED QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 1
Enter value to enqueue: 4
Enqueued 4 into queue.

--- LINKED QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 1
Enter value to enqueue: 2
Enqueued 2 into queue.

--- LINKED QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 1
Enter value to enqueue: 3
Enqueued 3 into queue.

--- LINKED QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 3
Queue elements (front to rear): 4 -> 2 -> 3 -> None

--- LINKED QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 2
Dequeued value: 4

--- LINKED QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 3
Queue elements (front to rear): 2 -> 3 -> None

--- LINKED QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 4
Exiting...

** Process exited - Return Code: 0 **
================================================================================
"""
