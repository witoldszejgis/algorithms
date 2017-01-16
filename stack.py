class Node:
    def __init__(self,value,next):
        self.data=value
        self.next=next
class MyStack(object):
    def __init__(self):
        self.top=None
    def is_empty(self):
        if self.top is None:
            return True
    def pop(self):
        if not self.is_empty():
            data=self.top.data
            self.top=self.top.next
            return data

    def push(self,value):
        nodePush=Node(value,self.top)
        self.top=nodePush


        

def is_matched(expression):
    stack = MyStack()
    matched=True
    for i in range(0,len(expression)):
        if(expression[i]=="(" or expression[i]=="[" or expression[i]=="{"):
            stack.push(expression[i])
        if(expression[i]==")" or expression[i]=="]" or expression[i]=="}"):

            first=stack.pop()
                
            second=expression[i]

            if(first is None):
                matched=False
            elif(first=="(" and second!=")"):
                matched=False
            elif(first=="[" and second!="]"):
                matched=False
            elif(first=="{" and second!="}"):
                matched=False
        
    if(stack.top is not None):
        matched=False
    return matched


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
