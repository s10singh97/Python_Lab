class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def BST(self, val):
    if self == None:
        self = val
    else:
        if self.value < val.value:
            if self.right == None:
                self.right = val
            else:
                BST(self.right, val)
        else:
            if self.left == None:
                self.left = val
            else:
                BST(self.left, val)
                
def show(self):
    print("\nInorder traversal is :\n")
    if self:
        show(self.left)
        print(self.value)
        show(self.right)


a = int(input("Enter number of values you want to insert: "))
print("Enter " + str(a) + " different values: ")                 
for i in range(0, a):
    n = int(input())
    if i == 0:
        b = Node(n)
    else:
        BST(b, Node(n))
    
show(b)    
