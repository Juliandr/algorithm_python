class IntNode(object):
	def __init__(self, f, r):
		self.first = f
		self.rest = r
l = IntNode(5, None)
l = IntNode(10, l)
l = IntNode(15, l)