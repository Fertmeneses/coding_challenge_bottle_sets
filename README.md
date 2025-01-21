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

I start my algorithm with the **easiest option: making sets with single bottles**. Within the input list $L$, I count all elements that share the same capacity value $C_i$. The result is a **collection** {$C$}, which represents the **number of sets** that can be made **for each value $C$** using just **single bottles**.

As a first guess for the optimal number of sets, I choose the best option within the collection {$C$}. I name this guess $N_1$. This is the starting point, the next step will take care of a more refined analysis and check if there is a better value than $N_1$. 

### Part 2: Sets with combined bottles

#### Uniqueness of the solution 

It is now time to consider those sets that can be made using a combination of two bottles. The good news is that **for a given value $C$**, the bottles within the input list $L$ can be arranged in a **unique combination using sets having up to 2 bottles**. Let me explain first the opposite case, and **imagine that the rules are different and I can make sets of up to 3 bottles**:

<div class="warning" style='background-color:rgb(240, 241, 181); color:rgb(0, 0, 0); border-left: solid rgb(226, 194, 78) 4px; border-radius: 6px; padding:0.7em;'>
<span>
<p style='margin-top:0.1em; text-align:center'>
<b>Example for rule "Sets can have up to 3 bottles" </b></p>
<p style='margin-left:1em;'>

Input list: [1,1,2,2,3,4]. <br>
Capacity for all sets: $C=4$. <br>
Configuration A (sets): [2,2] + [3,1] + [4]. <br>
Configuration B (sets): [1,1,2] + [4].

</p></span>
</div>
<br/><br/>

It's clear that the Configuration A, with 3 sets, is better than the Configuration B, with only 2 sets. The main message here is that, **using up to 3 bottles per set, the configuration of bottles for each capacity $C$ may not be unique**, then it's necessary to find them all and choose the best one.

Now let's consider the **actual rule: sets can have up to 2 bottles** and analyze a single bottle $L_i$ within the input list, with a capacity $c_i$ There are three possible cases when we choose a fixed value $C$ for all sets:

1. If $c_i=C$, then the bottle $L_i$ makes a single set. 
2. If $c_i>C$, the bottle $L_i$ is useless. 
3. If $c_i<C$, the bottle $L_i$ needs another bottle $L_j$ with capacity $c_j = C - c_i$.

As this is valid for all bottles within the input list, single bottles with capacity $c_i=C$ will make simple sets, while the other bottles will be arranged in sets $(c_i,c_j)$ that add $c_i+c_j=C$. The conclusion is: **for any capacity $C$ there is a unique configuration of bottles**. 

My **algorithm** will make use of this valuable information: it will **find the unique configuration for each capacity $C$ and count the number of sets $n_C$**. The highest number will be the final answer. Therefore, the main question becomes how to analyze all possible $C$ values... If the algorithm doesn't take into account all $C$ values, then there is no certainty that its output will be correct. On the other hand, a complete but inefficient analysis will find the right answer at the expense of too long computing times. My objective is to **design a method that analyzes all possible $C$ values as efficiently as possible**.

#### The simplest algorithm

To set a lower limit, the **simplest algorithm** may analyze **all $C$ values** ranging from the minimum capacity in the input list $C_{min} = \min(L)$ to the highest sum $C_{max} = \max(L_i+L_j)$, **one by one**. 

<div class="warning" style='background-color:rgb(240, 241, 181); color:rgb(0, 0, 0); border-left: solid rgb(226, 194, 78) 4px; border-radius: 6px; padding:0.7em;'>
<span>
<p style='margin-top:0.1em; text-align:center'>
<b>Example for simple algorithm analyzing a full range of capacity values </b></p>
<p style='margin-left:1em;'>

<b>Input list: [2,2,2,4,4,8,8,8]</b>. <br>
Minimum capacity: $C_{min}=2$. <br>
Maximum capacity: $C_{max}=8+8=16$. <br>
<b>Possible capacities: [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]</b>.

</p></span>
</div>
<br/><br/>

As you can imagine from the long list of possible capacities, this algorithm is **very inefficient** as it analyzes **values that are not even possible** for the input list.

#### A refined algorithm

A better version of the previous algorithm is one that analyzes only possible capacity values. As **my code** already took a **first guess based on single-bottle sets**, I will avoid repetitions and in **this step** I only take into account capacities that are made of **sets of two bottles**.

<div class="warning" style='background-color:rgb(240, 241, 181); color:rgb(0, 0, 0); border-left: solid rgb(226, 194, 78) 4px; border-radius: 6px; padding:0.7em;'>
<span>
<p style='margin-top:0.1em; text-align:center'>
<b>Example of my code analyzing all possible capacity values </b></p>
<p style='margin-left:1em;'>

