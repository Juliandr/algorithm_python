class IntNode(object):
	"""docstring for IntNode"""
	def __init__(self, i, n):
		self.item = i
		self.next = n

class SLList(object):
	"""docstring for SLList"""
	def __init__(self, x):
		self.__first = IntNode(x, None)
		self.__size = 1

	def add_first(self, x):
		self.__first = IntNode(x, self.__first)
		self.__size += 1

	def get_first(self):
		return self.__first.item

	def add_last(self, x):
		p = self.__first
		while p.next is not None:
			p = p.next
		p.next = IntNode(x, None)
		self.__size += 1

	def __size(self, p):
		if p.next is None:
			return 1
		else:
			return 1 + self.__size(p.next)

	def size(self):
		return self.__size(self.__first)

	def get_size(self):
		return self.__size
l = SLList(5)
l.add_first(10)
l.add_first(15)
print(l.get_first())
print(l.get_size())