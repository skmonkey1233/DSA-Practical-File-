# 📚 Data Structures and Algorithms (DSA) Practical Record

[![Language: Python](https://img.shields.io/badge/Language-Python%203.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Course: MCA Sem 1](https://img.shields.io/badge/Course-MCA%20Sem%201-104C3B)]()
[![Institution: MRIIRS](https://img.shields.io/badge/Institution-MRIIRS%20(SCA)-1E406E)]()
[![Status: Completed](https://img.shields.io/badge/Status-Completed%20(10%20Experiments)-brightgreen)]()

Complete repository for **Data Structures & Algorithms Laboratory Record**, implemented in Python 3. Each experiment is modularized into its own standalone, executable file complete with time/space complexity documentation and terminal execution logs.

---

## 👤 Academic & Student Details

- **Student Name:** Dwadasi Venkata Sri Sai Kumar
- **Roll Number:** `26MCAP101N007`
- **Degree & Branch:** Master of Computer Applications (MCA)
- **Semester:** 1st Semester
- **Department:** School of Computer Applications (SCA)
- **Institution:** Manav Rachna International Institute of Research and Studies (MRIIRS), Faridabad
- **Faculty Mentor:** Mr. Sachin Sharma (Assistant Professor, SCA, MRIIRS)

---

## 📑 Index of Experiments

| Exp No. | Experiment Title | Python File | Data Structure / Concept | Time Complexity | Output Screenshot |
|:---:|:---|:---|:---|:---:|:---:|
| **Exp 1** | List Operations (Insertion, Deletion and Display) | [`01_list_operations.py`](./01_list_operations.py) | Dynamic Array / Python List | `Insert: O(n), Delete: O(n), Display: O(n)` | [View](./screenshots/exp1_list_operations.png) |
| **Exp 2** | Sorting Algorithms & Time Complexity Comparison (Bubble, Insertion, Quick, Merge, Heap) | [`02_sorting_algorithms_comparison.py`](./02_sorting_algorithms_comparison.py) | Sorting & Empirical Benchmark | `O(n log n) to O(n^2)` | [View](./screenshots/exp2_sorting_comparison.png) |
| **Exp 3** | Searching Algorithms & Time Complexity Comparison (Linear Search vs. Binary Search) | [`03_searching_algorithms_comparison.py`](./03_searching_algorithms_comparison.py) | Searching & Empirical Benchmark | `Linear: O(n), Binary: O(log n)` | [View](./screenshots/exp3_searching_comparison.png) |
| **Exp 4** | Stack, Queue, Circular Queue (using Arrays) & Browser History (using Stacks) | [`04_stack_queue_browser_history.py`](./04_stack_queue_browser_history.py) | Stack, Linear Queue, Circular Queue, Dual Stack | `Push/Pop: O(1), Enqueue/Dequeue: O(1)` | [View](./screenshots/exp4_stack_queue_browser.png) |
| **Exp 5** | Evaluation of Postfix Expression | [`05_evaluate_postfix.py`](./05_evaluate_postfix.py) | Stack Application / Arithmetic Expression | `O(n) where n is token count` | [View](./screenshots/exp5_postfix_evaluation.png) |
| **Exp 6** | Conversion of Infix Expression to Postfix | [`06_infix_to_postfix.py`](./06_infix_to_postfix.py) | Stack Application / Shunting-Yard Variant | `O(n)` | [View](./screenshots/exp6_infix_to_postfix.png) |
| **Exp 7** | Singly Linked List (Insert, Delete, Display) | [`07_singly_linked_list.py`](./07_singly_linked_list.py) | Singly Linked List | `Insert Begin: O(1), Insert End: O(n), Delete: O(n)` | [View](./screenshots/exp7_singly_linked_list.png) |
| **Exp 8** | Circular Linked List (Insert, Delete, Display) | [`08_circular_linked_list.py`](./08_circular_linked_list.py) | Circular Singly Linked List | `Insert Begin/End: O(n), Delete: O(n)` | [View](./screenshots/exp8_circular_linked_list.png) |
| **Exp 9** | Stack, Queue & Circular Queue using Linked List | [`09_stack_queue_circular_queue_linked_list.py`](./09_stack_queue_circular_queue_linked_list.py) | Linked List Stack, FIFO Queue & Circular Queue | `Push/Pop: O(1), Enqueue/Dequeue: O(1)` | [View](./screenshots/exp9_linked_list_stack_queue.png) |
| **Exp 10** | Linked List Concatenation & Polynomial Addition | [`10_linked_list_concatenation_and_polynomial.py`](./10_linked_list_concatenation_and_polynomial.py) | Linked List Applications (Concatenation & Polynomial Math) | `Concat: O(n), Add Poly: O(m + n)` | [View](./screenshots/exp10_concatenation_and_polynomial.png) |

---

## ⚡ Algorithmic Comparison: Sorting Algorithms Benchmark (Experiment 2)

| Algorithm | Best Time | Average Time | Worst Time | Auxiliary Space | Stable? | In-Place? |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Bubble Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | ✅ Yes | ✅ Yes |
| **Insertion Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | ✅ Yes | ✅ Yes |
| **Quick Sort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(\log n)$ | ❌ No | ✅ Yes |
| **Merge Sort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ | ✅ Yes | ❌ No |
| **Heap Sort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(1)$ | ❌ No | ✅ Yes |

---

## 🔍 Algorithmic Comparison: Searching Algorithms Benchmark (Experiment 3)

| Algorithm | Best Time | Average Time | Worst Time | Auxiliary Space | Requires Sorted List? |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Linear Search** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | ❌ No (Works on any list) |
| **Binary Search** | $\mathcal{O}(1)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ | ✅ Yes (Requires sorted input) |

---

## 📂 Repository Structure

```text
DSA-Practical-Record/
├── 01_list_operations.py                          # Exp 1: List Operations (Insert, Delete, Display)
├── 02_sorting_algorithms_comparison.py            # Exp 2: Sorting Algorithms (Bubble, Insertion, Quick, Merge, Heap)
├── 03_searching_algorithms_comparison.py          # Exp 3: Searching Algorithms (Linear Search vs Binary Search)
├── 04_stack_queue_browser_history.py              # Exp 4: Stack, Queue, Circular Queue and Browser History
├── 05_evaluate_postfix.py                         # Exp 5: Postfix Expression Evaluation
├── 06_infix_to_postfix.py                         # Exp 6: Infix to Postfix Conversion
├── 07_singly_linked_list.py                       # Exp 7: Singly Linked List (Insert, Delete, Display)
├── 08_circular_linked_list.py                     # Exp 8: Circular Linked List (Insert, Delete, Display)
├── 09_stack_queue_circular_queue_linked_list.py   # Exp 9: Stack, Queue & Circular Queue using Linked List
├── 10_linked_list_concatenation_and_polynomial.py # Exp 10: Linked List Concatenation & Polynomial Addition
├── Data_Structures_and_Algorithms_Practical_File.docx # Official Academic Record Submission Document
├── screenshots/                                   # Terminal execution screenshots for all practicals
│   ├── exp1_list_operations.png
│   ├── exp2_sorting_comparison.png
│   ├── exp3_searching_comparison.png
│   ├── exp4_stack_queue_browser.png
│   ├── exp5_postfix_evaluation.png
│   ├── exp6_infix_to_postfix.png
│   ├── exp7_singly_linked_list.png
│   ├── exp8_circular_linked_list.png
│   ├── exp9_linked_list_stack_queue.png
│   └── exp10_concatenation_and_polynomial.png
├── .gitignore                                     # Standard Python gitignore
└── README.md                                      # Repository documentation and practical index
```

---

## 🚀 How to Clone and Run

### 1. Clone the repository
```bash
git clone <YOUR-GITHUB-REPO-URL>
cd DSA-Practical-Record
```

### 2. Run any experiment
Each experiment is self-contained with no external dependencies required (uses standard Python library):

```bash
# Example: Run List Operations
python 01_list_operations.py

# Example: Run Infix to Postfix Converter
python 06_infix_to_postfix.py

# Example: Run Postfix Expression Evaluator
python 05_evaluate_postfix.py

# Example: Run Polynomial Addition
python 09b_polynomial_addition.py
```

---

## 📝 Verification & Testing
Every experiment has been executed and validated against multiple edge cases:
- Dynamic array boundary checks (underflow, overflow, index bounds)
- Stack underflow/overflow handling
- Queue and Circular Queue wrapping using modular index arithmetic `(rear + 1) % capacity`
- Singly, Circular, and Doubly Linked list traversal and pointer adjustments
- Polynomial degree order alignment and coefficient summation

Execution transcripts and screenshot evidence are embedded directly within each source script and archived under `screenshots/`.

---
*Maintained by **Dwadasi Venkata Sri Sai Kumar** for MCA Semester 1 DSA Practical Evaluation.*
