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

[Website: how to install Python on Mac](https://www.dataquest.io/blog/installing-python-on-mac/) 👈🏽.

**General**: Whatever the operating system, open the Linux terminal / Windows PowerShell / Mac IDLE Shell in the same folder as the python files. From there, run:
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

---
---
---

## My solution

<center><figure>
  <img src="https://github.com/Fertmeneses/coding_challenge_bottle_sets/blob/main/assets/Spoiler_alert.png?raw=true" alt="Spoiler alert"> 
</figure></center>

In the following, I explain my own solution for this challenge. I'll describe the overall analysis and main ideas, and the programming code step by step. 

### Overall stragegy

The "Bottle sets" challenge is based on a relatively simple mathematical problem, or at least simple to enunciate. There are many ways to **build a solution**, **from using brute force** and try all possibilities within the input list, **to find an optimal formula** that provides an elegant solutions. Although the later seems the best approach, there is a competition between the time invested in the solution (up to 45 minutes if you take that challenge) and its elegance. As a consequence, in my solution **I elaborate some analysis and general rules, but also make use of some brute force**. This balance produces a functioning code, which passes all test cases, although not the most efficient one.

### Part 1: Sets with single bottles

I start my algorithm with the **easiest option: making sets with single bottles**. Within the input list $L$, I count all elements that share the same capacity value $C_i$. The result is a **collection $\{C\}$**, which represents the **number of sets** that can be made **for each value $C$** using just **single bottles**.

As a first guess for the optimal number of sets, I choose the best option within the collection $\{C\}$. I name this guess $N_1$. This is the starting point, the next step will take care of a more refined analysis and check if there is a better value than $N_1$. 

### Part 2: Sets with combined bottles

It is now time to consider those sets that can be made using a combination of two bottles. The good news is that **for a given value $C$**, the bottles within the input list $L$ can be arranged in a **unique combination using sets having up to 2 bottles**. Let me explain first the opposite case, and **imagine that the rules are different and I can make sets of up to 3 bottles**:

Input list: [1,1,2,2,3,4].
Rule: sets can have up to three bottles.
Capacity: $C=4$.
Configuration A: [2,2] + [3,1] + [4]
Configuration B: [1,1,2] + [4]

It's clear that the Configuration A, with 3 sets, is better than the Configuration B, with only 2 sets. The main message here is that, **using up to 3 bottles per set, the configuration of bottles for each capacity $C$ may not be unique**, then it's necessary to find them all and choose the best one.

Now let's consider the **actual rule: sets can have up to 2 bottles** and analyze a single bottle $L_i$ within the input list, with a capacity $c_i$. There are three possible cases when we choose a fixed value $C$ for all sets:

1. If $c_i=C$, then the bottle $L_i$ makes a single set. 
2. If $c_i>C$, the bottle $L_i$ is useless. 
3. If $c_i<C$, the bottle $L_i$ will form a useful set **only** if there is another bottle $L_j$ with capacity $c_j = C - c_i$.

As this is valid for all bottles within the input list, single bottles with capacity $c_i=C$ will make simple sets, while the other bottles will be arranged in sets $(c_i,c_j)$ that add $c_i+c_j=C$. The conclusion is: **for any capacity $C$ there is a unique configuration of bottles**. 

My **algorithm** will make use of this valuable information: it will **find the unique configuration for each capacity $C$ and count the number of sets $n_C$**. The highest number will be the final answer. However, what I did not determine yet is how to find all possible $C$ values...

%%%% EXPLAIN BRUTE FORCE METHOD, FROM C=LOWEST TO C=HIGHEST SUM.
%%%% THEN EXPLAIN MY METHOD AND WHY I COMPARE WITH N_1.



### Code: step by step

Description

![Banner](httplink)

