#%%
def BinaryTree(r):
    return [r, [], []]

def insertLeft(tree, newBranch):
    t = tree.pop(1)
    if len(t) > 1:
        tree.insert(1, [newBranch, t, []])
    else:
        tree.insert(1, [newBranch, [], []])
    return tree


def insertRight(tree, newBranch):
    t = tree.pop(2)
    if len(t) > 1:
        tree.insert(2, [newBranch, [], t])
    else:
        tree.insert(2, [newBranch, [], []])
    return tree

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal
def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]
# %%
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.leftChild
            self.leftChild = t
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.rightChild
            self.rightChild = t
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj
    def getRootVal(self):
        return self.key
# %%