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

	# PART 1: Make a first guess with single-bottle sets.

	# 1. Identify sub-groups with equal values:
	vals = list(set(stock)) # Unique values
	groups = {val: stock.count(val) for val in vals} # key=capacity, value=counts

	# 2. Choose the highest counts as the first guess:
	best_N = max(groups.values())

	# PART 2: Explore two-bottle sets and improve {best_N} if possible.

	# 3. Check the values of all sums and save them:
	# (Note: the self-sum i+i is included, even if there is only one sample of that value)
	sum_vals = [] # Initiate
	for i in range(len(vals)):
		for j in range(i,len(vals)):
			sum_vals.append(vals[i]+vals[j]) # Add the sum value
	sum_vals = list(set(sum_vals)) # Erase repetitions

	# 4. Count the sets with {sum_vals} values and update {N_best} if possible:
	for sum_val in sum_vals:
		check_vals = [] # Auxiliar list to avoid repeated counts
		# Initiate counts with the summing value itself
		n_sum = groups[sum_val] if sum_val in groups else 0
		# Sum the contribution of each pair of correct values:
		for val_i in groups:
			# Check if there is a pair with this sum value:
			val_j = sum_val-val_i # Proposed matching value
			if val_i not in check_vals:
				check_vals += [val_i,val_j] # Update check list
				# Add sets to the current {sum_val} value:
				if val_i == val_j and groups[val_i]>1:
					n_sum += int(groups[val_i]/2)
				elif val_i != val_j and val_j in groups:
					n_sum += min([groups[val_i],groups[val_j]])
		# Update N_best if neccesary:
		best_N = max([best_N,n_sum])

	return best_N

# # Evaluate challenge (DON'T MODIFY):
import os
if __name__ == "__main__":
	os.system('python test_cases.py')