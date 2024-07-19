n = int(input())
# 4 -> 15
# [4,3,2,1] [] []
# [4,3,2] [1] [] 1 2 
# [4,3] [1] [2] 1 3
# [4,3] [] [2,1] 2 3
# [4] [3] [2,1] 1 2
# [4,1] [3] [2] 3 1 
# [4,1] [3,2] [] 3 2 
# [4] [3,2,1] []  1 2

# [] [3,2,1] [4] 1 3 

# [] [3,2] [4,1] 2 3 
# [2] [3] [4,1] 2 1 
# [2,1] [3] [4] 3 1 
# [2,1] [] [4,3] 2 3
# [2] [1] [4,3] 1 2 
# [] [1] [4,3,2] 1 3 
# [] [] [4,3,2,1] 2 3

# 3 -> 7
# [3,2,1] [] [] 
# [3,2] [] [1] 1 3
# [3]  [2] [1] 1 2 
# [3] [2,1] [] 3 2 

# [] [2,1] [3] 1 3

# [1] [2] [3]  2 1 
# [1] [] [3,2] 2 3
# [] [] [3,2,1] 1 3

# 2 -> 3
# [2,1] [] []  
# [2] [1] [] 1 2 

# [] [1] [2] 1 3 

# [] [] [2,1] 2 3

# 1 -> 2
# [1] [] [] 
# [] [] [1] 1 3

# always consists of getting n-1 stack onto the middle, then moving largest` piece onto the right
# then moving n-1 stack onto the right
# basically use dp
# solve the n-1 subproblem recursively
discs = [[i for i in range(n, 0, -1)], [], []]

# calc moves to move disc n from a pile to another pile
# free pile is the pile which we can safely put discs on
def solve1(n, from_pile, to_pile, free_pile, moves):
    if n == 1:
        moves.append(f'{from_pile} {to_pile}')
        return moves
    # if n == 2, we need to use the free pile
    elif n == 2:
        moves.append(f'{from_pile} {free_pile}')
        moves.append(f'{from_pile} {to_pile}')
        moves.append(f'{free_pile} {to_pile}')
        return moves
    else:
        # move n-1 pile onto middle stack
        moves = solve1(n-1, from_pile, free_pile, to_pile, moves)
        # move last piece onto right pile
        moves.append(f'{from_pile} {to_pile}')
        # move n-1 pile onto right stack
        return solve1(n-1, free_pile, to_pile, from_pile, moves)

sol = solve1(n, 1, 3, 2, [])
print(len(sol))
for x in sol:
    print(x)
