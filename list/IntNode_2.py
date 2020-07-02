class IntNode(object):
	def __init__(self):
		self.first = None
		self.rest = None
l1 = IntNode()
l1.first = 5

l1.rest = IntNode()
l1.rest.first = 10
l1.rest.rest = IntNode()
l1.rest.rest.first = 15


print(l1.rest.first)