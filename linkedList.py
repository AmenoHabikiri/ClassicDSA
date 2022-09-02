class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class SLinkedList:
    def __init__(self):
        self.head=None
    def insertEnd(self,k):
        NewNode=Node(k)
        temp=self.head
        if self.head is None:
            self.head=NewNode
            return
        while (temp.next):
            temp=temp.next
        temp.next=NewNode
    def deleteNode(self,k):
        temp=self.head
        if temp.data == k:
            self.head=temp.next
            temp=None
            return
        while (temp.next) :
            if (temp.next.data == k):
                break
            temp=temp.next
        if (temp.next is None):
            print("Node not found")
        else:
            if (temp.next.next is not None):
                temp.next=temp.next.next
            else:
                temp.next=None
    def insertInBetween(self,node1,k):
        NewNode=Node(k)
        temp=self.head
        while (temp.next):
            if temp.data != node1:
                temp=temp.next
            else:
                break
        NewNode.next=temp.next
        temp.next=NewNode               
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def lastNode(self):
        temp=self.head
        if temp is None:
            return temp
        else:
            while (temp.next):
                temp=temp.next
            return temp.data
    def reverseList(self):
        last=self.head
        i=0
        if last is None:
            return 
        else:
            while (last.next is not None):
                last=last.next
                i+=1
        last.next=Node(self.head.data)
        self.head=self.head.next
        for i in range(i-1):
            temp=Node(self.head.data)
            self.head=self.head.next
            temp.next=last.next
            last.next=temp
            temp=None
list1=SLinkedList()
for i in range(0,10):
    list1.insertEnd(i)
list1.printList()
print("***")
list1.reverseList()
list1.printList()

        