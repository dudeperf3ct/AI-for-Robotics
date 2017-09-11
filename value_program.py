# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']
visit = []
def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    values = [[99 for _ in range(len(grid[0]))] for __ in range(len(grid))]
    closed = [[0 for _ in range(len(grid[0]))] for __ in range(len(grid))]
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    x = goal[0]
    y = goal[1]
    #print (x, y)
    closed[x][y] = 1
    values[x][y] = 0
    visit.append([x, y])
    while (visit):
	    #for _ in range(4):    
        x = visit[0][0]
        y = visit[0][1]
        for i in range(len(delta)):
            x2 = x - delta[i][0]
            y2 = y - delta[i][1]
            if(x2>=0 and y2>=0 and x2 < len(grid) and y2 < len(grid[0]) and grid[x2][y2]!=1 and closed[x2][y2]==0):
                #print ("open", x2, y2)
                visit.append([x2, y2])
                values[x2][y2] = values[x][y] + cost
                closed[x2][y2] = 1    
            elif(x2>=0 and y2>=0 and x2 < len(grid) and y2 < len(grid[0]) and closed[x2][y2]==0):
                #print ("closed", x2, y2)
                closed[x2][y2] = 1
            #print (values)    
        #print (visit)    
        visit.pop(0)    
        #print (visit)
	    #break    
    return values 

def isfull(closed):
    count = 0
    ele = len(closed) * len(closed[0])
    for i in range(len(closed[0])):
        for j in range(len(closed)):
            if(bool(closed[i][j])):
                print (i, j , count)
                count+=1
            elif(count == ele):
                return False
            else:
                return True
                
k = compute_value(grid, goal, cost)
print (k)
