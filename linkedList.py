"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    nodes=[]
    hasCycle=False
    current=head
    while current.next is not None and hasCycle!=True:
        nodes.append(current)
        current=current.next
        if current in nodes:
            hasCycle=True
    return hasCycle
    

