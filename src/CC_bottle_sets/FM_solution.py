# Solution by Fernando Meneses (@github Fertmeneses)

def optim_sets(stock):
	"""
	Find the maximum number of sets that can be made from the input list
	{stock}, which represents a collection of bottles. All sets must be
	made of one or two bottles, and all sets must share the same
	total volume.

	--- Inputs ---
	{stock} [List]: Each element represents the volume of a single
	bottle, in litres.
	
	--- Outputs ---
	{best_N} [Integer]: Maximum number of sets that can be made.
	"""

	# Implement your code here:

	# PART 1: Make a simple initial guess with...
	# ...sets of single bottles.

	# 1. Identify sub-groups with equal values:
	from collections import Counter
	groups = dict(Counter(stock)) # Generate dictionary with counts for each value

	# 2. Choose the highest count number as the first guess for {best_N}:
	best_N = max(groups.values())

	# PART 2: Explore sets with combined bottles and...
	#... improve {best_N} if possible.

	# 3.
	# best_N = 0

	return best_N

#print(optim_sets([9]))
# # Evaluate challenge (DON'T MODIFY):
import os
if __name__ == "__main__":
	os.system('python test_cases.py')