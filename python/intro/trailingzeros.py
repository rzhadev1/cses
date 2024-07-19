import math
n = int(input())

# probably cant calculate n!
# linear in n solution?

# pattern: 
'''
total = 1
for i in range(2, n+1):
    total *= i
    tstr = str(total)
    nz = 0
    for j in range(len(tstr)-1, 0, -1):
        if tstr[j] == '0':
            nz += 1
        else:
            break
    print(f'i:{i}, nz: {nz}')
'''
if n < 4: 
    print(0)
else:
    ctr = 1 
    total = 0
    while n >= 5**ctr: 
        total += n // (5**ctr)
        ctr += 1 
    print(total)






