#This program checks if the string is palindrome or not. It skips the nonalphanumeric character and only checks if the alphanumeric characters make up a palindrome. The rumtime is O(n). 
def is_palindrome(S):
	i = 0
	j = len(S) - 1
	while i < j:
		while not S[i].isalnum():
			i += 1
		while not S[j].isalnum():
			j -= 1
		if S[i].lower() == S[j].lower():
			i += 1
			j -= 1 
		else:
			return False
	return True