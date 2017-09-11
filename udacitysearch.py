# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

checked = []
p = []

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1
    initi = [cost, init[0], init[1]]
    opened = []
    opened.append(initi)
    p = []
    p = [opened[0][1], opened[0][2]]
    while(p != goal):
        m = minimum(opened)
        #print (m, opened[m])
        for i in range(len(delta)):
            
            j = delta[i][0] + opened[m][1]
            k = delta[i][1] + opened[m][2]
            #print (j, k)
            if (j>=0 and k>=0 and j<=len(grid)-1 and k<=len(grid[0])-1 and grid[j][k]==0):
                new = [j, k]
                new1 = [opened[m][0] + 1, j, k]
                if new not in checked and new1 not in opened:
                    opened.append([opened[m][0]+cost, j, k])
        # cost = cost + 1
        checked.append([opened[m][1], opened[m][2]])
        l = opened.pop(m)
        #print (opened, l)
        if len(opened)==0:
        	print 'fail'
        	return ' '
        p = [opened[0][1], opened[0][2]]
        path = opened[0]
        #print ("Path", p, goal)
    return path

def minimum(opened):
    mi = opened[0][0]
    m = 0
    for i in range(len(opened)):
        if mi>opened[i][0]:
            m = i
    return m        
grid = [[0, 1],
        [0, 0]]    
j = search(grid, init, goal, cost)
print (j)