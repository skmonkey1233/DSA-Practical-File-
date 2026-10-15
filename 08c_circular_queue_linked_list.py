"""
================================================================================
EXPERIMENT 8C: CIRCULAR QUEUE IMPLEMENTATION USING LINKED LIST
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To implement a Circular Queue using a Linked List maintained with a single rear pointer.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Circular Queue / Linked List
    - Time Complexity           : Enqueue: O(1), Dequeue: O(1)
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Experiment 8C: Circular Queue using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

rear = None

while True:
    print("\n--- LINKED CIRCULAR QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter value: "))
        new_node = Node(x)
        if rear is None:
            rear = new_node
            new_node.next = new_node
        else:
            new_node.next = rear.next
            rear.next = new_node
            rear = new_node
        print(f"Enqueued {x} in circular queue.")

    elif choice == 2:
        if rear is None:
            print("Circular Queue Underflow!")
        else:
            first = rear.next
            print("Dequeued value:", first.data)
            if first == rear:
                rear = None
            else:
                rear.next = first.next

    elif choice == 3:
        if rear is None:
            print("Circular Queue is empty.")
        else:
            print("Circular Queue elements:", end=" ")
            temp = rear.next
            while True:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == rear.next:
                    break
            print("(front)")

    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
--- LINKED CIRCULAR QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 1
Enter value: 4
Enqueued 4 in circular queue.

--- LINKED CIRCULAR QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 1
Enter value: 3
Enqueued 3 in circular queue.

--- LINKED CIRCULAR QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 1
Enter value: 2
Enqueued 2 in circular queue.

--- LINKED CIRCULAR QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 3
Circular Queue elements: 4 -> 3 -> 2 -> (front)

--- LINKED CIRCULAR QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 2
Dequeued value: 4

--- LINKED CIRCULAR QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 3
Circular Queue elements: 3 -> 2 -> (front)

--- LINKED CIRCULAR QUEUE MENU ---
1. Enqueue
2. Dequeue
3. Display
4. Exit
Enter choice: 4
Exiting...

** Process exited - Return Code: 0 **
================================================================================
"""
