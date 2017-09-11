# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 1, 0],
        [1, 1, 1, 0, 0, 0]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 0] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
# values =    [
#             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
#             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
#             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
#             ]
print (len(closed), len(closed[0]))
mat = []
count = 0
for i in range(len(grid)):
    mat.append([])
    for j in range(len(grid[0])):        
        print i, j
        mat[i].append(count)
        count += 1
print (len(mat), len(mat[0]), mat[0][5])
values = []
for i in range(len(grid)):
    for j in range(len(grid[0])):        
        values.append([[999, 999, 999]])
closed = []
for i in range(len(grid)):
    for j in range(len(grid[0])):        
        closed.append([[0, 0, 0]])
def optimum_policy2D(grid,init,goal,cost):
    total_cost = 0
    x = init[0]
    y = init[1]
    act = init[2]
    if(act == -1):
        total_cost += cost[0] 
    elif(act == 0):
        total_cost += cost[1] 
    elif(act == 1):
        total_cost += cost[2] 
    num = getnum(x, y)
    values[num][0][0] = x
    values[num][0][1] = y
    values[num][0][2] = act
    closed[num][0][1] = 1
    print (values)
    print (closed)
    p = []
    p = [x, y]
    while(p != goal):
    #for _ in range(13):
        new_cost = [999, 999, 999]
        direction = [99, 99, 99, 99]
        flag = 0
        for i in range(len(forward)):
            x2 = x + forward[i][0]
            y2 = y + forward[i][1]
            print x, y, forward_name[i], forward, i
            if (x2 >=0 and y2 >=0 and x2 < len(grid) and y2 < len(grid[0]) and grid[x2][y2] != 1):
                num = getnum(x2, y2)
                num1 = getnum(x, y)
                print (x, y, closed[num1][0][0], closed[num1][0][1], closed[num1][0][2])
                print (x2, y2, forward_name[i], closed[num][0][0], closed[num][0][1], closed[num][0][2])
                if(forward_name[i] == 'up'):
                    new_cost[1] = cost[1]
                    # act = action[1]
                    print (cost[1])
                    direction[0] = 0
                    flag=1
                elif(forward_name[i] == 'down' and closed[num][0][1] == 0):
                    new_cost[1] = cost[1]
                    # act = action[1]
                    closed[num][0][1] = 1
                    print (cost[1])
                    direction[2] = 2
                    flag=1 
                elif(forward_name[i] == 'left' and closed[num][0][2] == 0):
                    new_cost[2] = cost[2]
                    # act = action[2]
                    print (cost[2])
                    direction[1] = 1
                    flag=1
                    # temp = forward.pop(0)
                    # forward.insert(3, temp)
                elif(forward_name[i] == 'right' and closed[num][0][0] == 0):
                    new_cost[0] = cost[0]
                    # act = action[0]
                    print (cost[0])
                    direction[3] = 3
                    flag=1
                    # temp = forward.pop()
                    # forward.insert(0, temp)
        if(flag != 0):
            min = getmin(new_cost)
            act = action[min]
            print (min, direction, new_cost)
            if min == 1:
                if(direction[0] != 99):
                    if (x + forward[direction[0]][0] >=0 and y + forward[direction[0]][1] >=0 and x + forward[direction[0]][0] < len(grid) and y + forward[direction[0]][1] < len(grid[0])):    
                        x2 = x + forward[direction[0]][0]
                        y2 = y + forward[direction[0]][1]                
                        closed[num][0][1] = 1
                else:
                    if (x + forward[direction[2]][0] >=0 and y + forward[direction[2]][1] >=0 and x + forward[direction[2]][0] < len(grid) and y + forward[direction[2]][1] < len(grid[0])):
                        x2 = x + forward[direction[2]][0]
                        y2 = y + forward[direction[2]][1]                
                        closed[num][0][1] = 1
            if (min==2):
                    x2 = x + forward[direction[1]][0]
                    y2 = y + forward[direction[1]][1]                 
                    closed[num][0][2] = 1
                    temp = forward.pop(0)
                    forward.insert(3, temp)
            elif(min==0):    
                    x2 = x + forward[direction[3]][0]
                    y2 = y + forward[direction[3]][1]                 
                    closed[num][0][0] = 1
                    temp = forward.pop()
                    forward.insert(0, temp)                                
            print (x, y, total_cost, new_cost, min)
            total_cost += new_cost[min]
            print ("Num", num)

            values[num1][0][0] = x
            values[num1][0][1] = y
            values[num1][0][2] = act
            closed[num1][0][min] = 1
            x = x2
            y = y2
            print (values)           
            p = [x, y]
            print (x, y, closed[num1][0][0], closed[num1][0][1], closed[num1][0][2], p, goal)
            print (closed)
                    #break

    return values

def getnum(x, y):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i == x and j ==y):
                return mat[i][j]
def getmin(new_cost):
    m = 0
    min = new_cost[0]
    for o in range(len(new_cost)):
        if (min>new_cost[o]):
            min = new_cost[o]
            m = o
    return m        


k = optimum_policy2D(grid, init, goal, cost)
print (k)
final = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        num = getnum(i, j)
        if (k[num][0][2] == 0):
            final[i][j] = '#'
        elif (k[num][0][2] == 1):
            final[i][j] = 'L'
        if (k[num][0][2] == -1):
            final[i][j] = 'R'
for i in range(len(grid)):
    print (final[i])                    