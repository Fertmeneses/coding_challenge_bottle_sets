# Open coding challenge: Bottle sets

This open coding challenge is designed to develop both **programming and data analysis skills**. Anyone can attempt their own solution, **the objective is to pass with 100% accuracy all test cases**. While efficienty in coding and analysis is a plus, the primary aim is accuracy in the solution.

## Introduction

In the following sections, you will find the **instructions** to solve the challenge and the **problem description**, which outlines the rules, objective and constrains. This challenge format was **inspired by the [Turing](https://www.turing.com/) platform**, where similar problems are proposed, combining data analysis skills along with coding, and the user has to solve it within a strict time limit, **just 45 minutes**! Here, you can take it easy and solve it at your own pace, or challenge yourself by setting a timer. Either way... have fun! 

## Instructions

### Files

The Github repository includes several files:

- **'Challenge_Description.txt'**: this plain file includes the problem description, task, examples and constrains. You will also find them further in this website.

- **'codes/challenge.py'**: this Python file is where you have to **implement your solution**. Only modify the section marked as '# Implement your code here'. The rest of the script runs your solution against the test cases.

- **'codes/test_cases.py'**: this script evaluates your solution using many (hidden) test cases and **returns your success rate** (e.g. "20% of the test cases were successful"). You don't need to use this file.

- **'codes/FM_solution.py'**: this file contains **my own solution**. Later I explain how to run it if you want to test it and play around.

### Running your solution

*Prerequisites (Python):*

**Linux system**: Ensure Python is installed. For assistance, refer to [how to install python on Linux](https://www.geeksforgeeks.org/how-to-install-python-on-linux/).

**Windows system**: Install a Python interpreter. For assistance, refer to [Python releases for Windows](https://www.python.org/downloads/windows/) and also [Using Python on Windows](https://docs.python.org/3/using/windows.html).

**MacOS system**: Ensure Python is installed. For assistance, you can refer to [how to install Python on Mac](https://www.dataquest.io/blog/installing-python-on-mac/) 👈🏽.

*General instructions:*

Open a terminal (Linux), PowerShell (Windows) or IDLE Shell (Mac) in the same directory as the python files and run:

```bash
python challenge.py
```

This line will return your solution's success rate on the the test cases.

### Running my solution (optional)

If you want to run my own solution, open the **'codes/test_cases.py'** file, comment the first line (put a hash # at the beggining) and uncomment the second line (remove the hash #). After the changes, the first line without any hash should be:

```python
from FM_solution import optim_sets
```

You can then revert these changes to evaluate your solution again.

## Problem description, task and constrains

Once you are familiar with the instructions, you can start the challenge. If you are setting a timer, start it as soon as you begin reading the following section.

<center><figure>
  <img src="https://github.com/Fertmeneses/coding_challenge_bottle_sets/blob/main/assets/Image_Conceptual_Bottles.jpg?raw=true" alt="Conceptual image"> 
  <figcaption><sup>Conceptual image, AI-generated using the prompt: "Two shelves with crystal bottles of many sizes and shapes, with an alchemist theme".</sup></figcaption>
</figure></center>

### Description

You are a seller of liquid products, which can be stored in bottles of any size. Recently, you received an unusual order: a client requests *'as many sets of bottles as possible, where each set consists of one or two bottles, and all sets must have the same total volume'*. The volume, measured in litres, can be any integer value, e.g. 1L or 5L, what matters is that you maximize the number of sets, as the mysterious client will pay you a very high amount per set, regardless of the liquid volume.

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

* The input list contains integer values within the range 1 to 100.
* The input list includes 1 to 100 elements.

---
---
---

## My solution

<center><figure>
  <img src="https://github.com/Fertmeneses/coding_challenge_bottle_sets/blob/main/assets/Spoiler_alert.png?raw=true" alt="Spoiler alert"> 
</figure></center>

Below, I explain my solution for this challenge, including the overall analysis and step-by-step breakdown of the code.

### Overall stragegy

The "Bottle sets" challenge is based on a relatively simple mathematical problem, or at least simple to enunciate. There are many ways to **build a solution**, ranging from **brute force**, by trying all possibilities within the input list, to **elegant mathematical formulae** that provides an exact description. Although the later seems the best approach, there is a competition between the time invested in the solution (up to 45 minutes if you take that challenge) and its elegance. As a consequence, my solution combines **some analysis and general rules with a bit of brute force**. While not the most efficient algorithm, this balance produces a functioning and simple code.

### Uniqueness of the solution 

The good news is that **for any given capacity value $C$**, the bottles in the input list $L$ can be arranged in a **unique combination using sets having up to 2 bottles**. Let me explain first the opposite case, and **imagine that the rules are different and the sets can include up to 3 bottles**:

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

It's clear that Configuration A, with 3 sets, is better than Configuration B, with only 2 sets. The takeaway message here is that **using up to 3 bottles per set, the configuration of bottles for any capacity $C$ may not be unique**. Therefore, it's necessary to first find all possible configurations and then choose the best one.

Now consider the **actual rule: sets can have up to 2 bottles**. For a single bottle $L_i$ with capacity $C_i$, there are three possible cases when a total capacity value $C$ is fixed for all sets:

1. If $C_i=C$, the bottle $L_i$ makes a single-bottle set. 
2. If $C_i>C$, the bottle $L_i$ is useless. 
3. If $C_i<C$, the bottle $L_i$ needs another bottle $L_j$ with capacity $C_j = C - C_i$.

Since this applies to all bottles in the input list, single bottles with capacity $C_i=C$ will form simple sets, while the other bottles will be arranged in sets $(C_i,C_j)$ that add $C_i+C_j=C$. The conclusion is: **for any capacity $C$, there is a unique configuration of bottles**. 

My **algorithm** makes use of this valuable information: it **finds the unique configuration for each capacity $C$, counts the number of sets, and chooses the highest count as the final answer**. Therefore, the main question becomes how to efficiently analyze all possible capacities...

#### The simplest algorithm

To set a baselie, meaning a basic code that just works, the **simplest algorithm** may analyze **all capacity values** ranging from the smallest capacity in the input list $C_{min} = \min(L)$ to the largest sum $C_{max} = \max(C_i+C_j)$ for any two bottles $(L_i,L_j)$, **one by one**. 

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

As you can imagine from the long list of possible capacities, this algorithm is **highly inefficient** as it analyzes **values that are not even feasible** for the input list.

#### A refined algorithm

A better approach is to analyze only **feasible capacity values**, using both **single- and two-bottle sets**.

<div class="warning" style='background-color:rgb(240, 241, 181); color:rgb(0, 0, 0); border-left: solid rgb(226, 194, 78) 4px; border-radius: 6px; padding:0.7em;'>
<span>
<p style='margin-top:0.1em; text-align:center'>
<b>Example of feasible capacity values </b></p>
<p style='margin-left:1em;'>

<b>Input list: [2,2,2,4,4,8,8,8]</b>. <br>
Single-bottle set capacities: [2,4,8]. <br>
Two-bottle set capacities: [4,6,8,10,12,16]. <br>
<b>Possible capacities: [2,4,6,8,10,12,16]</b>.

</p></span>
</div>
<br/><br/>

In this example, the **list of possible capacities is complete and none of the values are expendable**. Notice that the values $C=4$ and $C=8$ appear in both single- and two-bottle lists, as they can be reached in both ways.

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

Finally, let's explain the **full code, step by step**. For the sake of a good understanding, I will display segments of the code, one after the other, along with their explanation. Remember that you can view the original file [**codes/FM_solution.py**](https://github.com/Fertmeneses/coding_challenge_bottle_sets/blob/main/codes/FM_solution.py) in the Github repository.

```python
def optim_sets(stock):
	# 1. Identify sub-groups with equal values:
	vals = list(set(stock)) # Unique values
	groups = {val: stock.count(val) for val in vals} # key=capacity, value=counts  
#...
```

*Explanation:*

The first line identifies all capacity values from the input list by making a set, and then converts that set into a list $\color{teal}{\text{vals}}$ for future convenience.

The second line creates the dictionary $\color{teal}{\text{groups}}$ by counting all elements of each capacity value from the list $\color{teal}{\text{vals}}$, using the built-in method *count()*. Each dictionary key is a capacity value, and its respective value is the number of elements in the input list $\color{teal}{\text{stock}}$ with such capacity.

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

The list $\color{teal}{\text{sum\_vals}}$ comprises all the capacity values that can be made as a combination of any two single bottles. The first line just initiates the empty list, and the following two lines define a double loop to sample the combination of all elements ($i$,$j$) within the list of unique values $\color{teal}{\text{vals}}$. Inside the loop, each capacity result is added to the list. Once the loop is finished, the list is converted into a set to avoid repeated values, and then to a list for future convenience.

Notice that the double loop iterates over all indexes $i$ within $\color{teal}{\text{vals}}$, but the $j$ index starts from $i$ rather than 0. This avoids repetitions, as commutation of the elements $i$ and $j$ leads to the same sum result. On the other hand, the double loop allows to sum one element $i$ with itself ($j=i$), as the $\color{teal}{\text{stock}}$ list may include bottles with the same capacity. However, this coding block allows to include the value $\color{teal}{\text{vals}}[i]$+$\color{teal}{\text{vals}}[i]$ even when there is only a single bottle with capacity $\color{teal}{\text{vals}}[i]$ in the input $\color{teal}{\text{stock}}$ list. This little problem will be corrected later.

```python
#...
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

*Explanation:*

In this final block, the initial guess $\color{teal}{\text{best\_N}}$ (based on single-bottle sets) is compared to collections of sets with capacities from the $\color{teal}{\text{sum\_vals}}$ list, which by definition involve two-bottle sets, but can also include single-bottle sets.

The first line defines a loop over all capacity values within $\color{teal}{\text{sum\_vals}}$. Immediately after, for each capacity value an auxiliary list $\color{teal}{\text{check\_list}}$ is initiated, which takes note of the groups of bottles already used and avoid repeated counts. Also, a counting variable $\color{teal}{\text{n\_sum}}$ is defined (initialization is explained later), which accumulates the number of sets for the current capacity value and is finally compared whit $\color{teal}{\text{best\_N}}$.

The main idea is to use the $\color{teal}{\text{groups}}$ dictionary, which has the information about the bottle counts for each capacity value, rather than directly use the $\color{teal}{\text{stock}}$ list and make sets one by one. For a fixed capacity value $C$, a single key $C_i$ from $\color{teal}{\text{groups}}$ has several options:

1. $C_i = C$, then all bottles with capacity $C_i$ will be used as single-bottle sets. This is how the variable $\color{teal}{\text{n\_sum}}$ is initiated: $\color{teal}{\text{n\_sum}}=\color{teal}{\text{groups}}[C_i]$ if there are any bottles with capacity $C_i$, else $\color{teal}{\text{n\_sum}}=0$.

2. $C_i > C$, then all bottles with capacity $C_i$ won't be used.

3. $C_i = C/2$, then each pair of bottles with capacity $C_i$ will be used as a two-bottle set. The variable $\color{teal}{\text{n\_sum}}$ is updated in this way by dividing the $\color{teal}{\text{groups}}[C_i]$ by two and rounding down (a half pair coming from an odd number of bottles is not accepted).

4. $C_i < C$ **and** $C_i \neq C/2$, then all, some or none bottles with capacity $C_i$ will be used in two-bottle sets, which depends on the number of bottles with capacity $C_j = C - C_i$. If there are no bottles with capacity $C_j$, then none of the bottles with capacity $C_i$ will be used. If there is at least one bottle with capacity $C_j$, then, as any bottle $C_i$ needs a bottle $C_j$ to form a set with capacity $C$, the smallest group will determine how many sets can be made. Consequently, the variable $\color{teal}{\text{n\_sum}}$ is updated by the smallest number of bottles $\color{teal}{\text{groups}}[C_i]$ or $\color{teal}{\text{groups}}[C_j]$.

The code describes all these options for the $C_i$ capacities by iterating over the $\color{teal}{\text{val\_i}}$ values within $\color{teal}{\text{groups}}$. Option #1 is taken into account right at the beginning, when $\color{teal}{\text{n\_sum}}$ is initiated. All other options come next, and for them the complement capacity $C_j = C - C_i$ is defined as $\color{teal}{\text{val\_j}}$. To avoid repetitions within the loop, there is control stage that checks if any of the keys $\color{teal}{\text{val\_i}}$ or $\color{teal}{\text{val\_j}}$ were already analyzed, in which case the loop continues without any further actions. If neither keys were analyzed yet, both $\color{teal}{\text{val\_i}}$ and $\color{teal}{\text{val\_j}}$ values are added to the $\color{teal}{\text{check\_list}}$ and the process continues as described below.

If $\color{teal}{\text{val\_i}}$ is half the current capacity value, meaning $C_i = C/2$ (option #3), then $\color{teal}{\text{n\_sum}}$ is updated accordingly. Else, there is a condition that checks if the complement capacity $\color{teal}{\text{val\_j}}$ is within $\color{teal}{\text{groups}}$ (option #4), and updates $\color{teal}{\text{n\_sum}}$ accordingly. Notice that option #2 is implicitely included in this step, as $C_i>C$ implies $C_j<0$, then $\color{teal}{\text{val\_j}}$ can't be included in $\color{teal}{\text{groups}}$.

As a final step within the main loop (over $\color{teal}{\text{sum\_vals}}$), the final counts $\color{teal}{\text{n\_sum}}$ for each capacity $C$ is compared with $\color{teal}{\text{N\_best}}$, and the maximum value from ($\color{teal}{\text{N\_best}}$,$\color{teal}{\text{n\_sum}}$) is defined as the new (or old) optimal number of sets.

Once the main loop is finished, the function $\color{teal}{\text{optim\_sets}}$ returns the optimal number of sets $\color{teal}{\text{N\_best}}$.

#### Comments and invitation to collaborate

My solution passes 100% of the test cases, meaning it works fine. I'm sure there is room for improvement, so any feedback is very welcome. You can contact me via [LinkedIn](https://www.linkedin.com/in/fernando-meneses-unc/) or email (fertmeneses@gmail.com).

Also, I invite you to join the [GitHub project](https://github.com/Fertmeneses/coding_challenge_bottle_sets) as a collaborator and upload your own solution if you want to share it.

![Banner](https://github.com/Fertmeneses/coding_challenge_bottle_sets/blob/main/assets/Banner.png?raw=true)

