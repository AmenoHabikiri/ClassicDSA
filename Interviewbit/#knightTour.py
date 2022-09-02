#knightTour
import numpy as np
def knightTour(n):
    board=[[-1 for i in range(n)] for j in range(n)]
    knightTourHelper(n=n,board=board,x=2,y=0,count=0)
    print(np.array(board))
def knightTourHelper(n,board,x,y,count):
    if count==n*n:
        return True
    if (x<0) or (x>=n) or (y<0) or (y>=n) or board[y][x]!=-1:
        return False
    board[y][x]=count
    for x_move,y_move in zip([-2,-2,-1,-1,1,1,2,2],[-1,1,-2,2,-2,2,-1,1]):
        if knightTourHelper(n,board,x+x_move,y+y_move,count+1):
            return True
    board[y][x]=-1
    return False
knightTour(6)