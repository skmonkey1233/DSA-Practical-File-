"""
================================================================================
EXPERIMENT 4: STACK, QUEUE, CIRCULAR QUEUE & BROWSER NAVIGATION HISTORY
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To implement and verify Linear Data Structures (Stack, Linear Queue,
    and Circular Queue) using fixed-size arrays, and simulate web browser
    page navigation (Back and Forward) using dual stack concepts in Python.

TECHNICAL SPECIFICATIONS:
    - Data Structures           :
        * Stack          : LIFO (Last In First Out) using fixed array [size = 5]
        * Linear Queue   : FIFO (First In First Out) using fixed array [size = 5]
        * Circular Queue : Ring buffer with modular index arithmetic (rear + 1) % size
        * Browser History: Dual Stack simulation (Back stack & Forward stack)
    - Time Complexities:
        * Push / Pop / Peek     : O(1)
        * Enqueue / Dequeue     : O(1)
        * Browser Visit / Back  : O(1)
================================================================================
"""

# Stack, Queue, Circular Queue (using arrays) and Browser History (using stacks)

SIZE = 5

# ---------------- STACK ----------------
class Stack:
    def __init__(self):
        self.arr = [None] * SIZE
        self.top = -1

    def push(self, x):
        if self.top == SIZE - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.arr[self.top] = x
            print(x, "pushed")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            print(self.arr[self.top], "popped")
            self.top -= 1

    def peek(self):
        print("Top element:", self.arr[self.top]) if self.top != -1 else print("Stack is empty")

    def display(self):
        print("Stack:", self.arr[:self.top + 1]) if self.top != -1 else print("Stack is empty")

# ---------------- QUEUE ----------------
class Queue:
    def __init__(self):
        self.arr = [None] * SIZE
        self.front = 0
        self.rear = -1

    def enqueue(self, x):
        if self.rear == SIZE - 1:
            print("Queue is Full")
        else:
            self.rear += 1
            self.arr[self.rear] = x
            print(x, "inserted")

    def dequeue(self):
        if self.front > self.rear:
            print("Queue is Empty")
        else:
            print(self.arr[self.front], "removed")
            self.front += 1

    def display(self):
        print("Queue:", self.arr[self.front:self.rear + 1]) if self.front <= self.rear else print("Queue is empty")

# ---------------- CIRCULAR QUEUE ----------------
class CircularQueue:
    def __init__(self):
        self.arr = [None] * SIZE
        self.front = -1
        self.rear = -1

    def enqueue(self, x):
        if (self.rear + 1) % SIZE == self.front:
            print("Circular Queue is Full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % SIZE
        self.arr[self.rear] = x
        print(x, "inserted")

    def dequeue(self):
        if self.front == -1:
            print("Circular Queue is Empty")
            return
        print(self.arr[self.front], "removed")
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % SIZE

    def display(self):
        if self.front == -1:
            print("Circular Queue is empty")
            return
        items = []
        i = self.front
        while True:
            items.append(self.arr[i])
            if i == self.rear:
                break
            i = (i + 1) % SIZE
        print("Circular Queue:", items)

# ---------------- BROWSER HISTORY (2 stacks) ----------------
class Browser:
    def __init__(self):
        self.back = []        # stack of previous pages
        self.forward = []     # stack of forward pages
        self.current = "Home"

    def visit(self, url):
        self.back.append(self.current)
        self.current = url
        self.forward = []     # new visit clears forward history
        print("Visited:", self.current)

    def go_back(self):
        if not self.back:
            print("No page to go back")
        else:
            self.forward.append(self.current)
            self.current = self.back.pop()
            print("Back to:", self.current)

    def go_forward(self):
        if not self.forward:
            print("No page to go forward")
        else:
            self.back.append(self.current)
            self.current = self.forward.pop()
            print("Forward to:", self.current)

    def show(self):
        print("Back stack   :", self.back)
        print("Current page :", self.current)
        print("Forward stack:", self.forward)

# ---------------- MAIN MENU ----------------
s, q, cq, b = Stack(), Queue(), CircularQueue(), Browser()

while True:
    print("\n1.Stack  2.Queue  3.Circular Queue  4.Browser History  5.Exit")
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
        while True:
            c = input("\n[Browser] 1.Visit 2.Back 3.Forward 4.Show 5.Exit: ")
            if c == "1": b.visit(input("Enter website: "))
            elif c == "2": b.go_back()
            elif c == "3": b.go_forward()
            elif c == "4": b.show()
            else: break

    elif ch == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
1.Stack  2.Queue  3.Circular Queue  4.Browser History  5.Exit
Enter choice: 1

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 1
Enter value: 1
1 pushed

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 1
Enter value: 2
2 pushed

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 1
Enter value: 3
3 pushed

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 4
Stack: ['1', '2', '3']

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 2
3 popped

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 4
Stack: ['1', '2']

[Stack] 1.Push 2.Pop 3.Peek 4.Display 5.Back: 5

1.Stack  2.Queue  3.Circular Queue  4.Browser History  5.Exit
Enter choice: 2

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 1
Enter value: 1
1 inserted

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 1
Enter value: 5
5 inserted

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 1
Enter value: 15
15 inserted

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 1
Enter value: 2
2 inserted

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 3
Queue: ['1', '5', '15', '2']

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 2
1 removed

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 3
Queue: ['5', '15', '2']

[Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 4

1.Stack  2.Queue  3.Circular Queue  4.Browser History  5.Exit
Enter choice: 3

[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 1
Enter value: 8
8 inserted

[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 1
Enter value: 9
9 inserted

[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 1
Enter value: 12
12 inserted

[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 3
Circular Queue: ['8', '9', '12']

[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 2
8 removed

[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 3
Circular Queue: ['9', '12']

[Circular Queue] 1.Enqueue 2.Dequeue 3.Display 4.Back: 4

1.Stack  2.Queue  3.Circular Queue  4.Browser History  5.Exit
Enter choice: 4

[Browser] 1.Visit 2.Back 3.Forward 4.Show 5.Exit: 1
Enter website: https://www.youtube.com/
Visited: https://www.youtube.com/

[Browser] 1.Visit 2.Back 3.Forward 4.Show 5.Exit: 1
Enter website: https://www.amazon.in/
Visited: https://www.amazon.in/

[Browser] 1.Visit 2.Back 3.Forward 4.Show 5.Exit: 4
Back stack   : ['Home', 'https://www.youtube.com/']
Current page : https://www.amazon.in/
Forward stack: []

[Browser] 1.Visit 2.Back 3.Forward 4.Show 5.Exit: 3
No page to go forward

[Browser] 1.Visit 2.Back 3.Forward 4.Show 5.Exit: 2
Back to: https://www.youtube.com/

[Browser] 1.Visit 2.Back 3.Forward 4.Show 5.Exit: 3
Forward to: https://www.amazon.in/

[Browser] 1.Visit 2.Back 3.Forward 4.Show 5.Exit: 5

1.Stack  2.Queue  3.Circular Queue  4.Browser History  5.Exit
Enter choice: 5
Program ended.
================================================================================
"""
