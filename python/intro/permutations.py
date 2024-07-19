n = int(input())

# 1 -> [1]
# 2 -> impossible
# 3 -> impossible
# 4 -> [2, 4, 1, 3]
# 5 -> [2, 4, 1, 3, 5]
# 6 -> [2, 4, 6, 1, 3, 5]
if n == 2 or n == 3:
    print("NO SOLUTION")
elif n == 1:
    print("1")
else:
    # do evens first
    for i in range(2, n+1, 2):
        print(i, end=' ')

    # do evens
    for i in range(1, n+1, 2):
        print(i, end=' ')




