"""
================================================================================
EXPERIMENT 2: SORTING ALGORITHMS & TIME COMPLEXITY COMPARISON
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To write and execute a Python program to sort a list using Bubble Sort,
    Insertion Sort, Quick Sort, Merge Sort, and Heap Sort, and compare them
    on the basis of execution time and asymptotic time complexities.

TECHNICAL SPECIFICATIONS:
    - Sorting Algorithms        : Bubble Sort, Insertion Sort, Quick Sort, Merge Sort, Heap Sort
    - Asymptotic Complexities   :
        * Bubble Sort   : Best O(n), Avg O(n^2), Worst O(n^2), Space O(1) [Stable, In-Place]
        * Insertion Sort: Best O(n), Avg O(n^2), Worst O(n^2), Space O(1) [Stable, In-Place]
        * Quick Sort    : Best O(n log n), Avg O(n log n), Worst O(n^2), Space O(log n) [In-Place]
        * Merge Sort    : Best O(n log n), Avg O(n log n), Worst O(n log n), Space O(n) [Stable]
        * Heap Sort     : Best O(n log n), Avg O(n log n), Worst O(n log n), Space O(1) [In-Place]
================================================================================
"""

# Sorting a list using Bubble, Quick, Insertion, Merge and Heap sort
# and comparing them on the basis of time

import random
import time

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

def heapify(a, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heap_sort(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)
    return a

# Main program
data = [random.randint(1, 10000) for _ in range(2000)]
print("Original list (first 10):", data[:10])
print("Sorted list   (first 10):", sorted(data)[:10])

algorithms = [
    ("Bubble Sort",    bubble_sort,    "O(n)",       "O(n^2)",     "O(n^2)"),
    ("Insertion Sort", insertion_sort, "O(n)",       "O(n^2)",     "O(n^2)"),
    ("Quick Sort",     quick_sort,     "O(n log n)", "O(n log n)", "O(n^2)"),
    ("Merge Sort",     merge_sort,     "O(n log n)", "O(n log n)", "O(n log n)"),
    ("Heap Sort",      heap_sort,      "O(n log n)", "O(n log n)", "O(n log n)"),
]

print("\n%-15s %-12s %-12s %-12s %s" % ("Algorithm", "Best", "Average", "Worst", "Time taken (sec)"))
print("-" * 70)
for name, func, best, avg, worst in algorithms:
    start = time.time()
    result = func(data.copy())
    end = time.time()
    assert result == sorted(data)
    print("%-15s %-12s %-12s %-12s %.4f" % (name, best, avg, worst, end - start))

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
Original list (first 10): [3796, 3191, 4706, 1925, 8951, 513, 2585, 3291, 3116, 7482]
Sorted list   (first 10): [6, 9, 11, 11, 14, 23, 25, 29, 41, 53]

Algorithm       Best         Average      Worst        Time taken (sec)
----------------------------------------------------------------------
Bubble Sort     O(n)         O(n^2)       O(n^2)       0.1200
Insertion Sort  O(n)         O(n^2)       O(n^2)       0.0540
Quick Sort      O(n log n)   O(n log n)   O(n^2)       0.0030
Merge Sort      O(n log n)   O(n log n)   O(n log n)   0.0030
Heap Sort       O(n log n)   O(n log n)   O(n log n)   0.0030
================================================================================
"""
