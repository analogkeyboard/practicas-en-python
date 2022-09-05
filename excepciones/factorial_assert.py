def factorial(n):
	assert n>=0,"n debe ser mayor o igual a 0"
	fact=1

	for x in range(2,n+1):
		fact*=x
	return fact

print(factorial(10))
