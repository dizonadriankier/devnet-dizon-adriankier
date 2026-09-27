"""
Module 2 — Lesson 3: Loops & Lists
Student: Dizon, Adrian Kier T.
Date: 9/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Lists are used when we want to store multiple
values in one place. For example, we can have a
list of names or grades. Loops are useful when we
want to repeat something without writing the same
code many times. A for loop can go through each
item in a list, while a while loop keeps running
as long as a condition is true.


============================================
KEY VOCABULARY
============================================
- list: A group of values stored together in one variable.
- for loop: A loop that repeats for each item in a list or other group of values.
- while loop: A loop that keeps running while a condition is true.
- index: The position of an item inside a list. The first item starts at 0.
- iteration: One time that a loop runs.
- item: One value stored inside a list.


============================================
MY OWN EXAMPLE(S)
============================================
I made an example using a list of subjects.
The for loop goes through each subject and prints
it one by one.


"""

subjects = ["CybSec", "DevNet", "SysAdm", "Elective 1"]

for subject in subjects:
    print("My subject is:", subject)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One thing that was confusing to me was that the
index of a list starts at 0 instead of 1. So if I
have a list with three items, the positions are 0,
1, and 2. I also need to be careful with while
loops because if the condition never becomes false,
the loop can keep running.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
I can use lists and loops when working with a lot
of information. For example, if a program has a
list of students, a loop can go through the list
and display each student's name without having to
write a print statement for every student.
"""