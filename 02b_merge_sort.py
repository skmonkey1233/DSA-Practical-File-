"""
================================================================================
EXPERIMENT 2B: MERGE SORT ALGORITHM
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To write and execute a Python program to sort a list of numbers using the Merge Sort divide-and-conquer algorithm.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Sorting / Divide & Conquer
    - Time Complexity           : Best/Avg/Worst: O(n log n)
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Experiment 2B: Merge Sort Algorithm
def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []

    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Driver Code
a = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Original List:", a)
sorted_a = merge_sort(a)
print("Sorted list (Merge Sort):", sorted_a)

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
Enter numbers separated by spaces: 1 5 64 87 61
Original List: [1, 5, 64, 87, 61]
Sorted list (Merge Sort): [1, 5, 61, 64, 87]
================================================================================
"""
