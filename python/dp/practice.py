import math
line = input().split(' ')
n = int(line[0])
x = int(line[1])

coins = list(map(lambda x: int(x), input().split(' ')))

memo = [math.inf for _ in range(x+1)]

for c in coins: 
	memo[c] = 1

for i in range(0, x+1):
	for c in coins: 
		if i - c >= 0: 
			memo[i] = min(memo[i], 1+memo[i-c])


print(memo[x])

