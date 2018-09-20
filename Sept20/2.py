class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
 
def BST(self,node):
    if self is None:
        self = node
    else:
        if self.value < node.value:
            if self.right is None:
                self.right = node
            else:
                BST(self.right, node)
        else:
            if self.left is None:
                self.left = node
            else:
                BST(self.left, node)
 
def show(self):
    if self:
        show(self.left)
        print(self.value)
        show(self.right)
 
r = Node(50)
BST(r,Node(30))
BST(r,Node(20))
BST(r,Node(40))
BST(r,Node(70))
BST(r,Node(60))
BST(r,Node(80))
 
show(r)
 