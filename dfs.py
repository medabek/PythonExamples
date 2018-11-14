class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        
    def __str__(self):
        return str(self.value) + ", " +str(self.left)
    
    def getValue(self):
        return self.value


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()
        return
    def setLeftChild(self, node):
        self.left = node

    def getLeftChild():
        return self.left

    def setRightChild(self, node):
        self.right = node

    def getRightChild():
        return self.right

    def setParent(self, node):
        self.parent = node

    def getParent():
        return self.parent

def DFSBinary(root, key):
    stack = [root]
    while len(stack)>0:
        if stack[0].getValue()==key:
            return True
        else:
            temp = stack.pop(0)
            if temp.getRightChild():
                stack.insert(0,temp.getRightChild())
            if temp.getLeftChild():
                stack.insert(0,temp.getLeftChild())
    return False

n12 = BinaryTree(12)
root.(6)
root.insert(14)
root.insert(3)
print(root.PrintTree())

print(DFSBinary(root, 6))
