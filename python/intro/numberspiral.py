t = int(input())
# 0,0 -> 1 x
# 0,1 -> 2 x -> 1 + 1 + 1
# 1,1 -> 3 
# 1,0 -> 4
# 2,0 -> 5 x -> 2 + 2 + 1
# 2,1 -> 6 
# 2,2 -> 7
# 1,2 -> 8
# 0,2 -> 9
# 0,3 -> 10 x -> 3 + 3 + 1

# find area of the square before, then calculate value based 
# on the boundary

lines = []
for _ in range(t):
    line = [int(num)-1 for num in input().split(' ')]
    lines.append(line)

for q_x, q_y in lines: 
    # find which layer the point is in
    # alternates between x and y coordinate
    layer = max(q_x, q_y)
    prev_area = (layer) * (layer)
    
    # starts on x 
    layer_start_pt = ()
    if layer % 2 == 0: 
        layer_start_pt = (layer, 0)
    # starts on y
    else:
        layer_start_pt = (0, layer)

    dist = abs(layer_start_pt[0] - q_x) + abs(layer_start_pt[1] - q_y)
    print(prev_area + dist + 1)




