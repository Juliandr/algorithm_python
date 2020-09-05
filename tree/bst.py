class BST(object):
	"""docstring for BST"""
	def __init__(self, key, left=None, right=None):
		self.left = left
		self.right = right
		self.label = key

def bst_add(tree, x):
	if tree is None:
		return BST(x)
	if x < tree.label:
		tree.left = bst_add(tree.left, x)
	else:
		tree.right = bst_add(tree.right, x)
	return tree

def bst_find(tree, search_key):
	if tree is None:
		return None
	if search_key == tree.label:
		return tree
	elif search_key < tree.label:
		return bst_find(tree.left, search_key)
	else:
		return bst_find(tree.right, search_key)