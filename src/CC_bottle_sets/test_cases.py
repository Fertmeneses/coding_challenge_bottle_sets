from challenge import optim_sets

def make_block(values,numbers):
    """
    Build a 'block' of bottle values (represented by their capacity
    in litres), by joining sub-blocks of repeated values, and calculate
    the optimal number of sets according to the challenge rules.

    --- Inputs ---
    {values} [List]: Elements must be integers, representing the
    capacity of each sub-block of bottles.
    {numbers} [List]: Elements must be integers, representing the
    number of bottles with the associated capacity (correlative to
    the list {values}).

    --- Outputs ---
    {block} [String]: String representation of the 'block', in which
    all bottles are represented by their capacity, in litres, and
    spaced by a '.'.
    {N} [Integer]: Optimal number of sets, according to the challenge
    rules.
    """

    # Raise error if input lists have different size:
    if len(values)!=len(numbers):
        raise ValueError("The two input lists must have the same number of elements.")
    # Raise error if {values} list have duplicated values:
    seen = set()
    for x in values:
        if x in seen:
            raise ValueError("First list must not have duplicated values.")
        seen.add(x)

    # Build the string representation:
    block = '' # Initiate
    for i in range(len(values)):
        # Generate sub-block:
        sub_block = [str(values[i]) for _ in range(numbers[i])]
        # Update full block:
        block += '.'.join(sub_block)+'.'
    # Final block (erase the last '.'):
    block = block[:-1]

    # Calculate optimal number of sets (solution):
    N = max(numbers) # Initiate a priori solution
    for i in range(len(values)):
        for j in range(i+1,len(values)):
            sum_vals = values[i] + values[j] # Obtain the sum of any two values
            if sum_vals in values: # Check if the sum is within the input
                N = max(N,min([numbers[i],numbers[j]])
                    +numbers[values.index(sum_vals)]) # Update solution if needed

    return (block, N)

def make_gauss_series(n):
    """
    Build a 'Gauss' sequence of single bottle values (represented by their
    capacity in litres), from 1 litre to a chosen value, and calculate
    the optimal number of sets according to the challenge rules.

    --- Inputs ---
    {n} [Integer]: Maximum capacity, in litres, for the series.

    --- Outputs ---
    {gauss} [String]: String representation of the 'gauss' series,
    in which all bottles are represented by their capacity, in litres,
    and spaced by a '.'.
    {N} [Integer]: Optimal number of sets, according to the challenge
    rules.
    """
    # Prepare Gauss series in the string representation:
    gauss = '' # Initiate
    for i in range(1,n+1):
        gauss += str(i)+'.'
    gauss = gauss[:-1] # Erase the last '.'

    # Determine optimal number of sets (solution):
    N = int(n/2)

    return (gauss,N)

def make_fibonacci_series(n):
    """
    Build a 'Fibonacci' sequence of bottle values (represented by their
    capacity in litres), as a Fibonacci series with n elements, and
    calculate the optimal number of sets according to the challenge rules.

    --- Inputs ---
    {n} [Integer]: Number of elements for the sequence.

    --- Outputs ---
    {fibo} [String]: String representation of the 'fibonacci' series,
    in which all bottles are represented by their capacity, in litres,
    and spaced by a '.'.
    {2}: Optimal number of sets, always equal to 2, according to the
    challenge rules.
    """
    # Prepare Fibonacci series as a list of integers:
    fibo = [1] # Initiate
    if n > 1:
        fibo.append(1)
    for i in range(2,n+1):
        fibo.append(fibo[-1]+fibo[-2])
    # Convert to string representation:
    fibo = '.'.join([str(i) for i in fibo])

    return (fibo,2)

# Cases (list of tuples, including string representation and solution):
cases = [
# Simple:
make_block([9],[1]), 
make_block([40,50,80],[4,2,1]),
# Complex blocks:
make_block([1,5,6,12,15,30],[3,2,6,8,5,10]),
make_block([4,8,12,16,20],[10,11,12,11,10]),
make_block([3,9,12,20,25,30,44,45,47,66],[8,3,2,4,4,7,11,1,5,4]),
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
        decoded_list = [int(x) for x in case[0].split('.')]
        output = optim_sets(decoded_list)
        if output == case[1]:
            N += 1

    # Calculate success rate:
    success_rate = N/len(cases)*100
    print(f'Test results: {success_rate:.2f}% of the test cases were successful.')

test_result(cases)