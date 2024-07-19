n = int(input())
arr = list(map(lambda x: int(x), input().split(' ')))

# kadanes 
bestmax = -float("inf")
currmax = -float("inf")

for i in range(0, len(arr)):
	# the max subsequence either starts at num, or continues with adding 
	# on num 
	currmax = max(arr[i], currmax + arr[i])
	bestmax = max(bestmax, currmax)


print(bestmax)
