class IntNode(object):
	def __init__(self):
		self.first = None
		self.rest = None
l1 = IntNode()
l1.first = 5

l2 = IntNode()
l2.first = 10

l3 = IntNode()
l3.first = 15

l1.rest = l2
l2.rest = l3
print(l1.rest.first)

