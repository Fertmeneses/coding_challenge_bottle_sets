# Open coding challenge: Bottle sets

This open coding challenge aims to develop both **programming and data analysis skills**. Any user can try their own solution, **the objective is to pass with 100% accuracy all test cases**, while coding and analysis efficiency is a plus.

## Introduction

In the following sections, you will find the **instructions** to solve the challenge and the **problem description**, in which the rules, objective and constrains are described. The format of this challenge was **inspired by the [Turing](https://www.turing.com/) platform**, in which a similar problem is proposed, combining data analysis skills along with coding, and the user has to solve it within a strict time limit, **just 45 minutes**! Here, you can take it easy and do it at your own pace, or you can challenge yourself and set your timer. In any case... have fun! 

## Instructions

### Files

Within the repository files, the file **'codes/challenge.py'** contains a Python code in which you have to **propose a solution** for the problem. Only modify the part that says '# Implement your code here', the rest takes care of running the proposed solution against the test cases.

There is another file, **'codes/test_cases.py'**, in which the solution will be evaluated for many (hidden) test cases, and the **results will be returned as the success rate** (e.g. "20% of the test cases were successful"). You don't have to use that file.

Lastly, **my own solution** is available in the file **'codes/FM_solution.py'**. Although it passes all test cases, I'm sure that its efficiency can be improved, so any feedback, discussions and contributions are very welcome.

### Running your solution

**Linux system**: Make sure you have Python installed, if you need any help you can visit this link:

[Website: how to install python on Linux](https://www.geeksforgeeks.org/how-to-install-python-on-linux/) 👈🏽.

**Windows system**: Make sure you have a Python interpreter installed, if you need any help you can use the following links:

[Website: Python releases for Windows](https://www.python.org/downloads/windows/) 👈🏽.
[Website: Using Python on Windows](https://docs.python.org/3/using/windows.html) 👈🏽.

**MacOS system**: Make sure you have Python installed, if you need any help you can visit this link:

[Website: how to install python on macOS](https://www.dataquest.io/blog/installing-python-on-mac/) 👈🏽.

**General**: Whatever the operating system, open the Linux terminal / Windows PowerShell / macOS IDLE Shell in the same folder as the python files. From there, run:
```
python challenge.py
```
This line will return the success rest of your solution when evaluated on the the test cases. By default (no solution yet), none of the test cases will be passed, meaning 0% success rate.

### Running my solution (optional)

If you want to run my own solution, then you can open the **'codes/test_cases.py'** file, comment the first line (put a hash # at the beggining) and uncomment the second line (remove the hash #). After the changes, the first line without any hash should be:
```
from FM_solution import optim_sets
```
You can undo these changes and the challenge will evaluate your solution again.

## Problem description, task and constrains

Once you are familiar with the instructions, you can start the challenge. If you are going to use a timer and try to complete it within 45 minutes, you should start it as soon as you start reading the following section.

Note: you can also find the challenge description in the file **'Challenge_Description.txt'** within the repository.

<center><figure>
  <img src="https://github.com/Fertmeneses/coding_challenge_bottle_sets/blob/main/assets/Image_Conceptual_Bottles.jpg?raw=true" alt="Conceptual image"> 
  <figcaption><sup>Conceptual image, AI-generated using the prompt "Two shelves with crystal bottles of many sizes and shapes, with an alchemist theme".</sup></figcaption>
</figure></center>

### Description

You are a seller of liquid products, which can be stored in bottles of any size. Recently, you received an unusual order: a client requests *'as many sets of bottles as possible, where each set consists of one or two bottles, and all sets must have the same total volume'*. The volume, measured in litres, can be any integer value, for example 1L or 5L, what matters is that you maximize the number of sets, as the mysterious client will pay you a very high amount per set, regardless of the liquid volume.

### Task

Design an algorithm that takes as **input** a **list of bottle capacities** (in litres) available in your store, and **returns the maximum number of sets** that can be made. Each set must have one or two bottles, and the total volume of each set must be the same across all sets.

### Examples

| Input | Output | Explanation |
| :---- | :----: | :---- |
| [1,1,2,2,5,5] | 3 | Three sets with 2L each: [1,1] + [2] + [2] |
| [1,1,3,5] | 2 | Two sets with 1L each: [1] + [1] |
| [1,2,5,6,10,11,20] | 3 | Three sets with 11L each: [1,10] + [5,6] + [11] |
| [12] | 1 | Single set with 12L: [12] |
| [1,1,5,5] | 2 | Either two sets of 1L: [1] + [1]; two sets of 5L: [5] + [5]; or two sets of 6L: [1,5] + [1,5] |

### Constrains:

* The input list will only have integer values within the range 1 to 100.
* The input list will have from 1 to 100 elements.

INTRODUCE SOME BREAK
/----------
/----------


SPOILER ALERT! Maybe an image, like a red seal.

## My solution

Introduction

### Analysis and ideas

Description

### Code: step by step

Description

![Banner](httplink)

