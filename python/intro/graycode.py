n = int(input())

def solve(n, bitstr):
    # for all bitstr in the current list, prepend 0
    # then reverse the list and prepend 1
    if n == 0:
        return bitstr
    else:
        zero = []
        one = []
        for x in bitstr: 
            zero.append('0' + x)
        for x in bitstr[::-1]:
            one.append('1' + x)
        new = zero + one
        return solve(n-1, new)

for x in solve(n-1, ['0', '1']):
 print(x)

# 00 
# 01 
# 11
# 10

# 10
# 11
# 01
# 00
