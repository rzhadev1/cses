n = int(input())
line = [int(num) for num in input().split(' ')]

def solve(n, apples, sum1, sum2): 
    if n == len(apples):
        return abs(sum2 - sum1)
    else:
        return min(solve(n+1, apples, sum1+apples[n], sum2), 
                   solve(n+1, apples, sum1, sum2+apples[n]))

print(solve(0, line, 0, 0))



