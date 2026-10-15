"""
================================================================================
EXPERIMENT 10: LINKED LIST CONCATENATION & POLYNOMIAL REPRESENTATION AND ADDITION
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To write and execute a Python program to perform:
    1. Concatenation of two singly linked lists into a single merged chain.
    2. Representation and addition of single-variable polynomials using linked lists.

TECHNICAL SPECIFICATIONS:
    - Part 1: Singly Linked List Concatenation
        * Time Complexity      : O(n) where n is the length of the first list
        * Auxiliary Space      : O(1) in-place pointer relinking (temp.next = list2)
    - Part 2: Polynomial Representation & Addition
        * Representation       : Linked list where each node contains (coeff, power, next)
        * Ordering             : Strictly maintained in descending order of powers
        * Addition Complexity  : O(m + n) merge traversal where m, n are term counts
        * Auxiliary Space      : O(m + n) to store the resulting polynomial nodes
================================================================================
"""

# 1. Concatenation of two linked lists
# 2. Polynomial representation and addition using linked lists

# ---------------- PART 1: CONCATENATION ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_list(values):
    head = None
    for v in values:
        node = Node(v)
        if head is None:
            head = node
        else:
            temp = head
            while temp.next:
                temp = temp.next
            temp.next = node
    return head

def concatenate(list1, list2):
    if list1 is None:
        return list2
    temp = list1
    while temp.next:
        temp = temp.next
    temp.next = list2                       # last node of list1 -> head of list2
    return list1

def display(head):
    if head is None:
        print("List is empty")
        return
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# ---------------- PART 2: POLYNOMIAL ----------------
class Term:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None

def create_poly():
    head = None
    n = int(input("Enter number of terms: "))
    for i in range(n):
        c = int(input("  Coefficient of term %d: " % (i + 1)))
        p = int(input("  Power of term %d      : " % (i + 1)))
        node = Term(c, p)
        if head is None or p > head.power:  # keep powers in descending order
            node.next = head
            head = node
        else:
            temp = head
            while temp.next and temp.next.power >= p:
                temp = temp.next
            node.next = temp.next
            temp.next = node
    return head

def add_poly(p1, p2):
    result = []
    while p1 and p2:
        if p1.power == p2.power:
            result.append((p1.coeff + p2.coeff, p1.power))
            p1, p2 = p1.next, p2.next
        elif p1.power > p2.power:
            result.append((p1.coeff, p1.power))
            p1 = p1.next
        else:
            result.append((p2.coeff, p2.power))
            p2 = p2.next
    while p1:
        result.append((p1.coeff, p1.power))
        p1 = p1.next
    while p2:
        result.append((p2.coeff, p2.power))
        p2 = p2.next
    head = None
    for c, p in reversed(result):           # build linked list of the sum
        node = Term(c, p)
        node.next = head
        head = node
    return head

def show_poly(head):
    if head is None:
        print("0")
        return
    text = ""
    while head:
        text += "%+dx^%d " % (head.coeff, head.power)
        head = head.next
    print(text)

# ---------------- MAIN MENU ----------------
while True:
    print("\n1. Concatenate two linked lists")
    print("2. Polynomial addition")
    print("3. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        a = create_list(input("Enter elements of list 1 (space separated): ").split())
        b = create_list(input("Enter elements of list 2 (space separated): ").split())
        print("List 1 : ", end=""); display(a)
        print("List 2 : ", end=""); display(b)
        print("After concatenation: ", end=""); display(concatenate(a, b))

    elif ch == "2":
        print("\n-- First polynomial --")
        p1 = create_poly()
        print("\n-- Second polynomial --")
        p2 = create_poly()
        print("\nFirst  polynomial : ", end=""); show_poly(p1)
        print("Second polynomial : ", end=""); show_poly(p2)
        print("Sum               : ", end=""); show_poly(add_poly(p1, p2))

    elif ch == "3":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
1. Concatenate two linked lists
2. Polynomial addition
3. Exit
Enter choice: 1
Enter elements of list 1 (space separated): 45 11 26
Enter elements of list 2 (space separated): 78 95 23
List 1 : 45 -> 11 -> 26 -> None
List 2 : 78 -> 95 -> 23 -> None
After concatenation: 45 -> 11 -> 26 -> 78 -> 95 -> 23 -> None

1. Concatenate two linked lists
2. Polynomial addition
3. Exit
Enter choice: 2

-- First polynomial --
Enter number of terms: 2
  Coefficient of term 1: 4
  Power of term 1      : 2
  Coefficient of term 2: 8
  Power of term 2      : 3

-- Second polynomial --
Enter number of terms: 1
  Coefficient of term 1: 2
  Power of term 1      : 5

First  polynomial : +8x^3 +4x^2 
Second polynomial : +2x^5 
Sum               : +2x^5 +8x^3 +4x^2 

1. Concatenate two linked lists
2. Polynomial addition
3. Exit
Enter choice: 3
Program ended.
================================================================================
"""
