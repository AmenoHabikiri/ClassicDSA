#ratinmaze
import numpy as np
def genA(n):
    A=[[ np.random.randint(2) for i in range(n)] for j in range(n)]
    print(np.array(A))
    return A
def genB(n):
    B=[[ -1 for i in range(n)] for j in range(n)]
    return B

def isValid(n, maze, x, y, res):
    if x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1 and res[x][y] == 0:
        return True
    return False
 
# A recursive utility function to solve Maze problem
 
 
def RatMaze(n, maze, x, y, res):
    if x == n-1 and y == n-1:
        return True
    for x_move,y_move in zip([-1, 1, 0, 0],[0, 0, -1, 1]):
        x_new=x+x_move
        y_new=y+y_move
        if isValid(n, maze, x_new, y_new, res):
 
            # mark x, y as part of solution path
            res[x_new][y_new] = 1
            if RatMaze(n, maze,  x_new, y_new, res):
                return True
            res[x_new][y_new] = 0
    return False
 
 
def solveMaze(n,maze):
    # Creating a 4 * 4 2-D list
    res = [[0 for i in range(n)] for i in range(n)]
    res[0][0] = 1
 
 
    if RatMaze(n, maze, 0, 0, res):
        for i in range(n):
            for j in range(n):
                print(res[i][j], end=' ')
            print()
    else:
        print('Solution does  not exist')
 
 
# Driver program to test above function
if __name__ == "__main__":
    # Initialising the maze
    maze = [[1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1]]
 
    solveMaze(maze)
