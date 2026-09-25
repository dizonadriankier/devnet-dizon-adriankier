"""
Module 2 — Activity: File Sorting with os and shutil
Student: Dizon, Adrian Kier T.
Date: 09/27/2026

============================================

WHAT DID YOU BUILD? 
I made a simple Python program that sorts files into different folders. 
It checks the file extension to know what type of file it is. 
For example, if it is a JPG or PNG, it puts it in the Images folder. 
If it is a PDF or DOCX, it puts it in the Documents folder. 
I made it so I would not have to move the files one by one.

============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]

============================================
KEY VOCABULARY
============================================
- os module:
- shutil module:
- file path:
- directory:
(add more as needed)

============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""
import os
import shutil

folder = "files"

images = folder + "/Images"
documents = folder + "/Documents"

os.makedirs(images, exist_ok=True)
os.makedirs(documents, exist_ok=True)

for file in os.listdir(folder):

    if file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(folder + "/" + file, images + "/" + file)

    elif file.endswith(".pdf") or file.endswith(".docx"):
        shutil.move(folder + "/" + file, documents + "/" + file)

print("Files sorted!")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One thing I got confused about was the file path. 
I wasn't sure at first where I should put the files and folders for the code to work. 
I also learned that the Images and Documents folders need to be there before the files can be moved, so I added code that creates them automatically.
  
============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This can help me as a student because I usually have a lot of files for different subjects and projects. 
Sometimes my files can get mixed together in one folder. 
A program like this can automatically sort my documents, pictures, and other files into different folders. 
It can save me time and make it easier for me to find the files I need.
