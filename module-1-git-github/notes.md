# Module 1 — Git & GitHub

**Student:** Dizon, Adrian Kier T. 

**Date:** 9/27/2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is basically a tool that helps us keep track of the changes we make in our project. Like, if I change something in my code and then it suddenly breaks, I can use Git to go back to an older version. GitHub is different because it's a website where we can put our Git projects online. We can also use it to share our project and work with other people. So basically, Git is for tracking the changes, while GitHub is where we store and share the project online.

---

## Key vocabulary (in your own words)

- repository: Basically, this is the folder where our project and all its files are kept and tracked by Git.
- commit: It's like saving the changes you made at that point, so you have a record of what you did.
- branch: A separate version of the project where you can work on your changes without affecting the main branch.
- push / pull: Push is when you send your changes from your computer to GitHub. Pull is when you get the latest changes from GitHub to your computer.
- pull request: It's basically asking to add the changes from your branch into another branch, usually the main branch.
- merge conflict: This happens when two people change the same part of a file and Git doesn't know which change it should keep.

---

## Walking through what I did

First, I checked my current Git status and branches. Then I created and switched to my own branch called adrian. After making my changes, I checked the status again, added the changed files, and committed them with a message. After that, I pushed my branch to GitHub using git push -u origin adrian. Finally, I went to GitHub and created a pull request to merge my changes into the main branch.
```
git status
git branch
git switch -c adrian
git status
git add .
git commit -m "Update add notes feature"
git push -u origin adrian

```

---

## A mistake I made (or one I want to avoid)

One thing that confused me was the main branch. I accidentally used git switch -c main, which created a new local main branch instead of switching to the actual one. It didn't change the real main branch on GitHub, but it made things confusing for me. I learned that I should check which branch I'm currently on before doing anything, especially before making changes or pushing.

---

## How this connects to something else

For me, Git is kind of like saving different versions of a project. Instead of making a lot of copies like project_final, project_final2, or project_final_REAL, Git keeps track of the changes for me. This is also helpful when working with a group because everyone can work on their own branch without changing the main project.
