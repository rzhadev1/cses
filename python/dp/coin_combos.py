line = input().split(' ')
n = int(line[0])
x = int(line[1])

coins = sorted(list(map(lambda x: int(x), input().split(' '))))

memo = [0 for _ in range(x+1)]
memo[0] = 1
# num of ways to make x is same as sum of number of ways to make 
# x-c_i for all c_i 

for i in range(1,x+1): 
	memo[i] = 0
	for c in coins: 
		if i-c >= 0:
			memo[i] += memo[i-c] 
		else: 
			break


print(memo[x] % (int(1e9 + 7)))

