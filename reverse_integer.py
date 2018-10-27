#The time complexity is O(n) to reverse a given integer

def reverse(x):
	result = 0
	x_remaining = abs(x) 
	while x_remaining:
		result = result * 10 + x_remaining % 10
		x_remaining //= 10 
	return -result if x < 0 else result