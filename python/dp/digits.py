n  = int(input())


# memo[i] gives the min steps to get from i to 0
def remove_digits(n, memo):
	# if we got zero, takes 0 steps
	if n == 0: 
		return 0

	# if we have a single digit, the next step gives 0 
	elif n // 10 == 0:
		return 1
	# if we already saw this number, use the solution there
	elif n in memo.keys():
		return memo[n]

	# if we have a number with >= 2 digits, 
	else: 
		temp = str(n)
		memo[n] = float("inf")
		for digit in temp: 
			num = n - int(digit)
			res = remove_digits(num, memo) + 1
			memo[n] = min(memo[n], res)
		
		return memo[n]

print(remove_digits(n, {}))
			
