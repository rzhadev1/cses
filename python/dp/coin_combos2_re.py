line = input().split(' ')
n = int(line[0])
x = int(line[1])

coins = sorted(list(map(lambda x: int(x), input().split(' '))))

memo = [[0 for _ in range(n)] for k in range(x+1)]

for i in range(n):
	memo[0][i] = 1

# think about the transition from a given state 
# suppose you want to make a sum s
# we need to keep track of the last coin used, because other wise 
# we would double count states 
# (s,k) -> can either continue with k, in which case use 
# (s,k) -> (s-c[k], k)
# or (s,k) -> (s,k-1)
# where we use the next smaller coin
# are the only transitions 
for i in range(1, x+1): 
	total = 0 
	for k in range(n):
		if i - coins[k] >= 0: 
			total += memo[i - coins[k]][k]
		memo[i][k] = total % (int (1e9 + 7))

print(memo)
print(memo[x][n-1])

