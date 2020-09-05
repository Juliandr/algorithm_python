class BST(object):
    def __init__(self, key, l=None, r=None):
        self.label = key
        self.left = l
        self.right = r
    

def bst_add(tree, x):
    if tree is None:
        return (BST(x), True)
    flag = False
    if x < tree.label:
        tree.left, flag = bst_add(tree.left, x)
    elif x > tree.label:
        tree.right, flag = bst_add(tree.right, x)
    return (tree, flag)

bst = BST(4)
count = 1
for i in range(4):
    _, flag = bst_add(bst, int(i))
    if flag:
        count += 1
print(count)