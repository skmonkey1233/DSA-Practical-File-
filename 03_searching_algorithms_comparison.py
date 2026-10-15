"""
================================================================================
EXPERIMENT 3: SEARCHING ALGORITHMS & TIME COMPLEXITY COMPARISON
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To write and execute a Python program to search for an element using
    Linear Search and Binary Search algorithms and compare their efficiency
    on the basis of execution time and asymptotic time complexities.

TECHNICAL SPECIFICATIONS:
    - Search Paradigms          : Sequential Search vs. Divide and Conquer Search
    - Input Scale               : Array of 1,000,000 integers
    - Asymptotic Complexities   :
        * Linear Search : Best O(1), Average O(n), Worst O(n), Space O(1) [Unsorted/Sorted]
        * Binary Search : Best O(1), Average O(log n), Worst O(log n), Space O(1) [Sorted Only]
================================================================================
"""

# Searching an element using Linear Search and Binary Search
# and comparing them on the basis of time

import time

def linear_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

def binary_search(a, key):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Main program
a = list(range(1, 1000001))      # sorted list of 1 million numbers
key = int(input("Enter element to search (1 to 1000000): "))

start = time.time()
pos1 = linear_search(a, key)
t1 = time.time() - start

start = time.time()
pos2 = binary_search(a, key)
t2 = time.time() - start

print("\nLinear Search : found at index", pos1, "| time = %.8f sec" % t1)
print("Binary Search : found at index", pos2, "| time = %.8f sec" % t2)

print("\n%-15s %-8s %-10s %-10s %s" % ("Algorithm", "Best", "Average", "Worst", "Sorted list needed?"))
print("-" * 60)
print("%-15s %-8s %-10s %-10s %s" % ("Linear Search", "O(1)", "O(n)", "O(n)", "No"))
print("%-15s %-8s %-10s %-10s %s" % ("Binary Search", "O(1)", "O(log n)", "O(log n)", "Yes"))

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
Enter element to search (1 to 1000000): 750000

Linear Search : found at index 749999 | time = 0.01393294 sec
Binary Search : found at index 749999 | time = 0.00000787 sec

Algorithm       Best     Average    Worst      Sorted list needed?
------------------------------------------------------------
Linear Search   O(1)     O(n)       O(n)       No
Binary Search   O(1)     O(log n)   O(log n)   Yes
================================================================================
"""
