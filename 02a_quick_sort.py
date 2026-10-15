"""
================================================================================
EXPERIMENT 2A: QUICK SORT ALGORITHM
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To write and execute a Python program to sort a list of numbers using the Quick Sort divide-and-conquer algorithm.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Sorting / Divide & Conquer
    - Time Complexity           : Best/Avg: O(n log n), Worst: O(n^2)
    - Auxiliary Space Complexity: O(log n)
================================================================================
"""

# Experiment 2A: Quick Sort Algorithm
def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[-1]
    left = []
    right = []

    for x in a[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)

# Driver Code
a = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Original List:", a)
sorted_a = quick_sort(a)
print("Sorted list (Quick Sort):", sorted_a)

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
Enter numbers separated by spaces: 58 741 512 29 1 23 3
Original List: [58, 741, 512, 29, 1, 23, 3]
Sorted list (Quick Sort): [1, 3, 23, 29, 58, 512, 741]
================================================================================
"""
