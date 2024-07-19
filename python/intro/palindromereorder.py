from collections import defaultdict, deque
query = input()

# can probably do this recursively instead!
counts = defaultdict(int)
for letter in query:
    counts[letter] += 1

# can have at most one letter with odd count
num_odd = 0
odd_letter = ''
for letter in counts.keys():
    if counts[letter] % 2 != 0:
        num_odd += 1
        odd_letter = letter

#print(counts)
#print(num_odd)
#print(odd_letter)
sol = deque()
if num_odd > 1:
    print("NO SOLUTION")

# place the odd letter in the middle
elif num_odd == 1:
    sol.append(odd_letter)
    counts[odd_letter] -= 1
    #print(counts)

    for letter in counts.keys():
        while(counts[letter] > 0):
            sol.appendleft(letter)
            sol.append(letter)
            counts[letter] -= 2

    print(''.join(sol))

else: 
    for letter in counts.keys():
        while(counts[letter] > 0):
            sol.appendleft(letter)
            sol.append(letter)
            counts[letter] -= 2

    print(''.join(sol))

    
