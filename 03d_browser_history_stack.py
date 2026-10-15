"""
================================================================================
EXPERIMENT 3D: SIMPLE BROWSER HISTORY NAVIGATION USING STACK
================================================================================
Practical Lab Record : Data Structures & Algorithms (MCA Sem 1)
Student Name         : Dwadasi Venkata Sri Sai Kumar
Roll Number          : 26MCAP101N007
Faculty Mentor       : Mr. Sachin Sharma
Institution          : School of Computer Applications, MRIIRS

AIM:
    To simulate web browser navigation history (visiting pages, going back, and viewing current URL) using the Stack concept.

TECHNICAL SPECIFICATIONS:
    - Data Structure / Paradigm : Stack Application / Browser Simulation
    - Time Complexity           : Visit: O(1), Back: O(1), View: O(n)
    - Auxiliary Space Complexity: O(n)
================================================================================
"""

# Experiment 3D: Simple Browser History using Stack
history = []
current = -1

while True:
    print("\n--- BROWSER NAVIGATION MENU ---")
    print("1. Visit page")
    print("2. Back")
    print("3. Current page")
    print("4. Full History")
    print("5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        page = input("Enter page URL: ")
        history = history[:current + 1]
        history.append(page)
        current += 1
        print(f"Visited: {page}")

    elif choice == 2:
        if current > 0:
            current -= 1
            print(f"Moved BACK to: {history[current]}")
        else:
            print("No previous page in history!")

    elif choice == 3:
        if current == -1:
            print("No page currently opened.")
        else:
            print("Current page:", history[current])

    elif choice == 4:
        print("History Stack:", history, f"| Active Index: {current}")

    elif choice == 5:
        print("Exiting browser simulation...")
        break
    else:
        print("Invalid choice!")

"""
================================================================================
SAMPLE TERMINAL EXECUTION & VERIFICATION:
================================================================================
--- BROWSER NAVIGATION MENU ---
1. Visit page
2. Back
3. Current page
4. Full History
5. Exit
Enter choice: 1
Enter page URL: https://www.google.com/
Visited: https://www.google.com/

--- BROWSER NAVIGATION MENU ---
1. Visit page
2. Back
3. Current page
4. Full History
5. Exit
Enter choice: 3
Current page: https://www.google.com/

--- BROWSER NAVIGATION MENU ---
1. Visit page
2. Back
3. Current page
4. Full History
5. Exit
Enter choice: 1
Enter page URL: https://www.instagram.com/
Visited: https://www.instagram.com/

--- BROWSER NAVIGATION MENU ---
1. Visit page
2. Back
3. Current page
4. Full History
5. Exit
Enter choice: 4
History Stack: ['https://www.google.com/', 'https://www.instagram.com/'] | Active Index: 1

--- BROWSER NAVIGATION MENU ---
1. Visit page
2. Back
3. Current page
4. Full History
5. Exit
Enter choice: 2
Moved BACK to: https://www.google.com/

--- BROWSER NAVIGATION MENU ---
1. Visit page
2. Back
3. Current page
4. Full History
5. Exit
Enter choice: 5
Exiting browser simulation...

** Process exited - Return Code: 0 **
================================================================================
"""
