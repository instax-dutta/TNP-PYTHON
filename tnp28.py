class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class List:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=Node(data)
        if(self.head==None):
            self.head=newnode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
    def print(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
        
ob=List()
ob.insert(10)
ob.insert(20)
ob.print()
ob.insert(30)
ob.print()