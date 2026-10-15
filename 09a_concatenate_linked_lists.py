"""
================================================================================
EXPERIMENT 9A: CONCATENATION OF TWO SINGLY LINKED LISTS
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To write a Python program that creates two separate singly linked lists and concatenates the second list to the end of the first list.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Linked List Application
    - Time Complexity           : O(m) where m is length of first list
    - Auxiliary Space Complexity: O(1) auxiliary
================================================================================
"""

# Experiment 9A: Concatenation of Two Linked Lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def make_list(n, name="list"):
    head = None
    tail = None
    print(f"Enter {n} elements for {name}:")
    for i in range(n):
        x = int(input(f"  Element {i + 1}: "))
        new_node = Node(x)
        if head is None:
            head = tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

def display_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

# Driver Code
n = int(input("Enter number of elements in first list: "))
first = make_list(n, "First List")

m = int(input("Enter number of elements in second list: "))
second = make_list(m, "Second List")

print("\nFirst List :", end=" ")
display_list(first)
print("Second List:", end=" ")
display_list(second)

# Concatenation
if first is None:
    first = second
else:
    temp = first
    while temp.next is not None:
        temp = temp.next
    temp.next = second

print("\nCombined Concatenated List:", end=" ")
display_list(first)

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
Enter number of elements in first list: 3
Enter 3 elements for First List:
  Element 1: 4
  Element 2: 5
  Element 3: 9
Enter number of elements in second list: 2
Enter 2 elements for Second List:
  Element 1: 3
  Element 2: 1

First List : 4 -> 5 -> 9 -> None
Second List: 3 -> 1 -> None

Combined Concatenated List: 4 -> 5 -> 9 -> 3 -> 1 -> None

** Process exited - Return Code: 0 **
================================================================================
"""
