# 📚 Data Structures and Algorithms (DSA) Practical Record

[![Language: Python](https://img.shields.io/badge/Language-Python%203.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Course: MCA Sem 1](https://img.shields.io/badge/Course-MCA%20Sem%201-104C3B)]()
[![Institution: MRIIRS](https://img.shields.io/badge/Institution-MRIIRS%20(SCA)-1E406E)]()
[![Status: Completed](https://img.shields.io/badge/Status-Completed%20(18%20Experiments)-brightgreen)]()

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
| **Exp 2** | Sorting Algorithms & Time Complexity Comparison (Bubble, Insertion, Quick, Merge, Heap) | [`02_sorting_algorithms_comparison.py`](./02_sorting_algorithms_comparison.py) | Sorting & Empirical Benchmark | `O(n log n) to O(n^2)` | [View](./screenshots/time_complexity_comparison.png) |
| **Exp 3A** | Stack using List | [`03a_stack_using_list.py`](./03a_stack_using_list.py) | Stack (LIFO) / List | `Push: O(1), Pop: O(1), Peek: O(1)` | [View](./screenshots/exp3a_stack_list.png) |
| **Exp 3B** | Queue using List | [`03b_queue_using_list.py`](./03b_queue_using_list.py) | Linear Queue (FIFO) / List | `Enqueue: O(1), Dequeue: O(n)` | [View](./screenshots/exp3b_queue_list.png) |
| **Exp 3C** | Circular Queue using List | [`03c_circular_queue_using_list.py`](./03c_circular_queue_using_list.py) | Circular Queue (FIFO) / Fixed Array | `Enqueue: O(1), Dequeue: O(1)` | [View](./screenshots/exp3c_circular_queue_list.png) |
| **Exp 3D** | Browser History using Stack | [`03d_browser_history_stack.py`](./03d_browser_history_stack.py) | Stack Application / Browser Simulation | `Visit: O(1), Back: O(1), View: O(n)` | [View](./screenshots/exp3d_browser_history.png) |
| **Exp 4** | Evaluate Postfix Expression | [`04_evaluate_postfix.py`](./04_evaluate_postfix.py) | Stack Application / Arithmetic Expression | `O(n) where n is expression length` | [View](./screenshots/exp4_postfix_evaluation.png) |
| **Exp 5** | Convert Infix to Postfix | [`05_infix_to_postfix.py`](./05_infix_to_postfix.py) | Stack Application / Shunting-yard variant | `O(n)` | [View](./screenshots/exp5_infix_to_postfix.png) |
| **Exp 6** | Singly Linked List (Insert, Delete, Display) | [`06_singly_linked_list.py`](./06_singly_linked_list.py) | Singly Linked List | `Insert End: O(n), Delete: O(n), Display: O(n)` | [View](./screenshots/exp6_singly_linked_list.png) |
| **Exp 7** | Circular Linked List (Insert, Delete, Display) | [`07_circular_linked_list.py`](./07_circular_linked_list.py) | Circular Singly Linked List | `Insert End: O(n), Delete: O(n), Display: O(n)` | [View](./screenshots/exp7_circular_linked_list.png) |
| **Exp 8A** | Stack using Linked List | [`08a_stack_linked_list.py`](./08a_stack_linked_list.py) | Stack (LIFO) / Linked List | `Push: O(1), Pop: O(1), Peek: O(1)` | [View](./screenshots/exp8a_stack_linked_list.png) |
| **Exp 8B** | Queue using Linked List | [`08b_queue_linked_list.py`](./08b_queue_linked_list.py) | Linear Queue (FIFO) / Linked List | `Enqueue: O(1), Dequeue: O(1)` | [View](./screenshots/exp8b_queue_linked_list.png) |
| **Exp 8C** | Circular Queue using Linked List | [`08c_circular_queue_linked_list.py`](./08c_circular_queue_linked_list.py) | Circular Queue / Linked List | `Enqueue: O(1), Dequeue: O(1)` | [View](./screenshots/exp8c_circular_queue_linked_list.png) |
| **Exp 9A** | Concatenation of Two Linked Lists | [`09a_concatenate_linked_lists.py`](./09a_concatenate_linked_lists.py) | Linked List Application | `O(m) where m is length of first list` | [View](./screenshots/exp9a_concatenate_linked_lists.png) |
| **Exp 9B** | Polynomial Addition using Linked Lists | [`09b_polynomial_addition.py`](./09b_polynomial_addition.py) | Linked List Application / Polynomial | `O(m + n) where m, n are terms count` | [View](./screenshots/exp9b_polynomial_addition.png) |
| **Exp 10** | Doubly Linked List (Insert, Delete, Display) | [`10_doubly_linked_list.py`](./10_doubly_linked_list.py) | Doubly Linked List | `Insert End: O(n), Delete: O(n), Display: O(n)` | [View](./screenshots/exp10_doubly_linked_list.png) |

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

## 📂 Repository Structure

```text
DSA-Practical-Record/
├── 01_list_operations.py                 # Exp 1: List Operations (Insert, Delete, Display)
├── 02_sorting_algorithms_comparison.py   # Exp 2: Sorting Algorithms (Bubble, Insertion, Quick, Merge, Heap)
├── 03a_stack_using_list.py               # Exp 3A: Stack using List (LIFO)
├── 03b_queue_using_list.py               # Exp 3B: Linear Queue using List (FIFO)
├── 03c_circular_queue_using_list.py      # Exp 3C: Circular Queue using List
├── 03d_browser_history_stack.py          # Exp 3D: Browser History Simulation
├── 04_evaluate_postfix.py                # Exp 4: Postfix Expression Evaluation
├── 05_infix_to_postfix.py                # Exp 5: Infix to Postfix Conversion
├── 06_singly_linked_list.py              # Exp 6: Singly Linked List (Insert, Delete, Display)
├── 07_circular_linked_list.py            # Exp 7: Circular Linked List (Insert, Delete, Display)
├── 08a_stack_linked_list.py              # Exp 8A: Stack using Linked List
├── 08b_queue_linked_list.py              # Exp 8B: Queue using Linked List
├── 08c_circular_queue_linked_list.py     # Exp 8C: Circular Queue using Linked List
├── 09a_concatenate_linked_lists.py       # Exp 9A: Concatenation of Two Linked Lists
├── 09b_polynomial_addition.py            # Exp 9B: Polynomial Addition using Linked Lists
├── 10_doubly_linked_list.py              # Exp 10: Doubly Linked List (Insert, Delete, Display)
├── screenshots/                          # Terminal execution screenshots for all practicals
│   ├── exp1_list_operations.png
│   ├── ...
│   └── exp10_doubly_linked_list.png
├── .gitignore                            # Standard Python gitignore
└── README.md                             # Repository documentation and practical index
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

# Example: Run Quick Sort
python 02a_quick_sort.py

# Example: Run Infix to Postfix Converter
python 05_infix_to_postfix.py

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
