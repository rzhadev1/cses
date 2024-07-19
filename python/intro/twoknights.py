n = int(input())

# find x = num of ways that two knights can attack each other, then 
# compute (k choose 2) - x + overlap
# x: for k > 3, this is the number of 3x3 boards contained in kxk board * 8, (8 ways to attack on 3x3) 
# notice that for k=4, we have 8 positions of overlap between two consecutive boards

overlap = 0 # overlap follows 1,3,6,10,15,21,...
inc = 1 # increases by 1 each iter past k=3
for k in range(1, n+1):
    if k == 1:
        print(0)
    # 4 choose 2 = 6
    elif k == 2:
        print(6)
    else:
        # k choose 2 
        num_placements = k**2 * (k**2 - 1) // 2
        attacking = (k - 2) * (k - 2) * 8
        overlap_p = overlap * 8 

        # print(f'k:{k}, np: {num_placements}, att:{attacking}, op{overlap_p}')
        print(num_placements - attacking + overlap_p)
        overlap += inc
        inc += 1




