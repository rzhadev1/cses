import math
line = input().split(' ')
n = int(line[0])
x = int(line[1])

coins = list(map(lambda x: int(x), input().split(' ')))

def solve(y, coins, memo): 
	if y < 0:
		return math.inf
	
	if y == 0:
		return 0

	if y in memo: 
		return memo[y]

	else: 
		total = math.inf
		for i in coins:
			ci = 1 + solve(y-i, coins, memo)
			total = min(ci, total)
		
		memo[y] = total
		return memo[y]

if solve(x, coins, {}) == math.inf: 
	print('-1')
else:
	print(solve(x, coins, {}))




	
