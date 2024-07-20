from collections import defaultdict
string = input()
counts = defaultdict(int)

for char in string:
    counts[char] += 1

def solve(n, counts, strings): 
    if n == 0:
        return strings
    else:
        ret = []
        for char in counts.keys():
            if counts[char] > 0: 
                newstrings = [char + string for string in strings]
                counts[char] -= 1
                x = solve(n-1, counts, newstrings)
                counts[char] += 1
                ret = ret + x
        return ret

sol = solve(len(string), counts, [''])
print(len(sol))
for x in sorted(sol):
    print(x)
