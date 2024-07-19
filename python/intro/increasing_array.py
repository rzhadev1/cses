n = int(input())
line = [int(num) for num in input().split(' ')]

moves = 0 
for i in range(1, len(line)): 
    num = line[i]
    prev_num = line[i-1]
    if(num < prev_num):
        moves += prev_num - num
        line[i] += prev_num - num


print(moves)

