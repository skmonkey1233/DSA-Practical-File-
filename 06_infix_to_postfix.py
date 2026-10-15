"""
================================================================================
EXPERIMENT 6: CONVERSION OF INFIX EXPRESSION TO POSTFIX USING A STACK
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To write and execute a Python program that converts an Infix mathematical
    expression to a Postfix (Reverse Polish) expression using the stack data structure.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Stack (LIFO) / Shunting-Yard Algorithm
    - Operator Precedence       :
        * Exponentiation (^)    : Precedence 3 (Right associative)
        * Multiplication, Division (*, /) : Precedence 2
        * Addition, Subtraction (+, -)    : Precedence 1
    - Time Complexity           : O(n) where n is expression length
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Conversion of Infix Expression to Postfix Expression using a Stack

def precedence(op):
    if op == '^':
        return 3
    if op in '*/':
        return 2
    if op in '+-':
        return 1
    return 0

def infix_to_postfix(expression):
    stack = []
    result = ""
    for ch in expression:
        if ch.isalnum():                    # operand -> add to result
            result += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()                     # remove '('
        else:                               # operator
            while stack and precedence(stack[-1]) >= precedence(ch) and ch != '^':
                result += stack.pop()
            stack.append(ch)
    while stack:
        result += stack.pop()
    return result

# Main program
exp = input("Enter infix expression (e.g. A+B*C): ").replace(" ", "")
print("Postfix expression =", infix_to_postfix(exp))

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
Enter infix expression (e.g. A+B*C): (A + B) * (C - D) / (E + F) + G * H
Postfix expression = AB+CD-*EF+/GH*+
================================================================================
"""
