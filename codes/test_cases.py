from challenge import optim_sets
#from FM_solution import optim_sets

def make_blocks(values,samples):
    """
    Build 'blocks' of bottles with fixed values (represented by their
    capacity in litres), and then combine them in a single list. Also,
    calculate the optimal number of sets according to the challenge rules.

    --- Inputs ---
    {values} [List]: Elements must be integers, representing the
    capacity of each block of bottles.
    {samples} [List]: Elements must be integers, representing the
    number of bottles in each block (correlative to {values}).

    --- Outputs ---
    {block} [List]: List with all bottles, each one represented by
    its capacity in litres.
    {N} [Integer]: Optimal number of sets, according to the challenge
    rules.
    """

    # Raise error if input lists have different size:
    if len(values)!=len(samples):
        raise ValueError("The two input lists must have the same number of elements.")
    # Raise error if {values} list have duplicated values:
    seen = set()
    for x in values:
        if x in seen:
            raise ValueError("First list must not have duplicated values.")
        seen.add(x)

    # Build the full list of bottles:
    all_blocks = [] # Initiate
    for i in range(len(values)):
        # Generate a block:
        block = [values[i] for _ in range(samples[i])]
        # Update full block:
        all_blocks += block

    # Calculate optimal number of sets (solution):
    N = max(samples) # Initiate a priori solution
    # Check all possible sums:
    sum_vals = [] # Initiate
    for i in range(len(values)):
        for j in range(i,len(values)):
            sum_vals.append(values[i]+values[j]) # Add the sum value
    sum_vals = list(set(sum_vals)) # Erase repetitions
    # Count sets according to sums:
    for sum_val in sum_vals:
        check_vals = [] # Auxiliar list to avoid repeated counts
        # Initiate counts with the summing value itself:
        n_sum = samples[values.index(sum_val)] if sum_val in values else 0
        # Sum the contribution of each pair of correct values:
        for i in range(len(values)):
            val_i = values[i] # Identify value
            # Check if there is a pair with this sum value:
            val_j = sum_val-val_i # Proposed matching value
            if val_j in values and val_i not in check_vals:
                check_vals += [val_i,val_j] # Update check list
                # Add sets to the current {sum_val} value:
                if val_i == val_j and samples[i]>1:
                    n_sum += int(samples[i]/2)
                elif val_i != val_j:
                    j = values.index(val_j) # Identify index
                    n_sum += min([samples[i],samples[j]])
            # Update N if neccesary:
            N = max([N,n_sum])
    return (all_blocks, N)

def make_gauss_series(n):
    """
    Build a 'Gauss' series of bottles (represented by their
    capacity in litres), from 1 litre to a chosen value, and calculate
    the optimal number of sets according to the challenge rules.

    --- Inputs ---
    {n} [Integer]: Number of bottles within the series.

    --- Outputs ---
    {gauss} [List]: List with all bottles, each one represented by
    its capacity in litres.
    {N} [Integer]: Optimal number of sets, according to the challenge
    rules.
    """
    # Prepare Gauss series in the string representation:
    gauss = [] # Initiate
    for i in range(1,n+1):
        gauss.append(i)

    # Determine optimal number of sets (solution):
    N = -(-n//2) # Half if n is even, rounded up if n is odd

    return (gauss,N)

def make_fibonacci_series(n):
    """
    Build a 'Fibonacci' series of bottles (represented by their
    capacity in litres), and calculate the optimal number of sets
    according to the challenge rules.

    --- Inputs ---
    {n} [Integer]: Number of elements within the series.

    --- Outputs ---
    {fibo} [List]: List with all bottles, each one represented by
    its capacity in litres.
    {2}: Optimal number of sets (always equal to 2), according to the
    challenge rules.
    """
    # Prepare Fibonacci series as a list of integers:
    fibo = [1] # Initiate
    if n > 1:
        fibo.append(1)
    for i in range(2,n+1):
        fibo.append(fibo[-1]+fibo[-2])

    return (fibo,2)

# Cases (list of tuples, including string representation and solution):
cases = [
# Simple:
make_blocks([9],[1]), 
make_blocks([40,50,80],[4,2,1]),
# Complex blocks:
make_blocks([4,8,12,16,20],[2,3,2,3,2]),
make_blocks([1,5,6,12,15,30],[3,2,6,8,5,10]),
make_blocks([4,5,8,12,16,20,22],[10,20,11,12,11,10,6]),
make_blocks([3,9,12,20,25,30,44,45,47,66],[8,3,2,4,4,7,11,1,5,4]),
# Gauss series:
make_gauss_series(23),
make_gauss_series(38),
make_gauss_series(88),
# Fibonacci series:
make_fibonacci_series(7),
make_fibonacci_series(10),
]

def test_result(cases):
    # Evaluate all cases:
    N = 0 # Initiate success counts
    for case in cases:
        output = optim_sets(case[0])
        if output == case[1]:
            N += 1

    # Calculate success rate:
    success_rate = N/len(cases)*100
    print(f'Test results: {success_rate:.2f}% of the test cases were successful.')

test_result(cases)