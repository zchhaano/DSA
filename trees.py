myTree = ['a', # 根节点
        ['b', # 左子树
            ['d', [], []],
            ['e', [], []]
        ],
        ['c', # 右子树
        ['f' [], []],
            []
        ]
        ]
#创建一个新的二叉树，根节点为r
def BinaryTree(r):
    return [r, [], []]

#插入左子树
def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

#插入右子树
def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root
