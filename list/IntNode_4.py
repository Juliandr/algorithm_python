class IntNode(object):
	def __init__(self, f, r):
		self.first = f
		self.rest = r


	def size(self):
		if self.rest is None:
			return 1
		else:
			return 1 +self.rest.size()

	# def iterative_size(self):
	# 	p = self
	# 	total_size = 0
	# 	while p is not None:
	# 		total_size += 1
	# 		p = p.rest
	# 	return total_size

	def get(self, i):
		if i==0:
			return self.first
		else:
			return self.rest.get(i - 1)


l = IntNode(5, None)
l = IntNode(10, l)
l = IntNode(15, l)
print(l.size())
print(l.get(2))