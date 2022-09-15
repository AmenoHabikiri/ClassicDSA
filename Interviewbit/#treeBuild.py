#treeBuild                                          #1
import queue


class tree():                                 #3           #2
    def __init__(self,data):              #7      #5   #9
        self.data=data
        self.left=None
        self.right=None
def DFSIOT(node,li):
    if node:
        DFSIOT(node.left,li)
        li.append(node.data)
        DFSIOT(node.right,li)
def DFSPOT(node,li):
    if node:
        DFSPOT(node.left,li)
        DFSPOT(node.right)
        li.append(node.data,li)
def DFSPrOT(node,li):
    if node:
        li.append(node.data,li)
        DFSPrOT(node.left,li)
        DFSPrOT(node.right,li)
def BFS(node,li):
    if node is None:
        return 
    queue=[]
    queue.append(node.data)
    while len(queue)>0:
        li.append(queue)
        node=queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
            
        
        
        
node=tree(1)
node.left=tree(3)
node.right=tree(2)
node.left.left=tree(7)
node.left.right=tree(5)
node.right.right=tree(9)
li=[]
BFS(node,li)
print(li)

        
        