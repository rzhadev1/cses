n = int(input())

memo = [0 for _ in range(n+7)]
memo[0] = 1
memo[1] = 1
memo[2] = 2
memo[3] = 4
memo[4] = 8
memo[5] = 16
memo[6] = 32

if n >= 1 and n <= 6: 
	print(memo[n])

else: 
	for i in range(7,n+1): 
		memo[i] = (memo[i-1] + memo[i-2] + memo[i-3] + memo[i-4] + memo[i-5] + memo[i-6]) % (10**9 + 7)
	print(memo[n])
