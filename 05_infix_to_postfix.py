"""
================================================================================
EXPERIMENT 5: CONVERT INFIX EXPRESSION TO POSTFIX USING STACK
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To write a Python program that converts an Infix mathematical expression to a Postfix expression using the stack-based Shunting-Yard algorithm.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Stack Application / Shunting-yard variant
    - Time Complexity           : O(n)
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Experiment 5: Convert Infix to Postfix
def priority(op):
    if op == '^':
        return 3
    if op in "*/":
        return 2
    if op in "+-":
        return 1
    return 0

exp = input("Enter infix expression: ")
stack = []
postfix = ""

for ch in exp:
    if ch.isalnum():
        postfix += ch
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        if stack and stack[-1] == '(':
            stack.pop()
    elif ch in "+-*/^":
        while (stack and stack[-1] != '(' and
               priority(stack[-1]) >= priority(ch)):
            postfix += stack.pop()
        stack.append(ch)

while stack:
    postfix += stack.pop()

print("Infix expression  :", exp)
print("Postfix expression:", postfix)

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
Enter infix expression: (A + B) * (C - D) / (E + F) + G * H
Infix expression  : (A + B) * (C - D) / (E + F) + G * H
Postfix expression: AB+CD-*EF+/GH*+

** Process exited - Return Code: 0 **
================================================================================
"""
