n = int(input())

dp = [0 for _ in range(n+1)]
dp[0] = 0

# single digits take only 1 step

if n >= 9:
	for i in range(1, 10): 
		dp[i] = 1

	for i in range(10, n+1): 
		stri = str(i)
		
		dp[i] = float("inf")
		for digit in stri: 

			# number of moves needed at i is the same as 
			# number of moves need at i - digit (for all digits) + 1 
			# + 1 comes from using one move to subtract this current digit 
			dp[i] = min(dp[i], dp[i - int(digit)] + 1)


	print(dp[n])
else:
	print(1)

