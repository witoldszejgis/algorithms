""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
#Checking if given tree is proper BST
def isValidBST(node, MIN, MAX):
    if(node == None):
        return True;
    if(node.data > MIN and node.data < MAX and \
       isValidBST(node.left, MIN, node.data) and \
       isValidBST(node.right, node.data, MAX)):
          return True;
    else:
         return False;

def check_binary_search_tree_(root):
    return isValidBST(root,-100000,100000)
