import math
line = input().split(' ')
n = int(line[0])
x = int(line[1])

coins = list(map(lambda x: int(x), input().split(' ')))
memo = [math.inf for _ in range(x+1)]

for c in coins: 
	if c <= x:
		memo[c] = 1

memo[0] = 0
for i in range(x+1):
	for c in coins: 
		if i - c >= 0: 
			memo[i] = min(1+memo[i-c], memo[i])

if memo[x] == math.inf:
	print('-1')
else:
	print(memo[x])
