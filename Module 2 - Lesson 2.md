"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Dizon, Adrian Kier T.
Date: 9/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow is how we make the program decide what
to do based on a condition. For example, we can tell
the program to do something if a condition is true,
and do something else if it is false. We can use if,
elif, and else to handle different situations.


============================================
KEY VOCABULARY
============================================
- condition: Something that the program checks to see if it is true or false.
- if / elif / else: These are used to tell the program what to do depending on the condition.
- comparison operator: Symbols used to compare values, like ==, >, <, >=, and <=.
- boolean expression: An expression that results in either True or False.
- operator: A symbol used to perform a comparison or operation in the code.


============================================
MY OWN EXAMPLE(S)
============================================
I made an example that checks a student's grade.
The program checks the grade and gives a different
message depending on the result.


"""

grade = 85

if grade >= 90:
    print("Excellent!")
elif grade >= 75:
    print("You passed!")
else:
    print("You failed.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One thing that can be confusing is the difference
between = and ==. A single = is used to give a value
to a variable, while == is used to check if two values
are equal. I also need to remember the indentation
after if, elif, and else because Python uses it to
know which code belongs to the condition.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
I can use if and else in programs that need to make
decisions. For example, a student system can check
if a student passed or failed based on their grade.
It can also be used for things like checking a user's
age or deciding what message the program should show.
"""