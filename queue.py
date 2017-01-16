class Node:
    def __init__(self,value,next):
        self.data=value
        self.next=next
class MyQueue(object):
    def __init__(self):
        self.head=None
        self.tail=None
    
    def peek(self):
        if(self.isEmpty()!=True):
            return self.head.data
        
    def pop(self):

        data=self.head.data
        self.head=self.head.next
        if(self.head==None):
            self.tail=None
        return data
        
            
    def put(self, value):

        if(self.isEmpty()==True):
            newNode=Node(value,None)
            self.tail=newNode
            self.head=newNode
        else:
            newNode=Node(value,None)
            self.tail.next=newNode
            self.tail=newNode
    def isEmpty(self):
        if(self.head==None and self.tail==None):
            return True
        else:
            return False
queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