<b>Input list: [2,2,2,4,4,8,8,8]</b>. <br>
Single-bottle set capacities: [2,4,8]. <br>
Two-bottle set capacities: [4,6,8,10,12,16]. <br>
<b>Possible capacities: [2,4,6,8,10,12,16]</b>.

</p></span>
</div>
<br/><br/>

In this example, the **list of possible capacities is complete and none of the values are expendable**. Notice that the values $C=4$ and $C=8$ are shared by both single-bottle and two-bottle lists, as they can be reached in both ways.

### Code: step by step

Now that I've explained my reasoning, I will introduce a pseudo-code first and then explain all the details of the full code.

#### Pseudo-code

The following coding block is the simplified version of my original code, in which the **main steps are described and fictional functions are called**, such as "count_bottles". Later, in the full description, this auxiliar functions will be replaced by a more complex structure.

```python
def optim_set(stock):
  """
  From the input {stock} list, return the optimal number...
  of one- and two-bottle sets that can be made with a...
  common total capacity value.
  """ 
  # 1. Count bottles for each capacity value, store them in dictionary with [key = capacity], [value = number of bottles]
  groups = {C: count_bottles(stock,C) for C in stock}

  # 2. Make a first guess for optimal number of sets using only single-bottle sets:
  best_N = max(groups.values())

  # 3. Identify the capacities of all two-bottle sets:
  C_sum = [C_i+C_j for (C_i,C_j) in groups]

  # 4. For values in C_sum, count sets and improve {N_best} if possible:
	for C in C_sum:
    n_sets = count_sets(C,groups)
		best_N = max(best_N,n_sets)

  # Finally, return optimal number of sets:
  return best_N
```
#### Full description of the original code

Finally, let's explain the **full code, step by step**. For the sake of a good understanding, I will display segments of the code, one after the other, explaining the lines in-between. Remember that you can view the original file [**codes/FM_solution.py**](https://github.com/Fertmeneses/coding_challenge_bottle_sets/blob/main/codes/FM_solution.py) in the Github repository.

```python
def optim_sets(stock):
	# 1. Identify sub-groups with equal values:
	vals = list(set(stock)) # Unique values
	groups = {val: stock.count(val) for val in vals} # key=capacity, value=counts  
#...
```

*Explanation:*

The first line identifies all capacity values from the input list by making a set, and then converts that set into a list $\color{teal}{\text{vals}}$ for future convenience.

The second line creates the dictionary $\color{teal}{\text{groups}}$ by counting all elements with each capacity value from the list $\color{teal}{\text{vals}}$ with the built-in method *count()*. Each dictionary key is a capacity value, and its respective value is the number of elements in the input list $\color{teal}{\text{stock}}$ with that capacity.

Note: the second line is equivalent to use the *Counter* object from the **collections** library:

```python
# Equivalent method (not in original code):
from collections import Counter
groups = Counter(stock)
```

However, I preferred to used as many built-in methods as possible in this challenge, and avoid importing libraries so the code is more transparent to the reader. Let's continue:

```python
#...
  # 2. First guess with single-bottle sets:
  best_N = max(groups.values())
#...
```

*Explanation:*

This simple step just chooses the highest counts value within the $\color{teal}{\text{groups}}$ dictionary. Notice that the capacity associated to that counts value is not important for the final challenge answer, then it's not necessary to keep track of it.

```python
#...
  # 3. Identify the capacities of all two-bottle sets:
  sum_vals = [] # Initiate
	for i in range(len(vals)):
	  for j in range(i,len(vals)):
		  sum_vals.append(vals[i]+vals[j])
	sum_vals = list(set(sum_vals))
#...
```

*Explanation:*

The list $\color{teal}{\text{groups}}$ comprises all the capacity values that can be made as a combination of any two single bottles.
The first line just initiates the empty list, and the following two lines define a double loop to sample the combination of all elements ($i$,$j$) within the list of unique values $\color{teal}{\text{vals}}$. Inside the loop, each capacity result is added to the list.

Notice that the double loop iterates over all indexes $i$ within $\color{teal}{\text{vals}}$, but the $j$ index starts from $i$ rather than 0. This avoids repetitions, as commutation of the elements $i$ and $j$ leads to the same sum result. On the other hand, the double loop allows to sum one element $i$ with itself ($j=i$), as the $\color{teal}{\text{stock}}$ list may include bottles with the same capacity. However, this coding block allows to include the value $\color{teal}{\text{vals}}[i]$+$\color{teal}{\text{vals}}[i]$ even when there is only a single bottle with capacity $\color{teal}{\text{vals}}[i]$ in the input $\color{teal}{\text{stock}}$ list. This little problem will be corrected later.

