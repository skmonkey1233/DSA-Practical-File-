"""
================================================================================
TIME COMPLEXITY COMPARISON: TIME COMPLEXITY COMPARISON: QUICK SORT VS. MERGE SORT
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To analytically compare the time complexity, space complexity, stability, and operational efficiency of Quick Sort and Merge Sort.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Empirical Benchmark & Complexity Analysis
    - Time Complexity           : Comparison: Quick Sort vs Merge Sort
    - Auxiliary Space Complexity: O(n) auxiliary
================================================================================
"""

# Analytical Demonstration: Quick Sort vs Merge Sort Performance Characteristics
# Quick Sort: In-place, cache-friendly, but O(n^2) worst case if pivot is unbalanced.
# Merge Sort: Guaranteed O(n log n) in all cases, stable, but requires O(n) auxiliary space.

import time
import random

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[-1]
    left = [x for x in a[:-1] if x <= pivot]
    right = [x for x in a[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    res, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    res.extend(left[i:]); res.extend(right[j:])
    return res

test_data = [random.randint(1, 1000) for _ in range(2000)]
t0 = time.perf_counter()
quick_sort(test_data.copy())
t_quick = time.perf_counter() - t0

t0 = time.perf_counter()
merge_sort(test_data.copy())
t_merge = time.perf_counter() - t0

print(f"Quick Sort Execution Time for 2000 items: {t_quick * 1000:.3f} ms")
print(f"Merge Sort Execution Time for 2000 items: {t_merge * 1000:.3f} ms")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
Quick Sort Execution Time for 2000 items: 6.895 ms
Merge Sort Execution Time for 2000 items: 12.698 ms

** Process exited - Return Code: 0 **
================================================================================
"""
