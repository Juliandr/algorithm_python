class BST(object):
    def __init__(self, key, l=None, r=None):
        self.label = key
        self.left = l
        self.right = r
    

def bst_add(tree, x):
    if tree is None:
        return BST(x)
    if x < tree.label:
        tree.left = bst_add(tree.left, x)
    elif x > tree.label:
        tree.right = bst_add(tree.right, x)
    return tree
s = input()
s_list = s.split(' ')
bst = BST(int(s_list[0]))
for item in s_list[1:]:
    bst_add(bst, int(item))
path = []
node = bst
while node:
    path.append(str(node.label))
    node = node.right
print('->'.join(path))


