line = input().split(' ')
n = int(line[0])
x = int(line[1])

coins = sorted(list(map(lambda x: int(x), input().split(' '))))

memo = [0 for _ in range(x+1)]
memo[0] = 1

for k in range(0, n):
	for i in range(1, x+1): 
		if i - coins[k] >= 0: 
			memo[i] += memo[i - coins[k]]
			memo[i] = memo[i] % (int (1e9 + 7))


print(memo[x])

