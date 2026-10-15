"""
================================================================================
EXPERIMENT 5: EVALUATION OF A POSTFIX EXPRESSION USING A STACK
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To evaluate a Postfix (Reverse Polish) expression using the stack
    data structure in Python.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Stack Application / Arithmetic Expression
    - Algorithm                 :
        1. Scan tokens from left to right.
        2. If operand, push onto stack.
        3. If operator, pop two operands (b, then a), compute result, and push back.
        4. Final result remains as the single element on the stack.
    - Supported Operators       : +, -, *, /, ^ (exponentiation)
    - Time Complexity           : O(n) where n is the number of tokens
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Evaluation of a Postfix Expression using a Stack

def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():                 # operand -> push
            stack.append(int(token))
        else:                               # operator -> pop two, calculate, push
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)
    return stack.pop()

# Main program
exp = input("Enter postfix expression (separate with spaces, e.g. 2 3 1 * + 9 -): ")
print("Result =", evaluate_postfix(exp))

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
Enter postfix expression (separate with spaces, e.g. 2 3 1 * + 9 -): 2 3 1 * + 9 -
Result = -4
================================================================================
"""
