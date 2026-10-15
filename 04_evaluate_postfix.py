"""
================================================================================
EXPERIMENT 4: EVALUATE POSTFIX EXPRESSION USING STACK
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To evaluate a Postfix (Reverse Polish) expression using a stack in Python.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Stack Application / Arithmetic Expression
    - Time Complexity           : O(n) where n is expression length
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Experiment 4: Evaluate Postfix Expression
exp = input("Enter postfix expression (e.g. 23*54*+): ")
stack = []

for ch in exp:
    if ch.isdigit():
        stack.append(int(ch))
    elif ch in "+-*/^":
        if len(stack) < 2:
            print("Invalid expression!")
            break
        b = stack.pop()
        a = stack.pop()

        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            if b == 0:
                print("Cannot divide by zero!")
                break
            stack.append(a // b)
        elif ch == '^':
            stack.append(a ** b)
    elif ch == ' ':
        continue
    else:
        print(f"Invalid character: {ch}")
        break
else:
    if len(stack) == 1:
        print("Postfix Expression:", exp)
        print("Evaluated Result   :", stack[0])
    else:
        print("Invalid postfix expression!")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
Enter postfix expression (e.g. 23*54*+): 5 3 2 * + 8 4 / - 6 2 * +
Postfix Expression: 5 3 2 * + 8 4 / - 6 2 * +
Evaluated Result   : 21

** Process exited - Return Code: 0 **
================================================================================
"""
