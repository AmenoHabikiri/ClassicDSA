import numpy as np
def addTwoNumbers(A,B):
        temp1=A
        temp2=B
        i=0
        j=0
        while temp1 or temp2:
            if temp1:
                i=i+1
                temp1=temp1.next
            if temp2:
                j=j+1
                temp2=temp2.next
        print(i,j)
        if j>i:
            temp1=B
            temp2=A
        else:
            temp1=A
            temp2=B
        ans=temp1
        sum=0
        carry=0
        while (temp2):
            sum=(temp1.data+temp2.data+carry)
            carry=sum//10
            temp1.data=sum%10 
            temp2=temp2.next
            temp1=temp1.next
        while (carry>0):
            sum=temp1.data+carry
            carry=sum//10
            temp1.data=sum%10
            if temp1.next is None:
                break
            else:
                temp1=temp1.next  
        if carry==0:
            return ans
        else:
            x=Node(carry)
            temp1.next=x 
            return ans 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ListNode:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def append(self,k):
        if (self.head is None):
            self.head=Node(k)
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=Node(k)
    def kth_node_from_middle(self,k):
        if self.head is None:
            print(-1)
        else:
            temp=self.head
            n=1
            while (temp.next is not None):
                temp=temp.next
                n=n+1
        i=1
        temp=self.head
        mid=(n//2)+1
        print(mid)
        if (mid<=k):
            print(-1)
        while(i<((n//2)-k+1)):
           i=i+1
           temp=temp.next
        print(temp.data)      
    def SortBinary(self):
        temp=self.head
        one=0
        zero=0
        while(temp):
            if temp.data==1:
                one+=1
            else:
                zero+=1
            temp=temp.next
        temp=self.head
        while(temp):
            if zero>0:
                temp.data=0
                zero=zero-1
            else:
                temp.data=1 
            temp=temp.next       
    def swapListNodes(self):
        prev=self.head
        temp=self.head.next
        while(temp):
            c=prev.data
            prev.data=temp.data
            temp.data=c 
            if (temp.next):
                prev=temp.next
            else: 
                break
            if (prev.next):
                temp=prev.next
            else:
                break           
    def revLinkedList(self):
        curr=self.head
        prev=None
        while(curr):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
    def revK(self,A,k):
        if A == None:
            return None
        curr=A
        prev=None
        next=None
        i=0
        while(curr and i<k):  
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next 
            i+=1
        if next:
            A.next=self.revK(next,k)
        return prev
    def EvenReverse(self):
        li=[]
        temp=self.head
        i=1
        while(temp):
            if i%2==0:
                li.append(temp.data)
            i=i+1
            temp=temp.next
        li.reverse()            
        i=1
        temp=self.head
        while(temp):
            if i%2==0:
                temp.data=li[i//2-1]
            i=i+1
            temp=temp.next
    def leng(self):
        i=0
        temp=self.head
        while(temp):
            i=i+1
        return i
    def rotateK(self,k):
        i=0
        temp=self.head
        while(temp):
            i=i+1
            last=temp
            temp=temp.next    
        k=k%i
        i=i-k
        temp=self.head
        prev=None
        while(i>0):
            prev=temp
            temp=temp.next
            i=i-1
        prev.next=None
        last.next=self.head
        self.head=temp
    def insertionSort(self):
        prev=self.head
        if prev.next is None:
            return 1
        else:
            temp=prev.next
        i=1
        while(temp):
            i=i+1
            temp=temp.next
        temp=prev.next
        while(i>1):
            j=i-1
            prev=self.head
            temp=prev.next
            while(j>=1):
                if (prev.data>temp.data):
                    c=temp.data
                    temp.data=prev.data
                    prev.data=c   
                prev=temp
                temp=temp.next  
                j=j-1
            i=i-1       
    #def nLognSort(self):
    def palindrome(self):
        temp=self.head
        i=0
        while temp:
            temp=temp.next
            i=i+1
        if i%2==0:
            mid=i//2
        else:
            mid=i//2+1
        tempm=self.head
        temp=self.head
        while mid>0:
            mid=mid-1
            tempm=tempm.next
        i=i//2
        #now reverse the leftover linked list
        prev=None
        curr=tempm
        while(curr):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        tempm=prev
        while i>0 :
            if(temp.data!=tempm.data):
                return 0
            temp=temp.next
            tempm=tempm.next
            i=i-1 
        return 1    
    def RemoveDuplicates(self):
        prev=self.head
        curr=prev.next
        c=prev.data
        while c==curr.data:
            if curr.next:
                curr=curr.next
            else: break
            if curr.data!=c:
                self.head=curr
                prev=self.head
                if prev.next:
                    curr=prev.next
                c=prev.data
        if prev.data==curr.data:
            self.head=None
        next=curr.next
        while (curr.next):
            next=curr.next
            c=curr.data
            if c!=next.data:
                prev=curr
                curr=next
                next=curr.next
            else :
                while (c==next.data):
                    if next.next:
                        next=next.next
                    else: break
                curr=next
                prev.next=curr
        if next:
            if curr.data==next.data:
                prev.next=None                     
    def revList(self):
        curr=self.head
        prev=None
        while(curr):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
def revL(A,prev,curr):
    if curr is None:
        A.head=prev
        return 
    next=curr.next
    curr.next=prev
    revL(A,curr,next)
l1=ListNode()
l2=ListNode()
l2.append(1)
print("*****")
revL(l2,None,l2.head)
l2.display()
