#Checks parity of an integer in O(k) runtime; k being the number of 1's in an integer
def parity(x):
	result = 0
	while x:
		result ^= 1
		x &= x - 1		#drops the lowest set bit of x
	return result 