Finally, the last line of the block converts the list into a set to avoid repeated values, and then to a list for future convenience.

```python
  # 4. Count two-bottle sets and update first guess if needed:
  for sum_val in sum_vals:
		check_vals = []
		n_sum = groups[sum_val] if sum_val in groups else 0
		for val_i in groups:
			val_j = sum_val-val_i
			if val_i not in check_vals:
				check_vals += [val_i,val_j]
				if val_i == val_j:
					n_sum += int(groups[val_i]/2)
				elif val_i != val_j and val_j in groups:
					n_sum += min([groups[val_i],groups[val_j]])
		best_N = max([best_N,n_sum])

  return best_N
```

In this final block, the initial guess $\color{teal}{\text{best\_N}}$ (based on single-bottle sets) is compared to collections of sets with capacities from the $\color{teal}{\text{sum\_vals}}$ list, which by definition involve sets of two bottles, but can also include single-bottle sets.

The first line defines a loop over all capacity values within $\color{teal}{\text{sum\_vals}}$. Immediately after, for each capacity value an auxiliary list $\color{teal}{\text{check\_list}}$ is initiated, that takes note of the group of bottles already used and avoid repeated counts. Also, a counting variable $\color{teal}{\text{n\_sum}}$ is defined (explained later), which accumulates the number of sets for the current capacity value and is finally compared whit $\color{teal}{\text{best\_N}}$.

The main idea is to use the $\color{teal}{\text{groups}}$ dictionary, which has the information about the bottle counts for each capacity value, rather than directly use the $\color{teal}{\text{stock}}$ list and make sets one by one. For a fixed capacity value $C$, a single key $C_i$ from $\color{teal}{\text{groups}}$ has several options:

1. $C_i = C$, then all bottles with capacity $C_i$ will be used as single-bottle sets. This is how the variable $\color{teal}{\text{n\_sum}}$ is initiated: $\color{teal}{\text{n\_sum}}$=$\color{teal}{\text{groups}}[C_i]$ if any, else $\color{teal}{\text{n\_sum}}=0$.

2. $C_i > C$, then all bottles with capacity $C_i$ won't be used.

3. $C_i = C/2$, then each pair of bottles with capacity $C_i$ will be used as a two-bottle set. The variable $\color{teal}{\text{n\_sum}}$ is updated in this way by dividing the $\color{teal}{\text{groups}}[C_i]$ by two and rounding down.

4. $C_i < C$ **and** $C_i \neq C/2$, then all, some or none bottles with capacity $C_i$ will be used in two-bottle sets, which depends on the number of bottles with capacity $C_j = C - C_i$. If there are no bottles with capacity $C_j$, then none of the bottles with capacity $C_i$ will be used. If there is at least one bottle with capacity $C_j$, then, as any bottle $C_i$ needs a bottle $C_j$ to form a set with capacity $C$, the smallest group will determine how many sets can be made. Consequently, the variable $\color{teal}{\text{n\_sum}}$ is updated by the smallest number of bottles within $\color{teal}{\text{groups}}[C_i]$ and $\color{teal}{\text{groups}}[C_j]$.

The code describes all these options for the $C_i$ capacities by iterating over the $\color{teal}{\text{val\_i}}$ values within $\color{teal}{\text{groups}}$. Option #1 is taken into account right at the beginning, when $\color{teal}{\text{n\_sum}}$ is initiated. All other options come next, and for them the complement capacity $C_j = C - C_i$ is defined as $\color{teal}{\text{val\_j}}$. To avoid repetitions within the loop, there is control stage that checks if any of the keys $\color{teal}{\text{groups}}[C_i]$ or $\color{teal}{\text{groups}}[C_i]$ were already analyzed, in which case the loop continues without any further actions. If not, both $\color{teal}{\text{val\_i}}$ and $\color{teal}{\text{val\_j}}$ values are added to the $\color{teal}{\text{check\_list}}$ and the process continues as described below.

If $\color{teal}{\text{val\_i}}$ is half the current capacity value, meaning $C_i = C/2$ (option #3), then $\color{teal}{\text{n\_sum}}$ is updated accordingly. Else, there is a condition that checks if the complement capacity $\color{teal}{\text{val\_j}}$ is within $\color{teal}{\text{groups}}$ (option #4), and updates $\color{teal}{\text{n\_sum}}$ accordingly. Notice that option #2 is implicitely included in this step, as $C_i>C$ implies $C_j<0$, then $\color{teal}{\text{val\_j}}$ won't be included in $\color{teal}{\text{groups}}$.


CONTINUE FROM HERE...




![Banner](httplink)

