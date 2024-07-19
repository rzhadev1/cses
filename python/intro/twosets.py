n = int(input())

# 7 -> sum is 28
# 7,_ -> remaining sum is 21 7
# 7,6 -> remaining sum is 15 6
# 7,11 -> remaining sum is 10 5
# 11,11 -> remaining sum is 6 4 
# 14,11 -> remaining sum is 3 3
# 14,13 -> remaining sum is 1 2 
# 14,14 -> remaining sum is 0 1

# 6 -> sum is 21
# 6,_ -> remaining sum is 15 6
# 6,5 -> remaining sum is 10 5 
# 6,9 -> remaining sum is 6 4 
# 9,9 -> remaining sum is 3 3 
# 11,9 -> remaining sum is 1 2 
# 11,10 -> remaining sum is 0 1

left = []
right = []

lsum = 0
rsum = 0 
rem_sum = n * (n+1) // 2 # gaus sum
for i in range(n, 0, -1):
    if lsum == rsum: 
        left.append(i)
        lsum += i
    elif lsum > rsum: 
        right.append(i)
        rsum += i
    else:
        left.append(i)
        lsum += i

if lsum == rsum:
    print("YES")
    print(len(left))
    for l in left:
        print(l, end=' ')
    print()
    print(len(right))
    for r in right:
        print(r, end=' ')
else:
    print("NO")
