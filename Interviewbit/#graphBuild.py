def myFunc(A):
    return len(A)
class Graph:
    def __init__(self,edge):
        self.edge=edge
        self.graph_dict={}
        for start,end in self.edge:
            if start not in self.graph_dict:
                self.graph_dict[start]=[end]
            else:
                self.graph_dict[start].append(end)
    def get_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_path=self.get_path(node,end,path)
                for p in new_path:
                    paths.append(p)
        return paths
    def get_shortest_path(self,start,end,path=[]):
        paths=self.get_path(start,end,path)
        paths.sort(key=myFunc)
        k=len(paths[0])
        print(paths)
        i=0
        while i<len(paths):
            if len(paths[i])>k:
                paths.pop(i)
                l=l-1
                i=i-1
            i=i+1
        return paths
li=[("M","A"),("M","B"),("A","C"),("A","B"),("C","D"),("B","C"),("M","D"),("A","D")]
routes=Graph(li)
print(routes.graph_dict)
print(routes.get_path("M","D",))
print(routes.get_shortest_path("M","D"))