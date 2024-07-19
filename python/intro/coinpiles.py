t = int(input())

# sum is multiple of 3?
# also need that a or b is not too "large", i.e 
# a <= 2*b and b <= 2*a
# otherwise, you run out of coins on the other side

lines = []
for _ in range(t): 
    line = [int(num) for num in input().split(' ')]
    lines.append(line)

for line in lines:
    a = line[0]
    b = line[1]
    
    if a > 2*b or b > 2*a:
        print("NO")
    elif (a+b) % 3 == 0:
        print("YES")
    else:
        print("NO")
