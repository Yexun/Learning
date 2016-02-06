def is_palindrome(n):
	i=len(str(n))
	if n%10==int(n/pow(10,i-1)) and i>1:
		return n
output = filter(is_palindrome, range(1, 1000))
print(list(output))
