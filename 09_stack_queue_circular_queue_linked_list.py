"""
================================================================================
EXPERIMENT 9: STACK, QUEUE AND CIRCULAR QUEUE USING LINKED LIST
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To write and execute a Python program to implement Stack, Queue,
    and Circular Queue data structures using Singly Linked Lists and
    Circular Linked Lists.

TECHNICAL SPECIFICATIONS:
    - Stack Implementation          : Singly Linked List (LIFO)
        * Push (Insert at Head)     : O(1) time
        * Pop (Remove from Head)    : O(1) time
        * Peek                      : O(1) time
        * Display                   : O(n) time
    - Queue Implementation          : Singly Linked List with Front & Rear (FIFO)
        * Enqueue (Insert at Rear)  : O(1) time
        * Dequeue (Remove Front)    : O(1) time
        * Display                   : O(n) time
    - Circular Queue Implementation : Circular Linked List (rear.next -> front)
        * Enqueue (Insert at Rear)  : O(1) time
        * Dequeue (Remove Front)    : O(1) time
        * Display                   : O(n) time
    - Auxiliary Space Complexity    : O(n) dynamic node allocation
================================================================================
"""

# Stack, Queue and Circular Queue using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ---------------- STACK (insert/remove at head) ----------------
class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        node = Node(x)
        node.next = self.top
        self.top = node
        print(x, "pushed")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print(self.top.data, "popped")
            self.top = self.top.next

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        temp = self.top
        print("Stack (top to bottom):", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# ---------------- QUEUE (insert at rear, remove from front) ----------------
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        node = Node(x)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        print(x, "inserted")

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return
        print(self.front.data, "removed")
        self.front = self.front.next
        if self.front is None:
            self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        print("Queue (front to rear):", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# ---------------- CIRCULAR QUEUE (rear.next always points to front) ----------------
class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        node = Node(x)
        if self.front is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.rear.next = self.front         # keep the circle
        print(x, "inserted")

    def dequeue(self):
        if self.front is None:
            print("Circular Queue is Empty")
            return
        print(self.front.data, "removed")
        if self.front == self.rear:         # only one node
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

    def display(self):
        if self.front is None:
            print("Circular Queue is empty")
            return
        temp = self.front
        print("Circular Queue:", end=" ")
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.front:
                break
        print("(back to front)")

# ---------------- MAIN MENU ----------------
s, q, cq = Stack(), Queue(), CircularQueue()

while True:
    print("\n1.Stack  2.Queue  3.Circular Queue  4.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        while True:
            c = input("\n[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: ")
            if c == "1": s.push(input("Enter value: "))
            elif c == "2": s.pop()
            elif c == "3": s.peek()
            elif c == "4": s.display()
            else: break

    elif ch == "2":
        while True:
            c = input("\n[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: ")
            if c == "1": q.enqueue(input("Enter value: "))
            elif c == "2": q.dequeue()
            elif c == "3": q.display()
            else: break

    elif ch == "3":
        while True:
            c = input("\n[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: ")
            if c == "1": cq.enqueue(input("Enter value: "))
            elif c == "2": cq.dequeue()
            elif c == "3": cq.display()
            else: break

    elif ch == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
1.Stack  2.Queue  3.Circular Queue  4.Exit
Enter choice: 1

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 1
Enter value: 10
10 pushed

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 1
Enter value: 20
20 pushed

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 3
Top element: 20

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 4
Stack (top to bottom): 20 10 

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 2
20 popped

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 4
Stack (top to bottom): 10 

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 5

1.Stack  2.Queue  3.Circular Queue  4.Exit
Enter choice: 2

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 1
Enter value: 30
30 inserted

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 1
Enter value: 40
40 inserted

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 3
Queue (front to rear): 30 40 

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 2
30 removed

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 3
Queue (front to rear): 40 

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 4

1.Stack  2.Queue  3.Circular Queue  4.Exit
Enter choice: 3

[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 1
Enter value: 50
50 inserted

[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 1
Enter value: 60
60 inserted

[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 3
Circular Queue: 50 60 (back to front)

[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 2
50 removed

[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 3
Circular Queue: 60 (back to front)

[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 4

1.Stack  2.Queue  3.Circular Queue  4.Exit
Enter choice: 4
Program ended.
================================================================================
"""
