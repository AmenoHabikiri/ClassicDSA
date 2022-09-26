#augmentedBSTtofindmajorityelement
class BSTnode:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        self.count=1
class BinarySearchTree:
    def __init__(self) -> None:
        self.root=None
        self.size=0
    def find_and_parent(self,data):
        q=None
        p=self.root
        while p is not None and p.data!=data:
            q=p
            if data<p.data:
                p=p.left
            else:
                p=p.right
        return p,q
    def insert(self,data):
        self.size+=1
        if self.root==None:
            self.root=BSTnode(data)
            return
        p,q=self.find_and_parent(data)
        if p is not None:
            p.count=p.count+1
            return
        else:
            if data<q.data:
                q.left=BSTnode(data)
            else:
                q.right=BSTnode(data)
    def majority_element(self,root):
        if root:
            self.majority_element(root.left)
            if root.count>=(self.size//2):
                return root.count
            self.majority_element(root.right)
            
            
            
            
        
            