"""
================================================================================
EXPERIMENT 9B: POLYNOMIAL ADDITION USING LINKED LISTS
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To represent two single-variable polynomials using linked lists and compute their sum by combining coefficients of matching exponents.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Linked List Application / Polynomial
    - Time Complexity           : O(m + n) where m, n are terms count
    - Auxiliary Space Complexity: O(m + n)
================================================================================
"""

# Experiment 9B: Polynomial Addition using Linked Lists
class Term:
    def __init__(self, coef, power):
        self.coef = coef
        self.power = power
        self.next = None

def add_term(head, coef, power):
    if coef == 0:
        return head
    new_term = Term(coef, power)
    if head is None:
        return new_term
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = new_term
    return head

def read_polynomial(name):
    head = None
    n = int(input(f"Number of terms in {name}: "))
    for i in range(n):
        coef = int(input(f"  Term {i + 1} Coefficient: "))
        power = int(input(f"  Term {i + 1} Power: "))
        head = add_term(head, coef, power)
    return head

def display_poly(head):
    if head is None:
        print("0")
        return
    temp = head
    while temp is not None:
        print(f"{temp.coef}x^{temp.power}", end="")
        if temp.next is not None:
            print(" + ", end="")
        temp = temp.next
    print()

def add_polynomials(p1, p2):
    result = None
    t1 = p1
    while t1 is not None:
        t2 = p2
        found = False
        while t2 is not None:
            if t1.power == t2.power:
                result = add_term(result, t1.coef + t2.coef, t1.power)
                found = True
                break
            t2 = t2.next
        if not found:
            result = add_term(result, t1.coef, t1.power)
        t1 = t1.next

    t2 = p2
    while t2 is not None:
        t1 = p1
        found = False
        while t1 is not None:
            if t2.power == t1.power:
                found = True
                break
            t1 = t1.next
        if not found:
            result = add_term(result, t2.coef, t2.power)
        t2 = t2.next
    return result

# Driver Code
p1 = read_polynomial("Polynomial 1")
p2 = read_polynomial("Polynomial 2")

print("\nPolynomial 1:", end=" ")
display_poly(p1)
print("Polynomial 2:", end=" ")
display_poly(p2)

result = add_polynomials(p1, p2)
print("Sum of Polynomials:", end=" ")
display_poly(result)

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
Number of terms in Polynomial 1: 3
  Term 1 Coefficient: 4
  Term 1 Power: 5
  Term 2 Coefficient: 6
  Term 2 Power: 7
  Term 3 Coefficient: 8
  Term 3 Power: 9
Number of terms in Polynomial 2: 2
  Term 1 Coefficient: 0
  Term 1 Power: 1
  Term 2 Coefficient: 2
  Term 2 Power: 3

Polynomial 1: 4x^5 + 6x^7 + 8x^9
Polynomial 2: 2x^3
Sum of Polynomials: 4x^5 + 6x^7 + 8x^9 + 2x^3

** Process exited - Return Code: 0 **
================================================================================
"""
