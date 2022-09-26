class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
def insert(root,data):
    if root is None:
        return Node(data)
    else:
        if root.data<data:
            root.right=insert(root.right,data)
        else:
            root.left=insert(root.left,data)  
    return root
def inorder(root):
    if root:        
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def levelorderUsingDictionary(root,level,dic=None):
    if root is None:
        if level not in dic:
            dic[level]=[-1]
        else:
            dic[level].append(-1)
        return
    else:
        levelorderUsingDictionary(root.left,level+1,dic)
        if level not in dic:
            dic[level]=[root.data]
        else:
            dic[level].append(root.data)
        levelorderUsingDictionary(root.right,level+1,dic)
def pathSum(A,sum):
    if A is None:
        if sum==0:
            return True
        else:
            return False
    else:
        return (pathSum(A.left,sum-A.data) or pathSum(A.right,sum-A.data))
     
r=Node(10)
r=insert(r,6)
r=insert(r,3)
r=insert(r,7)
r=insert(r,11)
r=insert(r,13)
r=insert(r,19)
dic={}
print(pathSum(r,10))